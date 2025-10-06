# https://en.wikipedia.org/wiki/Greatest_common_divisor


def gcd(a, b):
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a


# Challenges:
#
# - Let __mul__ work for numbers and fractions
# - Let __add__ work for numbers and fractions
# - Make __init__ automatically simplify fractions
# - Add __sub__ method
# - Add __div__ method


class Fraction:
    def __init__(self, num, den):
        divisor = gcd(num, den)
        self.num = num // divisor
        self.den = den // divisor

    def __repr__(self):
        return f"{self.num}/{self.den}"

    # Calculate the value of the fraction as a single number

    def value(self):
        return self.num / self.den

    # Multiple two fractions to make a new fraction

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Fraction(self.num * other, self.den)

        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    # Add two fractions to make a new fraction

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Fraction(self.num + other * self.den, self.den)

        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)


a = Fraction(5, 20)

print(a)
print(a.value())
print(a + Fraction(2, 3))
print(a * Fraction(2, 3))
print(a + 6)
print(a * 6)
