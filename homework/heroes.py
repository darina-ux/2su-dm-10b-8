hero1 = {
    "name": "Solmyr",
    "hero_class": "Wizard",
    "town": "Tower",
    "attack": 12,
    "defence": 6,
    "spell_power": 2,
    "knowledge": 3,
    "hp": 100,
    "mp": 30,
    "level": 1,
    "specialty": "Chain Lightning",
    "army": ["Gremlins", "Stone Gargoyles"],
    "best_creature": "Titan",
}

hero2 = {
    "name": "Luna",
    "hero_class": "Elementalist",
    "town": "Conflux",
    "attack": 14,
    "defence": 4,
    "spell_power": 3,
    "knowledge": 3,
    "hp": 90,
    "mp": 30,
    "level": 1,
    "specialty": "Fire Wall",
    "army": ["Pixies", "Air Elementals"],
    "best_creature": "Phoenix",
}


def hit(attacker, defender):
    """One hit: attacker hits defender and reduces their hp."""
    # defence reduces the damage, but every hit deals at least 1
    damage = max(attacker["attack"] - defender["defence"], 1)
    defender["hp"] -= damage
    print(f"{attacker['name']} удря {defender['name']} за {damage} щети. "
          f"{defender['name']} има {max(defender['hp'], 0)} hp.")


def fight(hero_a, hero_b):
    """The heroes take turns hitting each other until one of them falls."""
    round_number = 1
    while hero_a["hp"] > 0 and hero_b["hp"] > 0:
        print(f"--- Round {round_number} ---")
        hit(hero_a, hero_b)
        if hero_b["hp"] <= 0:
            break
        hit(hero_b, hero_a)
        round_number += 1

    winner = hero_a if hero_a["hp"] > 0 else hero_b
    print(f"\Winner: {winner['name']}!")


fight(hero1, hero2)