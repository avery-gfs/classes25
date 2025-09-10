import math

class Circle:
    # __init__ defines how a new Circle is created
    def __init__(self, radius):
        self.radius = radius # store radius as a field on the new Circle object

    # __repr__ defines how the Circle is displayed
    def __repr__(self):
        return f"Circle({self.radius})"

    # Caculate the area of the Circle
    def area(self):
        return math.pi * self.radius ** 2

    # Caculate the perimeter of the Circle
    def perimeter(self):
        return 2 * math.pi * self.radius

    # Get a new Circle that is a scaled version of the original
    def scale(self, factor):
        return Circle(self.radius * factor)

circle = Circle(1)

print(circle)
print(circle.radius)
print(circle.area())
print(circle.perimeter())

circle2 = circle.scale(3)

print(circle2)
print(circle2.radius)
print(circle2.area())
print(circle2.perimeter())

