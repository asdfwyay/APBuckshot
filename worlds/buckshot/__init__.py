from BaseClasses import ItemClassification as IC, Tutorial
from worlds.AutoWorld import WebWorld, World
from .Enums import *
from .Items import BuckshotRouletteItem, item_table
from .Locations import BuckshotRouletteLocation, LocationData, location_table
from .Options import BuckshotRouletteOptions, option_groups
from .Regions import BuckshotRouletteRegion, region_table

class BuckshotWebWorld(WebWorld):
    theme = "stone"

    setup_en = Tutorial(
        tutorial_name="Multiworld Setup Guide",
        description="A guide to playing Buckshot Roulette",
        language="English",
        file_name="setup_en.md",
        link="setup/en",
        authors=["asdfwyay"]
    )

    tutorials = [setup_en]

class BuckshotWorld(World):
    """A Game by Mike Klubnika"""
    
    game = "Buckshot Roulette"
    web = BuckshotWebWorld()
    options: BuckshotRouletteOptions
    options_dataclass = BuckshotRouletteOptions
    location_name_to_id = location_table
    item_name_to_id = item_table

    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)
        self.included_locations = dict[str, LocationData]()

    def get_filler_items(self) -> list[str]:
        return [
            item_name
            for item_name, item_data in item_table.items()
            if item_data.classification == IC.filler
        ]

    def create_item(self, item_name: str) -> BuckshotRouletteItem:
        return BuckshotRouletteItem(item_name, item_table[item_name].classification, item_table[item_name].id, self.player)

    def create_items(self) -> None:
        # Setup Item Pool
        included_item_flags: int = I_CONSUMABLE
        filler_items: list[str] = self.get_filler_items()
        location_count: int = len(self.get_locations())

        if self.options.goal != "70k":
            included_item_flags |= I_DOUBLE_OR_NOTHING
        if self.options.double_or_nothing_requirements in ["pills", "vanilla_plus"]:
            included_item_flags |= I_PILLS

        # Add Progression Items
        item_pool: list[BuckshotRouletteItem] = [
            self.create_item(item_name)
            for item_name, item_data in item_table.items()
            if item_data.flags & included_item_flags == included_item_flags
        ]
        location_count -= len(item_pool)

        # Add Filler Items
        item_pool += [self.create_item(
            self.random.choice(filler_items) for _ in range(location_count)
        )]

        self.multiworld.itempool += item_pool

    def create_regions_and_locations(self) -> None:
        # Setup Locations
        included_location_flags: int = 0x00

        if self.options.achievements:
            included_location_flags |= L_ACHIEVEMENT
            if self.options.goal == "1000k" or (self.options.goal == "custom" and self.options.custom_goal_amount >= 1000000):
                included_location_flags |= L_LARGE_GOAL
            if not self.options.exclude_full_house:
                included_location_flags |= L_FULL_HOUSE
        if self.options.goal != "70k":
            included_location_flags |= L_DOUBLE_OR_NOTHING
        if self.options.shotsanity != "disabled":
            included_location_flags |= L_SHOTSANITY

        self.included_locations = {
            location_name: location_data
            for location_name, location_data in location_table.items()
            if location_data.flags & included_location_flags == included_location_flags
        }

        # Create region graph and add locations
        for region_name, region_data in region_table.items():
            region = BuckshotRouletteRegion(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

            region_filtered_locations: dict[str, int] = {
                location_name: location_data.id
                for location_name, location_data in self.included_locations.items()
                if location_data.region == region_name
            }

            region.add_locations(region_filtered_locations, BuckshotRouletteLocation)
            region.add_exits(region_data.connecting_regions)

