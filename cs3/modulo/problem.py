import os
import time


def lastDigit(n):
    # Return the last digit of an integer `n`
    pass


print(lastDigit(-5678) == 8)


def isEven(n):
    # Check whether an integer `n` is even
    pass


print(isEven(-4))
print(not isEven(5))


def isWhole(n):
    # Check whether a number `n` is an integer
    pass


print(isWhole(2))
print(not isWhole(2.5))


def gcd(a, b):
    # Get the greatest common divisor of two integers `a` and `b`
    pass


print(gcd(12, 20) == 4)


def calcDay(today, n):
    # Figure out what day it will be `n` days from now
    #
    # Hint: use the `.index()` method of list

    days = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]

    pass


print(calcDay("monday", 100) == "wednesday")


def showHeight(totalInches):
    # Display a height (given in inches) as feet and inch components
    # (You don't need to use % for the feet, just the inches)
    pass


print(showHeight(66) == "5'06\"")


def factors(n):
    # Get a list of the factors of an integer `n`
    pass


print(factors(40) == [2, 4, 5, 8, 10, 20])


def loading():
    # Display an animated loading bar
    #
    # Note that you can use this code to clear the current line:
    #
    # print("\x1b[1A\x1b[2K", end="")

    pass


loading()


def randomNums():
    # Generate a list of 10 random numbers using the LCG algorithm
    # https://en.wikipedia.org/wiki/Linear_congruential_generator

    seed = 17
    m = 2**32
    a = 1664525
    c = 1013904223

    pass


print(randomNums())
