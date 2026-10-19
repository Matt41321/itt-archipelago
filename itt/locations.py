from BaseClasses import Location

from .chapter_data import CHAPTERS, Chapter
from .checkpoint_data import CHECKPOINTS
from .items import GAME_NAME

LOCATION_ID_BASE = 7_720_000
COMPLETION_OFFSET = 0
DISCOVERY_OFFSET = 1000
CHECKPOINT_OFFSET = 2000

FINAL_CHAPTER = "A Grand Finale"
VICTORY_EVENT = "Ending"
MINIGAME_EVENT = "Mini-Game Discovered"


class ItTakesTwoLocation(Location):
    game = GAME_NAME


def completion_location_name(chapter: Chapter) -> str:
    return f"{chapter.name} Complete"


def discovery_location_name(chapter: Chapter) -> str:
    return f"{chapter.name} Discovered"


STORY_CHAPTERS: list[Chapter] = [c for c in CHAPTERS if not c.is_minigame]
MINIGAMES: list[Chapter] = [c for c in CHAPTERS if c.is_minigame]

# The story chapter each minigame is in.
MINIGAME_HOST: dict[str, Chapter] = {}
_host = None
for _chapter in CHAPTERS:
    if _chapter.is_minigame:
        MINIGAME_HOST[_chapter.name] = _host
    else:
        _host = _chapter

# The final chapter's completion is the goal event, not a location.
COMPLETION_LOCATIONS: dict[str, int] = {
    completion_location_name(c): LOCATION_ID_BASE + COMPLETION_OFFSET + c.index
    for c in STORY_CHAPTERS if c.name != FINAL_CHAPTER
}
DISCOVERY_LOCATIONS: dict[str, int] = {
    discovery_location_name(c): LOCATION_ID_BASE + DISCOVERY_OFFSET + c.index
    for c in MINIGAMES
}

# Checkpoint sanity
CHECKPOINT_KEY_TO_LOCATION: dict[str, str] = {key: name for key, _, name in CHECKPOINTS}
CHECKPOINT_CHAPTER: dict[str, str] = {name: chapter for _, chapter, name in CHECKPOINTS}
CHECKPOINT_LOCATIONS: dict[str, int] = {
    name: LOCATION_ID_BASE + CHECKPOINT_OFFSET + index for index, name in enumerate(dict.fromkeys(CHECKPOINT_CHAPTER))
}
LOCATION_NAME_TO_ID: dict[str, int] = {**COMPLETION_LOCATIONS, **DISCOVERY_LOCATIONS, **CHECKPOINT_LOCATIONS}

LOCATION_GROUPS: dict[str, set[str]] = {
    "Chapter Completions": set(COMPLETION_LOCATIONS),
    "Minigame Discoveries": set(DISCOVERY_LOCATIONS),
    "Checkpoints": set(CHECKPOINT_LOCATIONS),
}
