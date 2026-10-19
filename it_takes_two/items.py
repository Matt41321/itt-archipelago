from typing import NamedTuple

from BaseClasses import Item, ItemClassification

from .chapter_data import CHAPTERS

GAME_NAME = "It Takes Two"
ITEM_ID_BASE = 7_720_000


class ItTakesTwoItem(Item):
    game = GAME_NAME


class ItemData(NamedTuple):
    id: int
    classification: ItemClassification
    capability_tag: str = ""  # movement items only


CHAPTER_ITEMS: dict[str, ItemData] = {
    chapter.name: ItemData(ITEM_ID_BASE + 300 + chapter.index, ItemClassification.progression)
    for chapter in CHAPTERS if not chapter.is_minigame
}

# Item -> the capability tag the game mod blocks until it arrives.
MOVEMENT_ITEMS: dict[str, ItemData] = {
    "Double Jump": ItemData(ITEM_ID_BASE + 100, ItemClassification.progression, "AirJump"),
    "Dash": ItemData(ITEM_ID_BASE + 101, ItemClassification.progression, "Dash"),
    "Ground Pound": ItemData(ITEM_ID_BASE + 103, ItemClassification.progression, "GroundPound"),
    "Wall Jump": ItemData(ITEM_ID_BASE + 104, ItemClassification.progression, "WallSlide"),
    "Swinging": ItemData(ITEM_ID_BASE + 105, ItemClassification.progression, "Swinging"),
    "Grinding": ItemData(ITEM_ID_BASE + 106, ItemClassification.progression, "Grinding"),
    "Sprint": ItemData(ITEM_ID_BASE + 107, ItemClassification.progression, "SprintActivation"),
    "Slide": ItemData(ITEM_ID_BASE + 108, ItemClassification.progression, "SlopeSlide"),
    "Ledge Grab": ItemData(ITEM_ID_BASE + 109, ItemClassification.progression, "LedgeGrab"),
}

class Ability(NamedTuple):
    id: int
    tags: tuple[str, ...]  # capability tags the game mod blocks until it arrives
    owner: str = ""


# Each area's abilities, one item per character. Must match Abilities in main.lua.
ABILITIES: dict[str, Ability] = {
    "Shed May Ability": Ability(ITEM_ID_BASE + 420, ("HammerWeapon", "HammerSmash", "WeaponHammer")),  # Hammer
    "Shed Cody Ability": Ability(ITEM_ID_BASE + 421, ("NailWeapon",)),  # Nail Throw
    "Tree May Ability": Ability(ITEM_ID_BASE + 422, ("MatchWeapon",)),  # Match Gun
    "Tree Cody Ability": Ability(ITEM_ID_BASE + 423, ("SapWeapon",)),  # Sap Gun
    "Rose's Room May Ability": Ability(ITEM_ID_BASE + 424, ("Gravity",), owner="May"),  # Gravity Boots
    "Rose's Room Cody Ability": Ability(ITEM_ID_BASE + 425, ("ChangeSize", "MutuallyExclusiveSize")),  # Size Change
    "Cuckoo Clock May Ability": Ability(ITEM_ID_BASE + 426, ("TimeSequenceCapability", "Sequence")),  # Time Clone
    "Cuckoo Clock Cody Ability": Ability(ITEM_ID_BASE + 427, ("TimeControlCapability", "TimeControlling")),  # Time Control
    "Snow Globe Ability": Ability(ITEM_ID_BASE + 428, ("MagneticCapability", "MagnetCapability",
                                                      "MagneticPlayerAttraction", "PlayerMagnetLaunch")),  # Magnets
    "Garden May Ability": Ability(ITEM_ID_BASE + 430, ("WaterHose", "SickleName", "SickleAttackName")),  # Water Hose, Scythe
    "Garden Cody Ability": Ability(ITEM_ID_BASE + 431, ("Vine",)),  # Vine Whip
    "Attic May Ability": Ability(ITEM_ID_BASE + 432, ("PowerfulSong", "SongOfLife")),  # Singing
    "Attic Cody Ability": Ability(ITEM_ID_BASE + 433, ("Cymbal", "CymbalShield")),  # Cymbal
}
ABILITY_ITEMS: dict[str, ItemData] = {
    name: ItemData(ability.id, ItemClassification.progression) for name, ability in ABILITIES.items()
}

FILLER_ITEM_NAME = "Clockwork Gear"
FILLER_ITEMS: dict[str, ItemData] = {
    FILLER_ITEM_NAME: ItemData(ITEM_ID_BASE + 200, ItemClassification.filler),
}

PAGE_ITEM_NAME = "Page"
GOAL_ITEMS: dict[str, ItemData] = {
    PAGE_ITEM_NAME: ItemData(ITEM_ID_BASE + 201, ItemClassification.progression_skip_balancing),
}

BASIC_MOVEMENT = ("Double Jump", "Dash")

ITEM_TABLE: dict[str, ItemData] = {**CHAPTER_ITEMS, **MOVEMENT_ITEMS, **ABILITY_ITEMS, **FILLER_ITEMS, **GOAL_ITEMS}
ITEM_NAME_TO_ID: dict[str, int] = {name: data.id for name, data in ITEM_TABLE.items()}

ITEM_GROUPS: dict[str, set[str]] = {
    "Chapters": set(CHAPTER_ITEMS),
    "Movement": set(MOVEMENT_ITEMS),
    "Abilities": set(ABILITY_ITEMS),
}
for _chapter in CHAPTERS:
    if not _chapter.is_minigame:
        ITEM_GROUPS.setdefault(_chapter.group, set()).add(_chapter.name)
