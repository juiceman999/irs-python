""" Object Oriented & Classes """

#Paradigme impératif 
#Procédural 
#Orienté objet

# Une méthode n'est ni plus ni moins qu'une fonction à l'intérieure d'un classe
# Il faut créer une instance de classe 
# DIfférence entre classe et objet
#   > Un objet est un résultat sorti d'une classe
#   > Exemple : Une classe pour définir les attributs d'un chien
#               Si l'on utilise cette classe pour 3 chiens alors nous aurons 3 objets

# Attributs de classe vs attributs d'instance

class Dog:

    # Attributes / Properties
    # Class Attributes (same fo every object) > Généralement des constantes et on définit les constantes en majuscule
    ANIMAL_TYPE  = "Dog"
    dog_count = 0

    # Methods (class functions)

    def __init__ (self, race_param, color_param):
        """ Constructor Method """
        
        # Instance attributes
        race_param = self.race
        color_param = self.color
        height = 140
        #color ="Brown"
        #race = "Pitbull"

def display_info (self):
    print(f"Dog race = : {self.race}")

if __name__ == "__main__":
    dog_01 = Dog(race_param="Pitbull", color_param="Brown")
    dog_02 = Dog(race_param="Chiwawa", color_param="Grey")
    dog_03 = Dog(race_param="Caniche", color_param="White")

    dog_01.display_info()
