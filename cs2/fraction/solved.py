def gcd(a, b):
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a


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

    # Multiple two functions to make a new fraction
    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    # Add two functions to make a new fraction
    def __add__(self, other):
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)


a = Fraction(5, 20)

print(a)
print(a.value())
print(a * Fraction(2, 3))
print(a + Fraction(2, 3))
