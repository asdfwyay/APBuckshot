from dataclasses import dataclass
from BaseClasses import Item, ItemClassification

class BuckshotRouletteItem(Item):
    game = "Buckshot Roulette"

    def __init__(self, name, player, id, classification, force_not_advancement):
        if force_not_advancement:
            classification = ItemClassification.useful
        super(BuckshotRouletteItem, self).__init__(name, classification, id, player)

@dataclass
class ItemData:
    id: int
    classification: ItemClassification

item_table: dict[str, ItemData] = {
    "Double or Nothing Pills":  ItemData(1, ItemClassification.progression),
    "Expired Medicine":         ItemData(2, ItemClassification.progression),
    "Inverter":                 ItemData(3, ItemClassification.progression),
    "Cigarette Pack":           ItemData(4, ItemClassification.progression),
    "Burner Phone":             ItemData(5, ItemClassification.progression),
    "Adrenaline":               ItemData(6, ItemClassification.progression),
    "Magnifying Glass":         ItemData(7, ItemClassification.progression),
    "Beer":                     ItemData(8, ItemClassification.progression),
    "Hand Saw":                 ItemData(9, ItemClassification.progression),
    "Handcuffs":                ItemData(10, ItemClassification.progression)
}