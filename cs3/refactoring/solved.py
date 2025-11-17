import math


def clamp(num, low, high):
    return max(low, min(high, num))


print(clamp(-7, 0, 10))
print(clamp(7, 0, 10))
print(clamp(17, 0, 10))

# ---------------------------------------------------------


def priceTag(item, price):
    return f"A {item} costs ${price}"


print(priceTag("banana", 10))

# ---------------------------------------------------------


def sign(num):
    if num > 0:
        return "positive"

    if num == 0:
        return "zero"

    return "negative"


print(sign(8))
print(sign(0))
print(sign(-7))

# ---------------------------------------------------------


def isEven(num):
    return num % 2 == 0


print(isEven(7))
print(isEven(8))

# ---------------------------------------------------------


def sum(numbers):
    total = 0

    for n in numbers:
        total += n

    return total


print(sum([1, 2, 3, 4, 5]))
print(sum([]))

# ---------------------------------------------------------

hexValues = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15,
}


def hexToDec(hexStr):
    result = 0

    for d in hexStr:
        result = result * 16 + hexValues[d]

    return result


print(hexToDec("1a"))

# ---------------------------------------------------------

rpsResults = {
    # Pairs are in (player, ai) format
    ("rock", "rock"): "tie",
    ("rock", "paper"): "ai",
    ("rock", "scissors"): "player",
    ("paper", "rock"): "player",
    ("paper", "paper"): "tie",
    ("paper", "scissors"): "player",
    ("scissors", "rock"): "ai",
    ("scissors", "paper"): "player",
    ("scissors", "scissors"): "tie",
}


def rpsWinner(player, ai):
    return rpsResults[(player, ai)]


print(rpsWinner("rock", "paper"))
print(rpsWinner("scissors", "paper"))
print(rpsWinner("paper", "paper"))

# ---------------------------------------------------------


def primeFactors(num):
    results = []
    div = 2

    while div < math.sqrt(num):
        if num % div:
            div += 1
        else:
            results.append(div)
            num //= div

    results.append(num)
    return results


print(primeFactors(60))
print(primeFactors(100000001))

# ---------------------------------------------------------


def countEvens(numbers):
    return sum(isEven(n) for n in numbers)


print(countEvens([1, 4, 2, 7, 3, 1]))

# ---------------------------------------------------------


def shout(words):
    return " ".join(word.upper() + "!" for word in words)


print(shout(["germantown", "friends", "school"]))
