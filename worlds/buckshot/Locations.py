from dataclasses import dataclass
from enum import IntEnum
from BaseClasses import Location

class BuckshotRouletteLocation(Location):
    game = "Buckshot Roulette"

class LocationType(IntEnum):
    BASE_GAME = 0
    ACHIEVEMENT = 1
    DOUBLE_OR_NOTHING = 2
    SHOTSANITY = 3
    MULTIPLAYER = 4 # UNUSED

@dataclass
class LocationData:
    id: int
    location_type: LocationType

location_table: dict[str, LocationData] = {
    "Win Round 1":              LocationData(1, LocationType.BASE_GAME),
    "Win Round 2":              LocationData(2, LocationType.BASE_GAME),
    "Win Round 3":              LocationData(3, LocationType.BASE_GAME),

    "70K":                      LocationData(4, LocationType.ACHIEVEMENT),
    "Coin Flip":                LocationData(5, LocationType.ACHIEVEMENT),
    "Chasing Losses":           LocationData(6, LocationType.ACHIEVEMENT),
    "Bronze Gates":             LocationData(7, LocationType.ACHIEVEMENT),
    "High Rollers":             LocationData(8, LocationType.ACHIEVEMENT),
    "Name Taken":               LocationData(9, LocationType.ACHIEVEMENT),
    "Nope!":                    LocationData(10, LocationType.ACHIEVEMENT),
    "140K":                     LocationData(11, LocationType.ACHIEVEMENT),
    "Overdose":                 LocationData(12, LocationType.ACHIEVEMENT),
    "Soak It In":               LocationData(13, LocationType.ACHIEVEMENT),
    "Digita, Orava and Koni":   LocationData(14, LocationType.ACHIEVEMENT),
    "Why?":                     LocationData(15, LocationType.ACHIEVEMENT),
    "Going Out With Style!":    LocationData(16, LocationType.ACHIEVEMENT),
    "1000K":                    LocationData(17, LocationType.ACHIEVEMENT),
    "Know When To Quit":        LocationData(18, LocationType.ACHIEVEMENT),
    "Full House":               LocationData(19, LocationType.ACHIEVEMENT)
}
