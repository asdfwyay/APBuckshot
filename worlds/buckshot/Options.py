from dataclasses import dataclass
from Options import Choice, DefaultOnToggle, OptionGroup, OptionSet, PerGameCommonOptions, Range, Toggle

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
    range_end = 1000000000
    default = 1000000

class DoubleOrNothingRequirements(Choice):
    """
    Specify the requirements to unlock Double or Nothing mode

    - **Free**: Double or Nothing is unlocked from the start.
    - **Vanilla**: Double or Nothing is unlocked after beating the base game.
    - **Pills**: Double or Nothing is unlocked after obtaining the Double or Nothing Pills item in the multiworld.
    - **Vanilla Plus**: Double or Nothing is unlocked after beating the base game and finding the pills.
    """
    display_name = "Double or Nothing Requirements"
    option_free = 0
    option_vanilla = 1
    option_pills = 2
    option_vanilla_plus = 3
    default = 1

class AdditionalGoalRequirements(Choice):
    """
    Specify any additional requirements needed to reach goal.

    - **None**: No additional requirements need to be met in order to goal.
    - **Shots**: Obtain a percentage of your shotsanity checks specified by the "Shotsanity Goal Percentage" option.
    - **Streak**: Reach the maximum streak set in the "Streaksanity Count" option.
    - **Sanities**: Both shotsanity and streaksanity additional requirements are included

    If the respective sanities are not enabled, the additional goals will not be included.
    """
    display_name = "Additional Goal Requirements"
    option_none = 0
    option_shots = 1
    option_streak = 2
    option_sanities = 3
    default = 0

class AsynchronousPoints(Toggle):
    """
    If enabled, points required for a 1000K or custom goal can be obtained across multiple runs.

    Additionally, some filler items will be replaced with point increase items, which add points
    to your point total upon finding one.
    """
    display_name = "Asynchronous Points"

class PointFillerPercentage(Range):
    """
    Specify the maximum percentage of your required point total to be added as filler items.
    """
    display_name = "Point Filler Percentage"
    range_start = 0
    range_end = 100
    default = 25

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

class IncludedCustomMechanics(OptionSet):
    """
    Specify which custom mechanics are added to the game.

    ***ACTUAL OPTIONS***
    
    **Item Luck**: Adds 3 items to the pool named "Progressive Item Luck". For each progressive item luck you
    obtain, the likelihood of pulling an item increases.

    **Life Bank**: Adds a life bank to the game, accessible by clicking the icon on the top right of the UI.
    You gain life bank charges by finding items called "Life Bank Charge" spread throughout the multiworld.
    Spend a charge from your life bank any time during your turn to restore a charge during the round. Your
    charges are given back to you on a new run.

    **Item Buffs**: Finding "Item Buff" items in the multiworld will apply a permanent buff to your consumable items.

    **Item Debuffs**: Start with a selection of consumable items debuffed. Finding an item's respective "Clear Debuff"
    in the multiworld will remove its debuff.

    ***SIDE EFFECTS***

    **Poison Gauge**: A value representing the expected amount of damage you will take at the beginning
    of every turn as follows:

        Poison Gauge | Guaranteed Damage Every Turn | Chance of Losing One Extra Charge
        -------------+------------------------------+----------------------------------
              p      |    d = p / 100 rounded down  |           p / 100 - d            
        -------------+------------------------------+----------------------------------
                                           EXAMPLES                                    
        -------------+------------------------------+----------------------------------
              30     |              0               |               30%                
             100     |              1               |                0%                
             240     |              2               |               40%                

    Certain item debuffs will affect the poison gauge. The poison gauge is reset to 0 when starting a new round.
    """
    display_name = "Included Custom Mechanics"
    valid_keys = ["Item Luck", "Life Bank", "Item Buffs", "Item Debuffs"]
    default = frozenset({"Item Luck", "Life Bank", "Item Buffs"})

