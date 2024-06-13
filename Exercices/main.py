""" Docstring

@author: Romain Hénon-Hilaire
@description: Character Name Generator

"""

# Import Modules
import random

# Sub-function Random list Element
def random_list_element (user_list: list) -> str:
    user_list_length = len(user_list) -1
    
    random_list_element = random.radint(0, user_list_length)

    #print(user_list[random_list_element])
    return str(user_list[random_list_element])

# Main function
def main(debug_mode: bool = False):
    """ Application entry point """
    pass

    # Variable example
    character_name = "Jonesy"

    # ------------------------------------------------------
    # Collection de données
    vehicule = ["Car", "Boat", "Truck", "Motorbike", "Ship"]
    character_skins = {"Jonesy", "Peely", "Haven"}

    # Debug condition
    if (debug_mode):
        print(" DEBUG MODE ")
    else:
        pass

    print(f"Random list element: {random_list_element(vehicule)}")

# Main Guard

if __name__ == "__main__":
    main()