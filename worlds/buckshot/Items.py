from dataclasses import dataclass
from BaseClasses import Item, ItemClassification as IC

# Item Flags
CONSUMABLE = 0x01
DOUBLE_OR_NOTHING = 0x02

class BuckshotRouletteItem(Item):
    game = "Buckshot Roulette"

    def __init__(self, name, player, id, classification, force_not_advancement):
        if force_not_advancement:
            classification = IC.useful
        super(BuckshotRouletteItem, self).__init__(name, classification, id, player)

@dataclass
class ItemData:
    id: int
    classification: IC
    flags: int = 0x00

item_table: dict[str, ItemData] = {
    "Double or Nothing Pills":  ItemData(1,  IC.progression, DOUBLE_OR_NOTHING),
    "Cigarette Pack":           ItemData(2,  IC.progression, CONSUMABLE),
    "Magnifying Glass":         ItemData(3,  IC.progression, CONSUMABLE),
    "Beer":                     ItemData(4,  IC.progression, CONSUMABLE),
    "Hand Saw":                 ItemData(5,  IC.progression, CONSUMABLE),
    "Handcuffs":                ItemData(6,  IC.progression, CONSUMABLE),
    "Expired Medicine":         ItemData(7,  IC.progression, CONSUMABLE | DOUBLE_OR_NOTHING),
    "Inverter":                 ItemData(8,  IC.progression, CONSUMABLE | DOUBLE_OR_NOTHING),
    "Burner Phone":             ItemData(9,  IC.progression, CONSUMABLE | DOUBLE_OR_NOTHING),
    "Adrenaline":               ItemData(10, IC.progression, CONSUMABLE | DOUBLE_OR_NOTHING),

    "Empty Shell":              ItemData(11, IC.filler),
    "Empty Cigarette Box":      ItemData(12, IC.filler),
    "Broken Magnifying Glass":  ItemData(13, IC.filler),
    "Crushed Beer Can":         ItemData(14, IC.filler),
    "Sawed-Off Shotgun Barrel": ItemData(15, IC.filler),
    "Broken Handcuffs":         ItemData(16, IC.filler),
    "Empty Pill Packet":        ItemData(17, IC.filler),
    "Double Inverter":          ItemData(18, IC.filler),
    "Snapped Burner Phone":     ItemData(19, IC.filler),
    "Empty Adrenaline Vial":    ItemData(20, IC.filler),
}