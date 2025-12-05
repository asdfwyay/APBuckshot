from Options import Choice, Range

class Goal(Choice):
    """
    Specify the goal for your game.

    - **70K**: Beat the base game.
    - **140K**: Win Double or Nothing mode after doubling your earnings.
    - **1000K**: Cash out a minimum of $1,000,000 in Double or Nothing mode.
    - **Custom**: Cash out a mininum of a specified amount of money in Double or Nothing mode.
    """
    display_name = "Goal"
    option_70k = 0
    option_140k = 1
    option_1000k = 2
    option_custom = 3
    default = 1

class CustomGoalAmount(Range):
    """
    If Goal is set to Custom, specify the minimum amount of money needed to be cashed out.
    """
    display_name = "Custom Goal Amount"
    range_start = 1
    range_end = 100000000
    default = 1000000

class ConsumableItemLogic(Choice):
    """
    Specify how consumable items affect the logic for your game. In solo worlds, this only has a noticeable effect
    when Goal is 1000K or Custom (with a sufficiently large goal amount).

    - **Tight**:
        Two consumable items are expected before beating the 2nd round of the base game.
        Three consumable items are expected before beating the 3rd round of the base game.
        An additional item is expected for every round of Double or Nothing.
            (e.g. The 140K goal will logically expect obtaining every consumable item before goaling)

    - **Normal**:
        One consumable item is expected before beating the 2nd round of the base game.
        Two consumable items are expected before beating the 3rd round of the base game.
        An additional item is expected for every 3 rounds of Double or Nothing.
            (e.g. The 140K goal will logically expect obtaining 4 consumable items before goaling,
                  The 1000K goal will logically expect obtaining every consumable item before goaling)

    - **Minimal**:
        No consumable items are expected before beating the base game.
        An additional item is expected for every 3 rounds of Double or Nothing.
            (e.g. The 140K goal will logically expect obtaining 2 consumable items before goaling,
                  The 1000K goal will logically expect obtaining 7 consumable items before goaling)

    - **None**: Consumable items are not considered logically required for goal
        (except for obtaining certain achievements).
    """
    display_name = "Consumable Item Logic"
    option_tight = 0
    option_normal = 1
    option_minimal = 2
    option_none = 3
    default = 1

class Achievements(Choice):
    """
    Specify whether achievements are added as locations to your game.

    - **Enabled**: Achivements are considered locations.
    - **Disabled**: Achivements are not considered locations.
    """
    display_name = "Achivements"
    option_enabled = 0
    option_disabled = 1
    default = 0

class ExcludeFullHouse(Choice):
    """
    Specify whether the Full House achivement should be excluded from the location list.
    """
    display_name = "Exclude Full House"
    option_yes = 0
    option_no = 1
    default = 0

class EnableShotsanity(Choice):
    """
    Shotsanity adds locations for every successful live and blank shot up to a specified amount
    """
    display_name = "Shotsanity"
    option_yes = 0
    option_no = 1
    default = 0

class ShotsanityLiveCount(Range):
    """
    If Shotsanity is enabled, specify the number of locations to add for each successful live shot.
    """
    display_name = "Shotsanity Live Count"
    range_start = 1
    range_end = 500
    default = 50

class ShotsanityBlankCount(Range):
    """
    If Shotsanity is enabled, specify the number of locations to add for each successful blank shot.
    """
    display_name = "Shotsanity Blank Count"
    range_start = 1
    range_end = 500
    default = 50