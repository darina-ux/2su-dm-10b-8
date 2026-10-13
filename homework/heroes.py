hero1 = {
    "name": "Solmyr",
    "hero_class": "Wizard",
    "town": "Tower",
    "attack": 0,
    "defence": 0,
    "spell_power": 2,
    "knowledge": 3,
    "hp": 100,
    "mp": 30,
    "level": 1,
    "specialty": "Chain Lightning",
    "army": ["Gremlins", "Stone Gargoyles"],
    "best_creature": "Titan"
}

hero2 = {
    "name": "Luna",
    "hero_class": "Elementalist",
    "town": "Conflux",
    "attack": 0,
    "defence": 0,
    "spell_power": 3,
    "knowledge": 3,
    "hp": 100,
    "mp": 30,
    "level": 1,
    "specialty": "Fire Wall",
    "army": ["Pixies", "Air Elementals"],
    "best_creature": "Phoenix"
}

for hero in (hero1, hero2):
    print(f"--- {hero['name']} ---")
    for key, value in hero.items():
        print(f"{key}: {value}")
    print()


