import re


class Height:
    def __init__(self, feet, inches):
        self.totalInches = int(feet * 12 + inches)
        self.feet = abs(self.totalInches) // 12
        self.inches = abs(self.totalInches) % 12

        if self.totalInches < 0:
            self.feet *= -1
            self.inches *= -1

    def __str__(self):
        sign = "-" if self.totalInches < 0 else ""
        return f"{sign}{abs(self.feet)}'{abs(self.inches):02}\""

    def __eq__(self, other):
        return self.totalInches == other.totalInches

    def __le__(self, other):
        return self.totalInches <= other.totalInches

    def __lt__(self, other):
        return self.totalInches < other.totalInches

    def __ge__(self, other):
        return self.totalInches >= other.totalInches

    def __gt__(self, other):
        return self.totalInches > other.totalInches

    def __neg__(self):
        return Height(0, -self.totalInches)

    def __add__(self, other):
        return Height(0, self.totalInches + other.totalInches)

    def __sub__(self, other):
        return Height(0, self.totalInches - other.totalInches)

    def __mul__(self, n):
        return Height(0, self.totalInches * n)

    def __truediv__(self, n):
        return Height(0, self.totalInches / n)


print(Height(5, 10))

print(Height(5, 10) == Height(5, 10))
print(Height(5, 10) <= Height(5, 10))
print(Height(5, 10) < Height(6, 0))
print(Height(5, 10) > Height(4, 11))
print(Height(5, 10) <= Height(5, 10))
print(Height(5, 10) <= Height(6, 0))
print(Height(5, 10) >= Height(4, 11))
print(Height(5, 10) >= Height(5, 10))

print(Height(5, 10) + Height(1, 0))
print(Height(5, 10) + Height(0, 1))
print(Height(5, 10) + Height(0, 4))
print(Height(5, 10) + Height(1, 4))

print(Height(5, 10) - Height(1, 0))
print(Height(5, 10) - Height(0, 1))
print(Height(5, 10) - Height(0, 11))
print(Height(5, 10) - Height(1, 11))

print(Height(5, 10) * 2)
print(Height(5, 10) * 10)

print(Height(5, 10) / 2)
print(Height(5, 10) / 10)

print(-Height(5, 10))
