##Panda3D

class Vehicules:

    VEHICULE_TYPE = "Véhicule"

    def __init__(self, wheels, color) -> None:
        self.wheels = wheels
        self.color = color
        pass
    
    def move_forward():
        return f"Vehicule is moving forward"

class Car (Vehicules):
    pass

class Truck (Vehicules):
    pass

if __name__ == "__main__":
    new_car = Car()
    new_car.move_forward()
