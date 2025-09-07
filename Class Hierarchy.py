# Base class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

        # Base method
        def __drive(self):
            return f"The {self.brand} vehicle is moving."

        # Subclass 1
        class Car(Vehicle):
            def __drive(self):
                return f"The {self.brand} car is driving smoothly on the road."
        # Subclass 2
        class Bike(Vehicle):
            def __drive(self):
                return f"The {self.brand} bike is driving smoothly on the road."