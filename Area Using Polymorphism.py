# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclass: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        def area(self):
            return math.pi * (self.radius ** 2)

# Subclass: Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        def area(self):
            return self.width * self.height

# Function that uses polymorphism
def total_area(shape):
    return sum(shape.area() for shape in shapes)