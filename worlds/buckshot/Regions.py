from dataclasses import dataclass, field
from BaseClasses import Region
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import BuckshotWorld

@dataclass
class RegionData:
    connecting_regions: list[str] = field(default_factory=list)

class BuckshotRouletteRegion(Region):
    game = "Buckshot Roulette"

region_table: dict[str, RegionData] = {
    "Menu": RegionData(["Bathroom", "Double or Nothing Bathroom"]),
    "Bathroom": RegionData(["Balcony"]),
    "Double or Nothing Bathroom": RegionData(["Balcony", "Double or Nothing Balcony"]),
    "Balcony": RegionData(["Base Game Table"]),
    "Double or Nothing Balcony": RegionData(["Double or Nothing Table"]),
    "Base Game Table": RegionData([]),
    "Double or Nothing Table": RegionData([])
}