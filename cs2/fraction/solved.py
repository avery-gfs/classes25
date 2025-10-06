# https://en.wikipedia.org/wiki/Greatest_common_divisor


def gcd(a, b):
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a


# Challenge: make __init__ automatically simplify fractions


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

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Fraction(self.num * other, self.den)

        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Fraction(self.num + other * self.den, self.den)

        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)


a = Fraction(5, 20)

print(a)  # 1/4
print(a.value())  # 0.25
print(a + Fraction(2, 3))  # 11/12
print(a * Fraction(2, 3))  # 1/6
print(a + 6)  # 25/4
print(a * 6)  # 3/2
