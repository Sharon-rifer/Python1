# Base class
class Shape:
    def __init__(self, name="Shape"):
        self.name = name
        print(f"Initializing a {self.name} Shape")

    def calculate_area(self):
        print("base shape has no area calculation.")

# Derived class
class Rectangle(Shape):
    def __init__ (self, width, height):
# Call the parent constructor super().__init__(name="Rectangle")
             self.width = width
             self.height = height

     def calculate_area(self):
         # Call the base class method (even though it does nothing useful)
         super().calculate_area()

         # Rectangle's own logic
         return self.width * self.height



