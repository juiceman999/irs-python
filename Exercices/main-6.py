"""

        Docstring

"""

# Modules -- Python Standard Library
#import os as external_os       ## ALIAS
import os
import sys
import math
import abc
import dataclasses

# Modules -- External Libraries
# Via la commande "pip"
try:
    import pandas
except:
    print("Panda not found")

# Main function (entry-point)
def main():
    pass
    ...
    character_name = "Haven"

    player_name = None

    bool

    high_score = 1500

    player1_score = 300+500
    player2_score = int(450)
    money = float(254.52)
    complex_nb = complex(2+3i)    

    monster = monster.upper()
    npc_one = "Haven" ; npc_two = "Haven"
    
    # Lists
    vehicules = ["car", "boat", "ship", "plane"]
    vehicules = list(("car", "boat", "ship", "plane"))
    characters = ["Jonesy", "Haven", ""]

    vehicules.append("Buses")
    vehicules.
    vehicules.
    print(vehicules)
    vehicules.clear()

    # Set (& Forzensets)
    random_character = {"Peely", "Haven", "Jonesy"}
    random_character.add("New character")
    random_character.remove("Peely")
    print(f"x")

    # Frozenset = set that we cannot change
    frozen_random_character = frozenset((random_character))
    #frozen_random_character = frozenset(({"Peely", "Haven", "Jonesy"}))

    # Tuples ## Tuples plus rapide que les Listes
    object = ("Computer", "Game Console", "Smartphone")
    #print(object[2])
    #object.index

    # Dictionnary
    Glossary = {
        "AAA": None,
        "Game": "Definition",
        "Player": "A user of the game"
    }
    player_stas = {
        "Player Health": 100,
        "Player Shield": 250.25,
        "Player Name": "Jonesy"
    }
    # print(Glossary["Game"])

    # ----------------------------------------------
    # Loops (For, While )
    fruit_list = ["Banana", "Apple", "Orange"]
    for fruit in fruit_list:
        print(fruit)
        if (fruit == "Apple"):
            pass
            # break // POur arrêter le boucle
        else:
            continue

    x = 0
    while x <= 5:
        print(x)
        x += 1
        if ( x == 4 ):
            break
        else:
            continue

# Main Guard
if __name__ == "__main__":
    main()
