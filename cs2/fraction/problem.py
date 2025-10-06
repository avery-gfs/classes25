# Challenge: make __init__ automatically simplify fractions


class Fraction:
    def __init__(self, num, den):
        pass

    def __repr__(self):
        pass

    # Calculate the value of the fraction as a single number

    def value(self):
        pass

    def __mul__(self, other):
        pass

    def __div__(self, other):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass


a = Fraction(5, 20)

print(a)  # 1/4
print(a.value())  # 0.25
print(a + Fraction(2, 3))  # 11/12
print(a * Fraction(2, 3))  # 1/6
print(a + 6)  # 25/4
print(a * 6)  # 3/2
