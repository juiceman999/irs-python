
# Imperative Paradigm
## Le plus ancien et le plus rapide théoriquement car le système execute ligne par ligne

# Procedural Paradigm -- Top 2
## Ranger son code dans différentes procédures / fonctions / subroutines
## Découper son code de manière logique avec des petites procédures qui sont modulaires / modulables et qui chacune va réaliser une seule et unique tache
## Chaque fonciton peut retourner une ou plusieurs valeurs
## Utilisée dans les années 70/80 // Important jusque milieu années 90

# Object Oriented Pradigm -- Top 1
## Démocratisé entre années 80 et 2000
## On ne travaille plus avec des petites fonctions logiques mais des objets
## Avoir des objets qui communiquent entre eux et qui représentent des objets de la vie réelle
## Chaque objet dispose d attributs et méthodes
## Modéliser la vie réelle
## Constructeur : pour rendre privé l'attribut

## 4 piliers de l'orienté objet 
## - Polymorphisme : pouvoir utiliser des méthodes dans plusieurs classes pour un autre objectif
## - Encapsulation : L'encapsulation présente toutes les informations importantes d'un objet à l'intérieur de l'objet et n'expose que les informations choisies au monde extérieur.
## - Abstraction : N implémenter que ce qui est nécessaire
## - Héritage : Utiliser une classe dans une autre classe

##Exemple : Banquier, client, compte, etc

# Functional Paradigm
## Fonction purement mathématiques
## Ne retournent pas de valeur
## Ne doivent pas modifier de valeurs
## Moins utiliser

import os
import sys
import random

player_name = "Haven"

if (player_name == "Haven"):
    pass
else:
    pass

player_score = 150
print(f"Your score is : {player_score}")

# Procedural Paradigm

def character_creation (first_name,
                        last_name: str,
                        random_stats: bool = True,
                        height = 170,
                        age: int = 18) -> str:
    pass

    def random_name () -> int:
        return random.randint(160, 190)

    random_name()

    return f"""Your character has been created\n
                Name: {first_name} {last_name}
    """

def vehicule_creation (name: str = "Volvo") -> str:
    return f"Your vehicule is {name}"

print(character_creation("Jonesy", "Fornite"))

# --------------------------------------------
# Object Oriented Paradigm

class Vehicule:
    # Attributes (Class Attributes & Instance Attributes)
    # Classe Attributes
    vehicule_instances = 0
    OBJECT_TYPE = "Vehicule" # Constant
    brand="Ferrari"

    # Methods (Function class)
    # Constructor (no destructor in Python)
    def __init__ (self, 
                  color_param = "Blue", 
                  type: str ="Car" , 
                  wheels: int = 4):
        self.color = color_param
        self.type = type
        self.wheels = wheels

        self.damage = 0
        self.vehicule_speed = 0

    def __str__ (self):
        """ String representation of the object for users"""
        return f"This vehicule is a {self.type}. The color is {self.color}"""

    def __repr__ (self):
        """ String representation of the object for python developpers """
        return f"The Class Objetc is a vehicule.\n Type variable: {self.type}"""

    def accelerate(self):
        self.vehicule_speed += 50
    
    def get_color(self):
        return self.color

    def set_color(self, value):
        self.color = value

class Character:
    def __init__(self,name,height):
        self._name = name
        self._height = height

    #Getters & Setters

    # Get name
    @property # Decorator
    def name (self):
        return self._name
    
    @property
    def height (self):
        return self._height

    @name.setter
    def name (self, value):
        self._name = value

    @height.setter
    def height (self, value):
        self._height = value

# Cerating a new object
new_character = Character("Haven", 180)
# Setters
new_character.name("Jonesy")
new_character.height(180)
# Getters
print(new_character.name())
print(new_character.height())

# Creating a new object
car = Vehicule("Blue")
truck = Vehicule("Blue")
bus = Vehicule("Blue")

class Water_Animal():
    pass

class Animal:
    def __init__ (self, name):
        self._name = name

    @property
    def name (self):
        return self._name
    
    @name.setter
    def color (self, value):
        self._name = value

class Dolphin (Animal, Water_Animal):
    def __init__(self, color):
        self._color = color
    
    @property
    def color (self):
        return self._color
    
    @color.setter
    def color (self, value):
        self._color = value


new_dolphin = Dolphin("Dolphin", "Gray")
print(new_dolphin.name)
print(new_dolphin.color)

