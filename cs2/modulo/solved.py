import os
import time


def lastDigit(n):
    return abs(n) % 10


print(lastDigit(-5678) == 8)


def isEven(n):
    return n % 2 == 0


print(isEven(-4))
print(not isEven(5))


def isWhole(n):
    return n % 1 == 0


print(isWhole(2))
print(not isWhole(2.5))


def gcd(a, b):
    # There are more efficient ways to do this, such as
    # the euclidean algorithm

    result = 1

    for div in range(1, min(a, b)):
        if a % div == 0 and b % div == 0:
            result = div

    return result


print(gcd(12, 20) == 4)


def calcDay(current, offset):
    days = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]
    index = days.index(current)
    return days[(index + offset) % 7]


print(calcDay("monday", 100) == "wednesday")


def showHeight(totalInches):
    inches = totalInches % 12
    feet = totalInches // 12
    return f"{feet}'{inches:02}\""


print(showHeight(66) == "5'06\"")


def factors(n):
    return [f for f in range(2, n) if n % f == 0]


print(factors(40) == [2, 4, 5, 8, 10, 20])


def loading():
    for index in range(10):
        print("loading" + "." * (index % 5))
        time.sleep(0.2)
        print("\x1b[1A\x1b[2K", end="")


loading()

# random number gen

# ring buffer
