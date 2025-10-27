class Fraction:
    def __init__(self, num, den):
        # Challenge: automatically simplify fractions
        self.num = num
        self.den = den

    def __repr__(self):
        return f"{self.num}/{self.den}"

    def inverse(self):
        # Calculate the inverse of a fraction (1 / self)
        pass

    def __mul__(self, other):
        # Make `self * other` work
        if isinstance(other, int):
            return Fraction(self.num * other, self.den)

        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __truediv__(self, other):
        # Make `self / other` work
        pass

    def __add__(self, other):
        # Make `self + other` work
        pass

    def __sub__(self, other):
        # Make `self - other` work
        pass

    def __rmul__(self, other):
        # Make `other * self` work
        pass

    def __radd__(self, other):
        # Make `other + self` work
        pass

    def __rtruediv__(self, other):
        # Make `other / self` work
        pass

    def __rsub__(self, other):
        # Make `other - self` work
        pass


a = Fraction(5, 20)

print("Test methods:\n")

print("a = ", a)  # 1/4
print("a.inverse() = ", a.inverse())  # 4/1

print("\nTest multiplication:\n")

print("a * Fraction(2, 3) = ", a * Fraction(2, 3))  # 1/6
print("a * 6 = ", a * 6)  # 3/2

print("\nTest division:\n")

print("a / Fraction(2, 3) = ", a / Fraction(2, 3))  # 3/8
print("a / 6 = ", a / 6)  # 1/24

print("\nTest addition:\n")

print("a + Fraction(2, 3) = ", a + Fraction(2, 3))  # 11/12
print("a + 6 = ", a + 6)  # 25/4

print("\nTest subtraction:\n")

print("a - Fraction(2, 3) = ", a - Fraction(2, 3))  # -5/12
print("a - 6 = ", a - 6)  # -23/4

print("\nTest r-methods:\n")

print("6 * a = ", 6 * a)  # 3/2
print("6 / a = ", 6 / a)  # 24/1
print("6 + a = ", 6 + a)  # 25/4
print("6 - a = ", 6 - a)  # 23/4
