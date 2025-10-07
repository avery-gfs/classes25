import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


r = Rectangle(3, 4)

print(r.width)
print(r.height)
print(r)
print(r.area())
print(r.perimeter())


class Square:
    def __init__(self, width):
        pass  # Your code goes here

    def __repr__(self):
        pass  # Your code goes here

    def area(self):
        pass  # Your code goes here

    def perimeter(self):
        pass  # Your code goes here


s = Square(10)

print(s.width)
print(s)
print(s.area())
print(s.perimeter())


class Circle:
    def __init__(self, radius):
        pass  # Your code goes here

    def __repr__(self):
        pass  # Your code goes here

    def area(self):
        pass  # Your code goes here

    def perimeter(self):
        pass  # Your code goes here


c = Circle(10)

print(c.radius)
print(c)
print(c.area())
print(c.perimeter())


class Point:
    def __init__(self, x, y):
        pass  # Your code goes here

    def __repr__(self):
        pass  # Your code goes here

    def distance_to(self, other):
        # Use self.x, self.y, other.x, and other.y to calculate
        # the distance between two points

        pass  # Your code goes here


p = Point(1, 2)

print(p.x)
print(p.y)

origin = Point(0, 0)
print(p.distance_to(origin))


class Line:
    def __init__(self, p1, p2):
        pass  # Your code goes here

    def __repr__(self):
        pass  # Your code goes here

    def length(self):
        # Use the distance_to method on one of your point objects
        # to implement length

        pass  # Your code goes here

    def slope(self):
        pass  # Your code goes here


l = Line(Point(0, 0), Point(3, 4))

print(l)
print(l.p1)
print(l.p2)
print(l.length())
print(l.slope())
