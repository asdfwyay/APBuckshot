from dataclasses import dataclass, field
from BaseClasses import Region
from .Enums import *

@dataclass
class RegionData:
    connecting_regions: list[str] = field(default_factory=list)

class BuckshotRouletteRegion(Region):
    game = "Buckshot Roulette"

region_table: dict[str, RegionData] = {
    R_MENU: RegionData([R_BATHROOM, R_DON_BATHROOM]),
    R_BATHROOM: RegionData([R_BALCONY]),
    R_DON_BATHROOM: RegionData([R_BALCONY, R_DON_BALCONY]),
    R_BALCONY: RegionData([R_TABLE]),
    R_DON_BALCONY: RegionData([R_DON_TABLE]),
    R_TABLE: RegionData([]),
    R_DON_TABLE: RegionData([])
}