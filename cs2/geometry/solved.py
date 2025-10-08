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
        self.width = width

    def __repr__(self):
        return f"Square({self.width})"

    def area(self):
        return self.width**2

    def perimeter(self):
        return 4 * self.width


s = Square(10)

print(s.width)
print(s)
print(s.area())
print(s.perimeter())


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.radius})"

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


c = Circle(10)

print(c.radius)
print(c)
print(c.area())
print(c.perimeter())


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)


p = Point(1, 2)

print(p.x)
print(p.y)

origin = Point(0, 0)
print(p.distance_to(origin))


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"Line({self.p1}, {self.p2})"

    def length(self):
        return self.p1.distance_to(self.p2)

    def slope(self):
        dx = self.p1.x - self.p2.x
        dy = self.p1.y - self.p2.y
        return dy / dx


l = Line(Point(0, 0), Point(3, 4))

print(l)
print(l.p1)
print(l.p2)
print(l.length())
print(l.slope())
