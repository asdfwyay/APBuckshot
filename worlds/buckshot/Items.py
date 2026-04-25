from dataclasses import dataclass
from BaseClasses import Item, ItemClassification as IC
from .Enums import *

class BuckshotRouletteItem(Item):
    game = "Buckshot Roulette"

@dataclass
class ItemData:
    id: int
    classification: IC
    flags: int = 0x00

item_table: dict[str, ItemData] = {
    "Double or Nothing Pills":          ItemData(0x0000 + 1,  IC.progression, I_DOUBLE_OR_NOTHING | I_PILLS),
    "Hand Saw":                         ItemData(0x0000 + 2,  IC.progression, I_CONSUMABLE),
    "Magnifying Glass":                 ItemData(0x0000 + 3,  IC.progression, I_CONSUMABLE),
    "Beer":                             ItemData(0x0000 + 4,  IC.progression, I_CONSUMABLE),
    "Cigarette Pack":                   ItemData(0x0000 + 5,  IC.progression, I_CONSUMABLE),
    "Handcuffs":                        ItemData(0x0000 + 6,  IC.progression, I_CONSUMABLE),
    "Expired Medicine":                 ItemData(0x0000 + 7,  IC.progression, I_CONSUMABLE | I_DOUBLE_OR_NOTHING),
    "Burner Phone":                     ItemData(0x0000 + 8,  IC.progression, I_CONSUMABLE | I_DOUBLE_OR_NOTHING),
    "Adrenaline":                       ItemData(0x0000 + 9,  IC.progression, I_CONSUMABLE | I_DOUBLE_OR_NOTHING),
    "Inverter":                         ItemData(0x0000 + 10, IC.progression, I_CONSUMABLE | I_DOUBLE_OR_NOTHING),

    "Progressive Item Luck":            ItemData(0x0100 + 1,  IC.useful,      I_SPECIAL),
    "Life Bank Charge":                 ItemData(0x0100 + 2,  IC.useful,      I_SPECIAL),

    "Item Buff - Hand Saw":             ItemData(0x0100 + 3,  IC.useful,      I_SPECIAL),
    "Item Buff - Magnifying Glass":     ItemData(0x0100 + 4,  IC.useful,      I_SPECIAL),
    "Item Buff - Beer":                 ItemData(0x0100 + 5,  IC.useful,      I_SPECIAL),
    "Item Buff - Cigarette Pack":       ItemData(0x0100 + 6,  IC.useful,      I_SPECIAL),
    "Item Buff - Handcuffs":            ItemData(0x0100 + 7,  IC.useful,      I_SPECIAL),
    "Item Buff - Expired Medicine":     ItemData(0x0100 + 8,  IC.useful,      I_SPECIAL),
    "Item Buff - Burner Phone":         ItemData(0x0100 + 9,  IC.useful,      I_SPECIAL),
    "Item Buff - Adrenaline":           ItemData(0x0100 + 10, IC.useful,      I_SPECIAL),
    "Item Buff - Inverter":             ItemData(0x0100 + 11, IC.useful,      I_SPECIAL),

    "Clear Debuff - Hand Saw":          ItemData(0x0100 + 12, IC.useful,      I_SPECIAL),
    "Clear Debuff - Magnifying Glass":  ItemData(0x0100 + 13, IC.useful,      I_SPECIAL),
    "Clear Debuff - Beer":              ItemData(0x0100 + 14, IC.useful,      I_SPECIAL),
    "Clear Debuff - Cigarette Pack":    ItemData(0x0100 + 15, IC.useful,      I_SPECIAL),
    "Clear Debuff - Handcuffs":         ItemData(0x0100 + 16, IC.useful,      I_SPECIAL),
    "Clear Debuff - Expired Medicine":  ItemData(0x0100 + 17, IC.useful,      I_SPECIAL),
    "Clear Debuff - Burner Phone":      ItemData(0x0100 + 18, IC.useful,      I_SPECIAL),
    "Clear Debuff - Adrenaline":        ItemData(0x0100 + 19, IC.useful,      I_SPECIAL),
    "Clear Debuff - Inverter":          ItemData(0x0100 + 20, IC.useful,      I_SPECIAL),

    "Stolen Package Trap":              ItemData(0x0400 + 1,  IC.trap),
    "Schrodinger's Bullet Trap":        ItemData(0x0400 + 2,  IC.trap),

    "Empty Shell":                      ItemData(0x0700 + 1,  IC.filler),
    "Empty Cigarette Box":              ItemData(0x0700 + 2,  IC.filler),
    "Broken Magnifying Glass":          ItemData(0x0700 + 3,  IC.filler),
    "Crushed Beer Can":                 ItemData(0x0700 + 4,  IC.filler),
    "Sawed-Off Shotgun Barrel":         ItemData(0x0700 + 5,  IC.filler),
    "Broken Handcuffs":                 ItemData(0x0700 + 6,  IC.filler),
    "Empty Pill Packet":                ItemData(0x0700 + 7,  IC.filler),
    "Double Inverter":                  ItemData(0x0700 + 8,  IC.filler),
    "Snapped Burner Phone":             ItemData(0x0700 + 9,  IC.filler),
    "Empty Adrenaline Vial":            ItemData(0x0700 + 10, IC.filler),

    "Tiny Point Increase":              ItemData(0x0800 + 1,  IC.filler), # 0.25 %
    "Small Point Increase":             ItemData(0x0800 + 2,  IC.filler), # 0.5 %
    "Medium Point Increase":            ItemData(0x0800 + 3,  IC.filler), # 1 %
    "Large Point Increase":             ItemData(0x0800 + 4,  IC.filler), # 2 %
    "Huge Point Increase":              ItemData(0x0800 + 5,  IC.filler), # 5 %

    "Base Game Beaten":                 ItemData(0x0F00 + 1,  IC.progression, I_EVENT),
    "WINNER":                           ItemData(0x0F00 + 2,  IC.progression, I_EVENT),
}

item_id_table = {name: data.id for name, data in item_table.items()}
item_name_table = {data.id: name for name, data in item_table.items()}