class ItemBuffs(OptionSet):
    """
    Specify which items to include buffs for. Ignored if "Item Buffs" is not included in "Included Custom Mechanics."

    **Hand Saw**: Deals an extra point of damage (2 -> 3)
    **Magnifying Glass**: Gains the ability to convert the current shell to either live or blank (50% success chance)
    **Beer**: Gains the ability to clear the shotgun, immediately moving on to the next batch.
    **Cigarette Pack**: 50% chance to heal 2 charges instead of 1
    **Handcuffs**: Dealer skips one extra turn (1 -> 2)
    **Expired Medicine**: Buffs chance of healing (1 in 2 -> 5 in 6)
    **Burner Phone**: Gains the ability to select which shell to get info about (2nd - 8th)
    **Adrenaline**: Gains the ability to steal the dealer's adrenaline
    **Inverter**: Applies a Schrodinger's Bullet Trap to the dealer
    """
    display_name = "Item Buffs"
    valid_keys = [
        "Hand Saw",
        "Magnifying Glass",
        "Beer",
        "Cigarette Pack",
        "Handcuffs",
        "Expired Medicine",
        "Burner Phone",
        "Adrenaline",
        "Inverter"
    ]
    default = frozenset({
        "Hand Saw",
        "Magnifying Glass",
        "Beer",
        "Cigarette Pack",
        "Handcuffs",
        "Expired Medicine",
        "Burner Phone",
        "Adrenaline",
        "Inverter"
    })

class ItemDebuffs(OptionSet):
    """
    Specify which items should start with a debuff. Ignored if "Item Debuffs" is not included in "Included Custom Mechanics."

    **Hand Saw**: 25% chance to also deal 1 damage to the player
    **Magnifying Glass**: 40% chance to gain no information when viewing the current shell
    **Beer**: Adds 15 to the poison gauge (see custom mechanics)
    **Cigarette Pack**: Adds 30 to the poison gauge (see custom mechanics)
    **Handcuffs**: 25% chance for the dealer to immediately break free
    **Expired Medicine**: Failing the coin flip will also add 20 to the poison gauge (see custom mechanics)
    **Burner Phone**: 25% chance to get no information
    **Adrenaline**: Adds 50 to the poison gauge (see custom mechanics)
    **Inverter**: 25% chance to not invert the current shell
    """
    display_name = "Item Debuffs"
    valid_keys = [
        "Hand Saw",
        "Magnifying Glass",
        "Beer",
        "Cigarette Pack",
        "Handcuffs",
        "Expired Medicine",
        "Burner Phone",
        "Adrenaline",
        "Inverter"
    ]
    default = frozenset({
        "Hand Saw",
        "Magnifying Glass",
        "Beer",
        "Cigarette Pack",
        "Handcuffs",
        "Expired Medicine",
        "Burner Phone",
        "Adrenaline",
        "Inverter"
    })

class IncludedTraps(OptionSet):
    """
    Specify which traps are added to the game.
    
    **Stolen Package Trap**: Your box will be empty the next time you draw items.

    **Schrodinger's Bullet Trap**: The current shell is randomized the next time you
    pick up the shotgun.
    """
    display_name = "Included Traps"
    valid_keys = ["Stolen Package Trap", "Schrodinger's Bullet Trap"]
    default = frozenset({"Stolen Package Trap", "Schrodinger's Bullet Trap"})

class TrapFillPercentage(Range):
    display_name = "Trap Fill Percentage"
    range_start = 0
    range_end = 100
    default = 10

class ExcludeFullHouse(DefaultOnToggle):
    """
    Specify whether the Full House achivement should be excluded from the location list.
    """
    display_name = "Exclude Full House"

class Shotsanity(Choice):
    """
    Shotsanity adds locations for every successful live and blank shot up to a specified amount.
 
    - **Off**:
        Shotsanity is disabled.
    - **Balanced**:
        Shotsanity is enabled. Consumable item logic also applies to shotsanity locations.
    - **Unreasonable**:
        Shotsanity is enabled. No logic applies to shotsanity locations.
    """
    display_name = "Shotsanity"
    option_off = 0
    option_balanced = 1
    option_unreasonable = 2
    default = 1

class ShotsanityCount(Range):
    """
    If Shotsanity is enabled, specify the number of locations to add for each successful shot.
    """
    display_name = "Shotsanity Count"
    range_start = 1
    range_end = 1000
    default = 50

