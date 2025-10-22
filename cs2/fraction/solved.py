# https://en.wikipedia.org/wiki/Greatest_common_divisor


def gcd(a, b):
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a


class Fraction:
    def __init__(self, num, den):
        # Challenge: automatically simplify fractions
        divisor = gcd(num, den)
        self.num = num // divisor
        self.den = den // divisor

    def __repr__(self):
        return f"{self.num}/{self.den}"

    def inverse(self):
        # Calculate the inverse of a fraction (1 / self)
        return Fraction(self.den, self.num)

    def __mul__(self, other):
        # Make `self * other` work
        if isinstance(other, int):
            return Fraction(self.num * other, self.den)

        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __add__(self, other):
        # Make `self + other` work
        if isinstance(other, int):
            return Fraction(self.num + other * self.den, self.den)

        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __truediv__(self, other):
        # Make `self / other` work
        if isinstance(other, int):
            return self * Fraction(1, other)

        return self * other.inverse()

    def __sub__(self, other):
        # Make `self - other` work
        return self + (other * -1)

    def __rmul__(self, other):
        # Make `other * self` work
        return self * other

    def __radd__(self, other):
        # Make `other + self` work
        return self + other

    def __rtruediv__(self, other):
        # Make `other / self` work
        return self.inverse() * other

    def __rsub__(self, other):
        # Make `other - self` work
        return -1 * self + other


a = Fraction(5, 20)

print("Test methods:\n")

print("a = ", a)  # 1/4
print("a.inverse() = ", a.inverse())  # 4/1

print("\nTest multiplication:\n")

print("a * Fraction(2, 3) = ", a * Fraction(2, 3))  # 1/6
print("6 * a = ", 6 * a)  # 3/2
print("a * 6 = ", a * 6)  # 3/2

print("\nTest addition:\n")

print("a + Fraction(2, 3) = ", a + Fraction(2, 3))  # 11/12
print("6 + a = ", 6 + a)  # 25/4
print("a + 6 = ", a + 6)  # 25/4

print("\nTest division:\n")

print("a / Fraction(2, 3) = ", a / Fraction(2, 3))  # 3/8
print("6 / a = ", 6 / a)  # 24/1
print("a / 6 = ", a / 6)  # 1/24

print("\nTest subtraction:\n")

print("a - Fraction(2, 3) = ", a - Fraction(2, 3))  # -5/12
print("6 - a = ", 6 - a)  # 23/4
print("a - 6 = ", a - 6)  # -23/4
