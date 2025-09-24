import math


class Rectangle:
    pass


rect = Rectangle(3, 4)

print(rect)
print(rect.radius)
print(rect.area())
print(rect.perimeter())

rect2 = rect.scale(2)

print(rect2)
print(rect2.radius)
print(rect2.area())
print(rect2.perimeter())
