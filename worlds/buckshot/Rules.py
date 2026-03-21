from typing import Callable
from BaseClasses import CollectionState
from .Enums import *
from .Items import item_table

def consumable_rule(world, count: int, exclude_don=False) -> Callable[[CollectionState], bool]:
    consumables: list[str] = [
        item_name
        for item_name, item_data in item_table.items()
        if item_data.flags & I_CONSUMABLE and (not item_data.flags & I_DOUBLE_OR_NOTHING if exclude_don else True)
    ]
    return lambda state: state.has_from_list(consumables, world.player, count)

def specific_consumables_rule(world, consumables: list[str], count=-1) -> Callable[[CollectionState], bool]:
    if count <= 0:
        return lambda state: state.has_all(consumables, world.player)
    else:
        return lambda state: state.has_from_list(consumables, world.player, count)

def full_house_rule(world) -> Callable[[CollectionState], bool]:
    consumables: list[str] = [
        item_name
        for item_name, item_data in item_table.items()
        if (item_data.flags & I_CONSUMABLE) and item_name != "Adrenaline"
    ]
    return lambda state: state.has("Adrenaline", world.player) and state.has_from_list(consumables, world.player, 7)

def don_access_rule(world, items: list[str], location=None) -> Callable[[CollectionState], bool]:
    if location is None:
        return lambda state: state.has_all(items, world.player)
    else:
        return lambda state: state.has_all(items, world.player) and state.can_reach_location(location, world.player)
    
def streaksanity_rule(world, streak: int, exclude_don=False) -> Callable[[CollectionState], bool]:
    def inner(state):
        don_rule = True if exclude_don else state.can_reach_location("Chasing Losses", world.player)

        score = 3
        if state.has("Handcuffs", world.player):
            score += 2
        if state.has("Magnifying Glass", world.player):
            score += 1
        if state.has("Beer", world.player):
            score += 1
        if state.has("Burner Phone", world.player) and don_rule:
            score += 1
        if state.has("Adrenaline", world.player) and don_rule:
            score += 1
        if state.has("Inverter", world.player) and don_rule:
            score += 1

        return score
    
    max_streak = min(streak, 7) if exclude_don else streak
    return lambda state: (inner(state) >= max_streak) and (state.has("Handcuffs", world.player) if max_streak >= 5 else True)