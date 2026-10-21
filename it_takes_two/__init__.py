import logging
import math
from typing import Any

from BaseClasses import ItemClassification, Region
from worlds.AutoWorld import World
from worlds.LauncherComponents import Component, Type, components, launch_subprocess

from .chapter_data import CHAPTERS
from .items import (ABILITY_ITEMS, BASIC_MOVEMENT, CHAPTER_ITEMS, FILLER_ITEM_NAME, GAME_NAME, ITEM_GROUPS,
                    ITEM_NAME_TO_ID, ITEM_TABLE, MOVEMENT_ITEMS, PAGE_ITEM_NAME, ItTakesTwoItem)
from .locations import (CHECKPOINT_LOCATIONS, COMPLETION_LOCATIONS, DISCOVERY_LOCATIONS, FINAL_CHAPTER,
                        LOCATION_GROUPS, LOCATION_NAME_TO_ID, MINIGAME_EVENT, MINIGAMES, STORY_CHAPTERS, VICTORY_EVENT,
                        ItTakesTwoLocation, completion_location_name, discovery_location_name)
from .logic_data import NODES
from .options import Goal, ItTakesTwoOptions, StartingMovement, StartingSubChapters, itt_option_groups
from .rules import ENTRANCES, FINALE_REQUIREMENTS, node_of, reachable_nodes

def launch_client(*args: str) -> None:
    from .client import launch
    launch_subprocess(launch, name="ItTakesTwoClient", args=args)


components.append(Component("It Takes Two Client", func=launch_client, component_type=Type.CLIENT))


