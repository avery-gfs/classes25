class Height:
    def __init__(self, feet, inches):
        self.totalInches = max(int(feet * 12 + inches), 0)

    def __str__(self):
        feet = self.totalInches // 12
        inches = self.totalInches % 12

        return f"{feet}'{inches:02}\""

    def __eq__(self, other):
        return self.totalInches == other.totalInches

    def __lt__(self, other):
        return self.totalInches < other.totalInches

    def __gt__(self, other):
        return self.totalInches > other.totalInches

    def __le__(self, other):
        return self.totalInches <= other.totalInches

    def __ge__(self, other):
        return self.totalInches >= other.totalInches

    def __add__(self, other):
        return Height(0, self.totalInches + other.totalInches)

    def __sub__(self, other):
        return Height(0, self.totalInches - other.totalInches)

    def __mul__(self, n):
        return Height(0, self.totalInches * n)

    def __truediv__(self, n):
        return Height(0, self.totalInches / n)

    @staticmethod
    def fromStr(heightStr):
        feet = int(heightStr[:-4])
        inches = int(heightStr[-3:-1])
        return Height(feet, inches)


h = Height(5, 10)

print(h)

print(h == Height(5, 10))
print(h <= Height(5, 10))
print(h < Height(6, 0))
print(h > Height(4, 11))
print(h <= Height(5, 19))
print(h <= Height(6, 0))
print(h >= Height(4, 11))
print(h >= Height(5, 10))

print(h + Height(1, 0))
print(h + Height(0, 1))
print(h + Height(0, 4))
print(h + Height(1, 4))

print(h - Height(1, 0))
print(h - Height(0, 1))
print(h - Height(0, 11))
print(h - Height(1, 11))

print(h * 2)
print(h * 10)

print(h / 2)
print(h / 10)

print(Height.fromStr("5'06\"") == Height(5, 6))
