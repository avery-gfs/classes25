def binToDec(s):
    result = 0
    power = 2 ** (len(s) - 1)

    for d in s:
        if d == "1":
            result += power

        power //= 2

    return result


print(binToDec("11010"))  # Should print 26


def decToBin(n):
    result = ""

    while n > 0:
        if n % 2 == 0:
            result = "0" + result
        else:
            result = "1" + result

        n //= 2

    return result


print(decToBin(26))  # Should print 11010

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


def hexToDec(s):
    result = 0
    power = 16 ** (len(s) - 1)

    for d in s:
        result += hexValues[d] * power
        power //= 16

    return result


print(hexToDec("1a"))  # Should print 26

hexDigits = "0123456789abcdef"


def decToHex(n):
    result = ""

    while n > 0:
        result = hexDigits[n % 16] + result
        n //= 16

    return result


print(decToHex(26))  # Should print 1a
