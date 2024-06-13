""" Object Oriented & Classes """

def main():

    suzuki_car = Car("Suzuki","Red")
    toyota_car = Car("Toyota","Red", 350, 4)

    print(toyota_car)
    print(repr(toyota_car))

    #toyota_car.display_info()

    print(toyota_car.get_wheels)
    #toyota_car._wheels = "test"

    toyota_car.set_wheels(15)
    

class Car:

    VEHICULE_TYPE = "Car"
    vehicule_instances = 0

    # Method - Constructor
    def __init__ (self, 
                  brand: str, 
                  color: str,
                  max_speed: float = 250.0,
                  _wheels: int = 4):

        # Instance Attributes
        self.brand = brand
        self.color = color
        self.max_speed = max_speed
        self._wheels = _wheels

        self.damage = int(0)
        self.vehicule_speed = float(0)

        # Operations
        # vehicule_instances += 1
    
    def __str__ (self):
        return f"This object is a car\n The brand is {self.brand}"

    def __repr__ (self):
        return f" This is a class instance from Car "

    def get_wheels (self):
        return self._wheels
    
    def set_wheels (self, value):
        self._wheels = value

if __name__  == "__main__":
    main()
