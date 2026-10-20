"""It Takes Two client.

Talks to the game mod through files in %LOCALAPPDATA%/ItTakesTwoArchipelago:
  ap_state.txt   unlocked items, written here
  checks.txt     checks sent, written by the mod
  heartbeat.txt  updated here while connected; the mod does nothing without it
"""
import asyncio
import os
import time
from pathlib import Path

import Utils
from CommonClient import (ClientCommandProcessor, CommonContext, get_base_parser, gui_enabled, handle_url_arg, logger,
                          server_loop)
from NetUtils import ClientStatus

from .items import ABILITY_ITEMS, CHAPTER_ITEMS, GAME_NAME, MOVEMENT_ITEMS, PAGE_ITEM_NAME
from .locations import (CHECKPOINT_KEY_TO_LOCATION, DISCOVERY_LOCATIONS, FINAL_CHAPTER, LOCATION_NAME_TO_ID,
                        MINIGAMES, discovery_location_name)

BRIDGE_DIR = Path(os.getenv("LOCALAPPDATA", Path.home())) / "ItTakesTwoArchipelago"
STATE_FILE = BRIDGE_DIR / "ap_state.txt"
CHECKS_FILE = BRIDGE_DIR / "checks.txt"
SEED_FILE = BRIDGE_DIR / "seed.txt"
LAST_CHAPTER_FILE = BRIDGE_DIR / "last_chapter.txt"
HEARTBEAT_FILE = BRIDGE_DIR / "heartbeat.txt"
GOAL_LINE = "!goal"
CHECKPOINT_PREFIX = "cp:"
REACHED_PREFIX = "reached:"
POLL_SECONDS = 0.5


class ItTakesTwoCommandProcessor(ClientCommandProcessor):
    def _cmd_bridge(self) -> bool:
        """Show the folder used to talk to the game."""
        logger.info(f"Bridge folder: {BRIDGE_DIR}")
        return True


