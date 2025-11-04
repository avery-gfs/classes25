# Refactor the code for these functions to make it better
# You'll find **lots** of room for improvement

import math


def clamp(num, low, high):
    if num < low:
        return low

    elif num > high:
        return high

    elif num >= low and num <= high:
        return num


print(clamp(-7, 0, 10))
print(clamp(7, 0, 10))
print(clamp(17, 0, 10))

# ---------------------------------------------------------


def priceTag(a, b):
    return "A " + a + " costs $" + str(b)


print(priceTag("banana", 10))

# ---------------------------------------------------------


def sign(num):
    if (num > 0) == True:
        return "positive"

    elif num is 0:
        return "zero"

    elif (num < 0) == True:
        return "negative"


print(sign(8))
print(sign(0))
print(sign(-7))

# ---------------------------------------------------------


def isEven(num):
    half = num / 2

    if half == round(half):
        return True

    return False


print(isEven(7))
print(isEven(8))

# ---------------------------------------------------------


def sum(numbers):
    sum = 0

    for index in range(len(numbers)):
        sum = sum + numbers[index]

    return sum


print(sum([1, 2, 3, 4, 5]))
print(sum([]))

# ---------------------------------------------------------


def countEvens(numbers):
    count = 0

    for n in numbers:
        half = n / 2

        if half == round(half):
            count = count + 1

    return count


print(countEvens([1, 4, 2, 7, 3, 1]))

# ---------------------------------------------------------


def shout(words):
    result = ""
    index = 0

    while index < len(words):
        result += words[index].upper()
        result += "!"
        index = index + 1
        if index < len(words):
            result += " "

    return result


print(shout(["germantown", "friends", "school"]))

# ---------------------------------------------------------


def hexToDec(hexStr):
    digitVals = []

    for d in hexStr:
        if d == "0":
            digitVals.append(0)
        if d == "1":
            digitVals.append(1)
        if d == "2":
            digitVals.append(2)
        if d == "3":
            digitVals.append(3)
        if d == "4":
            digitVals.append(4)
        if d == "5":
            digitVals.append(5)
        if d == "6":
            digitVals.append(6)
        if d == "7":
            digitVals.append(7)
        if d == "8":
            digitVals.append(8)
        if d == "9":
            digitVals.append(9)
        if d == "a":
            digitVals.append(10)
        if d == "b":
            digitVals.append(11)
        if d == "c":
            digitVals.append(12)
        if d == "d":
            digitVals.append(13)
        if d == "e":
            digitVals.append(14)
        if d == "f":
            digitVals.append(15)

    result = 0

    for value in digitVals:
        result *= 16
        result += value

    return result


print(hexToDec("1a"))  # Should print 26

# ---------------------------------------------------------


def rpsWinner(player, ai):
    if player == "rock":
        if ai == "rock":
            return "tie"
        if ai == "paper":
            return "ai"
        if ai == "scissors":
            return "player"
    if player == "paper":
        if ai == "rock":
            return "player"
        if ai == "paper":
            return "tie"
        if ai == "scissors":
            return "player"
    if player == "scissors":
        if ai == "rock":
            return "ai"
        if ai == "paper":
            return "player"
        if ai == "scissors":
            return "tie"


print(rpsWinner("rock", "paper"))
print(rpsWinner("scissors", "paper"))
print(rpsWinner("paper", "paper"))

# ---------------------------------------------------------


def primeFactors(num):
    results = []
    div = 2

    while div < num:
        if num % div != 0:
            div = div + 1
        else:
            results.append(div)
            num /= div

    results.append(num)
    return results


print(primeFactors(60))
print(primeFactors(100000001))
