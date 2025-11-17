import os
import time


def lastDigit(n):
    # Return the last digit of an integer `n`
    return abs(n) % 10


print(lastDigit(-5678) == 8)


def isEven(n):
    # Check whether an integer `n` is even
    return n % 2 == 0


print(isEven(-4))
print(not isEven(5))


def isWhole(n):
    # Check whether a number `n` is an integer
    return n % 1 == 0


print(isWhole(2))
print(not isWhole(2.5))


def gcd(a, b):
    # Get the greatest common divisor of two integers `a` and `b`

    # There are more efficient ways to do this, such as
    # the euclidean algorithm

    result = 1

    for div in range(1, min(a, b)):
        if a % div == 0 and b % div == 0:
            result = div

    return result


print(gcd(12, 20) == 4)


def calcDay(today, n):
    # Figure out what day it will be `n` days from now

    days = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]

    index = days.index(today)
    return days[(index + n) % 7]


print(calcDay("monday", 100) == "wednesday")


def showHeight(totalInches):
    # Display a height (given in inches) as feet and inch components

    inches = totalInches % 12
    feet = totalInches // 12
    return f"{feet}'{inches:02}\""


print(showHeight(66) == "5'06\"")


def factors(n):
    # Get a list of the factors of an integer `n`

    return [f for f in range(2, n) if n % f == 0]


print(factors(40) == [2, 4, 5, 8, 10, 20])


def loading():
    # Display an animated loading bar
    #
    # Note that you can use this code to clear the current line:
    #
    # print("\x1b[1A\x1b[2K", end="")

    for index in range(10):
        print("loading" + "." * (index % 5))
        time.sleep(0.2)
        print("\x1b[1A\x1b[2K", end="")


loading()


def randomNums():
    # Generate a list of 10 random numbers using the LCG algorithm
    # https://en.wikipedia.org/wiki/Linear_congruential_generator

    seed = 17
    m = 2**32
    a = 1664525
    c = 1013904223

    n = seed
    result = []

    for _ in range(10):
        result.append(n / m)
        n = (n * a + c) % m

    return result


print(randomNums())