class ItTakesTwoContext(CommonContext):
    game = GAME_NAME
    items_handling = 0b111
    command_processor = ItTakesTwoCommandProcessor

    def __init__(self, server_address: str | None, password: str | None) -> None:
        super().__init__(server_address, password)
        self.checks_read = 0
        self.goal_sent = False
        self.seed_movement: set[str] = set(MOVEMENT_ITEMS)
        self.goal: str | None = None  # "default" or "minigames"
        self.goal_required = 0
        self.goal_progress_logged = 0
        self.unlock_reached = False
        self.reached_chapters: set[str] = set()  # sub-chapters played into, from checks.txt
        self.room_seed_name: str | None = None
        BRIDGE_DIR.mkdir(parents=True, exist_ok=True)

    async def server_auth(self, password_requested: bool = False) -> None:
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd: str, args: dict) -> None:
        if cmd == "RoomInfo":
            self.room_seed_name = args["seed_name"]
        elif cmd == "Connected":
            slot_data = args.get("slot_data", {})
            self.seed_movement = set(slot_data.get("movement_tags", MOVEMENT_ITEMS))
            self.goal = slot_data.get("goal")
            required_key = "minigames_required" if self.goal == "minigames" else "pages_required"
            self.goal_required = slot_data.get(required_key, 0)
            self.goal_progress_logged = 0
            self.unlock_reached = slot_data.get("unlock_reached_sub_chapters", False)
            # Re-read checks.txt from the start.
            self.checks_read = 0
            self.reached_chapters = set()
            self.goal_sent = False
            self.reset_bridge_for_new_seed()
            self.write_state()
        elif cmd == "ReceivedItems":
            self.write_state()
        elif cmd == "RoomUpdate" and "checked_locations" in args:
            self.write_state()

    async def disconnect(self, allow_autoreconnect: bool = False) -> None:
        clear_bridge_connection()
        await super().disconnect(allow_autoreconnect)

    def reset_bridge_for_new_seed(self) -> None:
        slot_id = f"{self.room_seed_name}:{self.slot}"
        previous = SEED_FILE.read_text(encoding="utf-8").strip() if SEED_FILE.exists() else None
        if previous != slot_id:
            if previous is not None:
                logger.info("New seed or slot: clearing checks left over from the previous one.")
            CHECKS_FILE.unlink(missing_ok=True)
            LAST_CHAPTER_FILE.unlink(missing_ok=True)
            SEED_FILE.write_text(slot_id + "\n", encoding="utf-8")

    def goal_progress(self) -> tuple[str, int]:
        if self.goal == "minigames":
            return "Mini-games discovered", sum(location in self.checked_locations
                                                for location in DISCOVERY_LOCATIONS.values())
        received = [self.item_names.lookup_in_game(item.item, GAME_NAME) for item in self.items_received]
        return "Pages", received.count(PAGE_ITEM_NAME)

    def available_items(self) -> set[str]:
        """Item names the game has unlocked, including the finale once the goal is met."""
        available = {self.item_names.lookup_in_game(item.item, GAME_NAME) for item in self.items_received}
        available |= set(MOVEMENT_ITEMS) - self.seed_movement
        if self.unlock_reached:
            available |= self.reached_chapters
        if self.goal is not None:
            _, progress = self.goal_progress()
            available.discard(FINAL_CHAPTER)
            if progress >= self.goal_required:
                available.add(FINAL_CHAPTER)
        return available

    def write_state(self) -> None:
        if self.goal is not None:
            label, progress = self.goal_progress()
            if progress > self.goal_progress_logged:
                self.goal_progress_logged = progress
                logger.info(f"{label}: {progress}/{self.goal_required}"
                            + (f" - {FINAL_CHAPTER} is unlocked!" if progress >= self.goal_required else ""))
        received = self.available_items()
        lines = ["connected"]
        lines += [f"chapter:{name}" for name in CHAPTER_ITEMS if name in received]
        lines += [f"move:{data.capability_tag}" for name, data in MOVEMENT_ITEMS.items() if name in received]
        lines += [f"ability:{name}" for name in ABILITY_ITEMS if name in received]
        # Discovered minigames, for the minigame menus.
        lines += [f"minigame:{minigame.name}" for minigame in MINIGAMES
                  if DISCOVERY_LOCATIONS[discovery_location_name(minigame)] in self.checked_locations]
        tmp = STATE_FILE.with_suffix(".tmp")
        tmp.write_text("\n".join(lines) + "\n", encoding="utf-8")
        tmp.replace(STATE_FILE)

    async def poll_checks(self) -> None:
        if not CHECKS_FILE.exists():
            return
        lines = CHECKS_FILE.read_text(encoding="utf-8").splitlines()
        if len(lines) < self.checks_read:
            self.checks_read = 0
        new_lines, self.checks_read = lines[self.checks_read:], len(lines)

        locations = []
        reached_before = len(self.reached_chapters)
        for line in new_lines:
            line = line.strip()
            if line.startswith(REACHED_PREFIX):
                # Played into this sub-chapter; only unlocks it with Unlock Reached Sub-Chapters on.
                name = line.removeprefix(REACHED_PREFIX)
                if name in CHAPTER_ITEMS and name != FINAL_CHAPTER and name not in self.reached_chapters:
                    self.reached_chapters.add(name)
                    if self.unlock_reached:
                        logger.info(f"Reached {name}: it's unlocked in chapter select")
            elif line == GOAL_LINE:
                if not self.goal_sent:
                    self.goal_sent = True
                    await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                    logger.info("Goal complete!")
            elif line.startswith(CHECKPOINT_PREFIX):
                # Only counts with checkpoint sanity on.
                name = CHECKPOINT_KEY_TO_LOCATION.get(line.removeprefix(CHECKPOINT_PREFIX))
                location = LOCATION_NAME_TO_ID.get(name)
                if location in self.missing_locations or location in self.checked_locations:
                    locations.append(location)
            elif line in LOCATION_NAME_TO_ID:
                locations.append(LOCATION_NAME_TO_ID[line])
            elif line:
                logger.warning(f"Game reported unknown location: {line}")

        if self.unlock_reached and len(self.reached_chapters) != reached_before:
            self.write_state()

        new_locations = [loc for loc in locations if loc not in self.checked_locations]
        if new_locations:
            await self.check_locations(new_locations)

    def run_gui(self) -> None:
        from kvui import GameManager

        class ItTakesTwoManager(GameManager):
            base_title = "Archipelago It Takes Two Client"

            def build(self):
                container = super().build()
                from .tracker import TrackerTab
                self.add_client_tab("Tracker", TrackerTab(self.ctx))
                return container

        self.ui = ItTakesTwoManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")


def clear_bridge_connection() -> None:
    """Tell the mod we're disconnected."""
    HEARTBEAT_FILE.unlink(missing_ok=True)
    STATE_FILE.unlink(missing_ok=True)


async def game_loop(ctx: ItTakesTwoContext) -> None:
    while not ctx.exit_event.is_set():
        if ctx.server and ctx.slot is not None:
            try:
                HEARTBEAT_FILE.write_text(f"{int(time.time())}\n", encoding="utf-8")
                await ctx.poll_checks()
            except OSError as error:
                logger.warning(f"Could not read {CHECKS_FILE}: {error}")
        await asyncio.sleep(POLL_SECONDS)


def launch(*args: str) -> None:
    Utils.init_logging("ItTakesTwoClient", exception_logger="Client")

    parser = get_base_parser(description="It Takes Two Archipelago client.")
    parser.add_argument("--name", default=None, help="Slot name to connect as.")
    parser.add_argument("url", nargs="?", help="Archipelago connection url")
    parsed = handle_url_arg(parser.parse_args(args), parser=parser)

    async def main() -> None:
        ctx = ItTakesTwoContext(parsed.connect, parsed.password)
        ctx.auth = parsed.name
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="ServerLoop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        loop_task = asyncio.create_task(game_loop(ctx), name="GameLoop")
        await ctx.exit_event.wait()
        await ctx.shutdown()
        loop_task.cancel()
        clear_bridge_connection()

    import colorama
    colorama.just_fix_windows_console()
    asyncio.run(main())
    colorama.deinit()
