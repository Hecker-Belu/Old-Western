import random

# Original text_list
text_list = [
    "You find a horse",
    "You come across a traveler",
    "You find some food scraps",
    "You found some metal scraps",
    "You found a strange text",
    "You encountered an enemy",
    "You found nothing",
    "You found a town",
    "You found some armor",
    "You found a cursed old boot",
    "You found gold",
]

# Function to generate random stats
def generate_random_stats():
    return {
        "Health": random.randint(-20, 20),
        "Gold": random.randint(-20, 20),
        "Reputation": random.randint(-20, 20)
    }

# Updated choices_for_text with random stats
choices_for_text = {
    "You find a horse": {
        1: {"response": "You ride the horse and continue your journey.", "stats": generate_random_stats()},
        2: {"response": "You pass the horse and continue on foot.", "stats": generate_random_stats()}
    },
    "You come across a traveler": {
        1: {"response": "You ask the traveler for information.", "stats": generate_random_stats()},
        2: {"response": "You ignore the traveler and move on.", "stats": generate_random_stats()}
    },
    "You find some food scraps": {
        1: {"response": "You eat the food scraps.", "stats": generate_random_stats()},
        2: {"response": "You leave the food scraps.", "stats": generate_random_stats()}
    },
    "You found some metal scraps": {
        1: {"response": "You collect the metal scraps.", "stats": generate_random_stats()},
        2: {"response": "You ignore the metal scraps.", "stats": generate_random_stats()}
    },
    "You found a strange text": {
        1: {"response": "You read the strange text.", "stats": generate_random_stats()},
        2: {"response": "You disregard the strange text.", "stats": generate_random_stats()}
    },
    "You encountered an enemy": {
        1: {"response": "You prepare to fight the enemy.", "stats": generate_random_stats()},
        2: {"response": "You try to escape from the enemy.", "stats": generate_random_stats()}
    },
    "You found nothing": {
        1: {"response": "You search the area thoroughly.", "stats": generate_random_stats()},
        2: {"response": "You leave the area.", "stats": generate_random_stats()}
    },
    "You found a town": {
        1: {"response": "You enter the town and explore.", "stats": generate_random_stats()},
        2: {"response": "You avoid the town and continue.", "stats": generate_random_stats()}
    },
    "You found some armor": {
        1: {"response": "You equip the armor.", "stats": generate_random_stats()},
        2: {"response": "You leave the armor behind.", "stats": generate_random_stats()}
    },
    "You found a cursed old boot": {
        1: {"response": "You inspect the cursed boot.", "stats": generate_random_stats()},
        2: {"response": "You discard the cursed boot.", "stats": generate_random_stats()}
    },
    "You found gold": {
        1: {"response": "You take the gold.", "stats": generate_random_stats()},
        2: {"response": "You leave the gold behind.", "stats": generate_random_stats()}
    }
}
