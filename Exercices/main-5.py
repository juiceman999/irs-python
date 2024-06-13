from abc import ABC, abstractmethod

class Animal (ABC):
    pass

    @abstractmethod
    def eat(self):
        pass

class Dog(Animal):
    pass

class Dinausore(Animal):
    pass

if __name__ == "__main__":
    new_animal=Animal
