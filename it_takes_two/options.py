from dataclasses import dataclass

from Options import Choice, DefaultOnToggle, PerGameCommonOptions, Range, Toggle


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


class StartWithBasicMovement(DefaultOnToggle):
    """Start with Double Jump and Dash."""
    display_name = "Start With Basic Movement"


class CheckpointSanity(Toggle):
    """Every checkpoint in the game becomes a check. The saving in the bottom right is a good indicator for if you collect a checkpoint. {Adds 282 locations}"""
    display_name = "Checkpoint Sanity"


@dataclass
class ItTakesTwoOptions(PerGameCommonOptions):
    goal: Goal
    page_count: PageCount
    page_percentage: PagePercentage
    minigames_required: MinigamesRequired
    start_with_basic_movement: StartWithBasicMovement
    checkpoint_sanity: CheckpointSanity