class ItTakesTwoWorld(World):
    """
    It Takes Two is a co-op platformer about Cody and May, a couple turned into dolls who must work together to get
    back to their daughter. Both players share one slot: every item applies to both characters.
    """
    game = GAME_NAME
    options_dataclass = ItTakesTwoOptions
    options: ItTakesTwoOptions

    item_name_to_id = ITEM_NAME_TO_ID
    location_name_to_id = LOCATION_NAME_TO_ID
    item_name_groups = ITEM_GROUPS
    location_name_groups = LOCATION_GROUPS

    start_chapters: list[str]
    starting_movement: tuple[str, ...]
    page_count: int
    pages_required: int

    def create_item(self, name: str) -> ItTakesTwoItem:
        data = ITEM_TABLE[name]
        return ItTakesTwoItem(name, data.classification, data.id, self.player)

    def generate_early(self) -> None:
        self.starting_movement = {StartingMovement.option_none: (),
                                  StartingMovement.option_basic_movement: BASIC_MOVEMENT,
                                  StartingMovement.option_sprint: ("Sprint",)}[self.options.starting_movement.value]
        if self.options.starting_sub_chapters == StartingSubChapters.option_first_of_each_chapter:
            # Start with the first sub-chapter of every chapter
            firsts: dict[str, str] = {}
            for chapter in STORY_CHAPTERS:
                firsts.setdefault(chapter.group, chapter.name)
            self.start_chapters = list(firsts.values())
        else:
            # Start with a random sub-chapter
            candidates = [chapter.name for chapter in STORY_CHAPTERS if chapter.name != FINAL_CHAPTER
                          and completion_location_name(chapter) in reachable_nodes({*self.starting_movement,
                                                                                    chapter.name})]
            self.start_chapters = [self.random.choice(candidates)]

        if self.options.goal == Goal.option_minigames:
            self.page_count = self.pages_required = 0
            return

        # Pages unlock the finale. There can't be more Pages than free locations.
        locations = len(COMPLETION_LOCATIONS) + len(DISCOVERY_LOCATIONS)
        if self.options.checkpoint_sanity:
            locations += len(CHECKPOINT_LOCATIONS)
        free = locations - len(self.pool_item_names())
        self.page_count = min(self.options.page_count.value, free)
        if self.page_count < self.options.page_count.value:
            logging.warning(f"{self.player_name}: only {free} free locations, so Page Count is lowered from "
                            f"{self.options.page_count.value} to {free}")
        self.pages_required = max(1, math.ceil(self.page_count * self.options.page_percentage.value / 100))

    def pool_item_names(self) -> list[str]:
        """Every item that goes in the pool apart from Pages and filler."""
        return [name for name in [*CHAPTER_ITEMS, *MOVEMENT_ITEMS, *ABILITY_ITEMS]
                if name not in (*self.start_chapters, FINAL_CHAPTER) and name not in self.starting_movement]

    def create_regions(self) -> None:
        menu = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu)

        # One region per logic node
        nodes: dict[str, Region] = {}
        for node in NODES:
            nodes[node] = Region(node, self.player, self.multiworld)
            self.multiworld.regions.append(nodes[node])
        for node, ways in ENTRANCES.items():
            combinations_by_source: dict[str | None, list[tuple[str, ...]]] = {}
            for source, needed in ways:
                if source is None:
                    needed = (*needed, NODES[node])
                combinations_by_source.setdefault(source, []).append(needed)
            for source, combinations in combinations_by_source.items():
                origin = menu if source is None else nodes[source]
                origin.connect(nodes[node], f"{origin.name} -> {node}", self.combination_rule(combinations))

        finale = Region(FINAL_CHAPTER, self.player, self.multiworld)
        self.multiworld.regions.append(finale)
        if self.options.goal == Goal.option_minigames:
            required = self.options.minigames_required.value
            menu.connect(finale, rule=lambda state: state.has(MINIGAME_EVENT, self.player, required))
        else:
            menu.connect(finale, rule=lambda state: state.has(PAGE_ITEM_NAME, self.player, self.pages_required))
        event = ItTakesTwoLocation(self.player, VICTORY_EVENT, None, finale)
        event.place_locked_item(ItTakesTwoItem(VICTORY_EVENT, ItemClassification.progression, None, self.player))
        event.access_rule = lambda state: state.has_all(FINALE_REQUIREMENTS, self.player)
        finale.locations.append(event)

        names = [*COMPLETION_LOCATIONS, *DISCOVERY_LOCATIONS]
        if self.options.checkpoint_sanity:
            names += CHECKPOINT_LOCATIONS
        for name in names:
            region = nodes[node_of(name)]
            region.locations.append(ItTakesTwoLocation(self.player, name, LOCATION_NAME_TO_ID[name], region))

        if self.options.goal == Goal.option_minigames:
            for minigame in MINIGAMES:
                region = nodes[discovery_location_name(minigame)]
                event = ItTakesTwoLocation(self.player, f"{minigame.name} Discovery Event", None, region)
                event.place_locked_item(ItTakesTwoItem(MINIGAME_EVENT, ItemClassification.progression, None,
                                                       self.player))
                region.locations.append(event)

    def combination_rule(self, combinations: list[tuple[str, ...]]):
        """Any one of these item combinations is enough."""
        if any(not needed for needed in combinations):
            return None
        return lambda state: any(state.has_all(needed, self.player) for needed in combinations)

    def create_items(self) -> None:
        for name in self.start_chapters:
            self.multiworld.push_precollected(self.create_item(name))
        for name in self.starting_movement:
            self.multiworld.push_precollected(self.create_item(name))
        pool = [self.create_item(name) for name in self.pool_item_names()]
        pool += [self.create_item(PAGE_ITEM_NAME) for _ in range(self.page_count)]

        unfilled = len(self.multiworld.get_unfilled_locations(self.player))
        pool += [self.create_item(FILLER_ITEM_NAME) for _ in range(unfilled - len(pool))]
        self.multiworld.itempool += pool

    def set_rules(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: state.has(VICTORY_EVENT, self.player)

    def get_filler_item_name(self) -> str:
        return FILLER_ITEM_NAME

    def fill_slot_data(self) -> dict[str, Any]:
        return {
            "start_chapters": self.start_chapters,
            "unlock_reached_sub_chapters": bool(self.options.unlock_reached_sub_chapters),
            "checkpoint_sanity": bool(self.options.checkpoint_sanity),
            "starting_movement": self.options.starting_movement.current_key,
            "goal": self.options.goal.current_key,
            "page_count": self.page_count,
            "pages_required": self.pages_required,
            "minigames_required": self.options.minigames_required.value,
            "movement_tags": {name: data.capability_tag for name, data in MOVEMENT_ITEMS.items()},
            "chapters": [
                {"index": c.index, "name": c.name, "group": c.group, "level": c.level,
                 "progress_point": c.progress_point, "is_minigame": c.is_minigame}
                for c in CHAPTERS
            ],
        }
