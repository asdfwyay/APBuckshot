from BaseClasses import Location

class BuckshotRouletteLocation(Location):
    game = "Buckshot Roulette"

base_game_locations: dict[str, int] = {
    "Win Round 1": 1,
    "Win Round 2": 2,
    "Win Round 3": 3
}

achievement_locations: dict[str, int] = {
    "70K": 4,
    "Coin Flip": 5,
    "Chasing Losses": 6,
    "Bronze Gates": 7,
    "High Rollers": 8,
    "Name Taken": 9,
    "Nope!": 10,
    "140K": 11,
    "Overdose": 12,
    "Soak It In": 13,
    "Digita, Orava and Koni": 14,
    "Why?": 15,
    "Going Out With Style!": 16,
    "1000K": 17,
    "Full House": 18,
    "Know When To Quit": 19
}

