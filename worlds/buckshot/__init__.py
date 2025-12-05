from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World

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