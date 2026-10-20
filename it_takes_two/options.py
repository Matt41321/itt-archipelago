from dataclasses import dataclass

from Options import Choice, PerGameCommonOptions, Range, Toggle


class Goal(Choice):
    """What you need to unlock A Grand Finale.
    Default: collect enough 'Pages' items.
    Mini-Games: discover enough minigames."""
    display_name = "Goal"
    option_default = 0
    option_minigames = 1
    default = 0


class PageCount(Range):
    """How many Pages are in the item pool."""
    display_name = "Page Count"
    range_start = 1
    range_end = 50
    default = 5


class PagePercentage(Range):
    """The percentage of the Pages in the pool needed to unlock A Grand Finale."""
    display_name = "Page Percentage"
    range_start = 1
    range_end = 100
    default = 80


class MinigamesRequired(Range):
    """How many of the 25 minigames you need to discover to unlock A Grand Finale."""
    display_name = "Mini-Games Required"
    range_start = 1
    range_end = 25
    default = 15


class StartingMovement(Choice):
    """Which movement you start with.
    None: no movement.
    Basic Movement: Double Jump and Dash.
    Sprint: just Sprint."""
    display_name = "Starting Movement"
    option_none = 0
    option_basic_movement = 1
    option_sprint = 2
    default = 1


class StartingSubChapters(Choice):
    """Which sub-chapters you start with.
    Random Sub-Chapter: one random sub-chapter you can complete with your starting movement.
    First Of Each Chapter: the first sub-chapter of every chapter."""
    display_name = "Starting Sub-Chapters"
    option_random_sub_chapter = 0
    option_first_of_each_chapter = 1
    default = 0


class UnlockReachedSubChapters(Toggle):
    """Playing through a sub-chapter into the next one unlocks the next one in chapter select, even if you haven't
    been sent it. For example, playing through Biting the Dust into The Depths lets you teleport to The Depths."""
    display_name = "Unlock Reached Sub-Chapters"


class CheckpointSanity(Toggle):
    """Every checkpoint in the game becomes a check. The saving in the bottom right is a good indicator for if you collect a checkpoint. {Adds 282 locations}"""
    display_name = "Checkpoint Sanity"


@dataclass
class ItTakesTwoOptions(PerGameCommonOptions):
    goal: Goal
    page_count: PageCount
    page_percentage: PagePercentage
    minigames_required: MinigamesRequired
    starting_movement: StartingMovement
    starting_sub_chapters: StartingSubChapters
    unlock_reached_sub_chapters: UnlockReachedSubChapters
    checkpoint_sanity: CheckpointSanity
