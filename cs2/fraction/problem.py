# Challenges:
#
# - Let __mul__ work for numbers and fractions
# - Let __add__ work for numbers and fractions
# - Make __init__ automatically simplify fractions
# - Add __sub__ method
# - Add __div__ method


class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __repr__(self):
        return f"{self.num}/{self.den}"

    # Calculate the value of the fraction as a single number

    def value(self):
        pass

    # Multiple two fractions to make a new fraction

    def __mul__(self, other):
        pass

    # Add two fractions to make a new fraction

    def __add__(self, other):
        pass


a = Fraction(5, 20)

print(a)
print(a.value())
print(a + Fraction(2, 3))
print(a * Fraction(2, 3))
print(a + 6)
print(a * 6)