class BalancedShotsanityCountPerRound(Range):
    """
    If Shotsanity is set to Balanced, specify the number of shot locations in logic during each round,
    starting from the second round of the base game.
        (e.g. If this setting is set to 10:
            - Shotsanity Locations beyond 10 expect Base Game Second Round
            - Shotsanity Locations beyond 20 expect Base Game Final Round
            - Shotsanity Locations beyond 30 expect Double or Nothing - 1 Round
            and so on...
        )

    No matter what value is set, all shotsanity locations will be in logic after beating the penultimate round before
    your goal.
        - If your goal is 70K, all shotsanity locations are in logic after Base Game Second Round.
        - If your goal is 140K, all shotsanity locations are in logic after Double or Nothing - 5 Rounds.
        - If your goal is 1000K, all shotsanity locations are in logic after Double or Nothing - 14 Rounds.

    You are **NOT** restricted from obtaining shotsanity locations out of logic.
    """
    display_name = "Balanced Shotsanity Live Count Per Round"
    range_start = 1
    range_end = 1000
    default = 5

class ShotsanityGoalPercentage(Range):
    """
    If included as an additional goal requirement, specify the percentage of
    shotsanity checks needed for goal.
    """
    display_name = "Shotsanity Goal Percentage"
    range_start = 1
    range_end = 100
    default = 100

class Streaksanity(Choice):
    """
    Streaksanity adds locations for every successful shot made on the dealer in a row without losing health (or resetting).
 
    - **Off**:
        Streaksanity is disabled.
    - **Logical**:
        Streaksanity is enabled. Logic will be applied to streak locations as follows:
        
        A score is calculated based on your currently obtained items:
            - Handcuffs: +2 pts
            - Magnifying Glass: +1 pt
            - Beer: +1 pt
            - Burner Phone: +1 pt (if Double or Nothing is accessible)
            - Adrenaline: +1 pt (if Double or Nothing is accessible)
            - Inverter: +1 pt (if Double or Nothing is accessible)
        A streak of `n` will require a score of at least `n + 3`.
        In addition, all streaks of at least 5 logically require handcuffs.
    - **Unreasonable**:
        Streaksanity is enabled. No logic applies to streaksanity locations.
    """
    display_name = "Streaksanity"
    option_off = 0
    option_logical = 1
    option_unreasonable = 2
    default = 0

class StreaksanityCount(Range):
    """
    If Streaksanity is enabled, specify the maximum streak to be included.
    """
    display_name = "Streaksanity Count"
    range_start = 2
    range_end = 10
    default = 7

@dataclass
class BuckshotRouletteOptions(PerGameCommonOptions):
    goal: Goal
    custom_goal_amount: CustomGoalAmount
    double_or_nothing_requirements: DoubleOrNothingRequirements
    consumable_item_logic: ConsumableItemLogic
    included_custom_mechanics: IncludedCustomMechanics
    item_buffs: ItemBuffs
    item_debuffs: ItemDebuffs
    included_traps: IncludedTraps
    trap_fill_percentage: TrapFillPercentage
    exclude_full_house: ExcludeFullHouse
    shotsanity: Shotsanity
    shotsanity_count: ShotsanityCount
    balanced_shotsanity_count_per_round: BalancedShotsanityCountPerRound
    streaksanity: Streaksanity
    streaksanity_count: StreaksanityCount

option_groups = [
    OptionGroup("Goal", [
        Goal,
        CustomGoalAmount,
        DoubleOrNothingRequirements,
        AdditionalGoalRequirements,
        AsynchronousPoints,
        PointFillerPercentage
    ]),
    OptionGroup("Difficulty", [
        ConsumableItemLogic,
        IncludedCustomMechanics,
        ItemBuffs,
        ItemDebuffs,
        IncludedTraps,
        TrapFillPercentage
    ]),
    OptionGroup("Achievements", [
        ExcludeFullHouse
    ]),
    OptionGroup("Shotsanity", [
        Shotsanity,
        ShotsanityCount,
        BalancedShotsanityCountPerRound,
        ShotsanityGoalPercentage
    ]),
    OptionGroup("Streaksanity", [
        Streaksanity,
        StreaksanityCount
    ])
]