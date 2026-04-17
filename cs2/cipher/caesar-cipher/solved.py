alphabet = "abcdefghijklmnopqrstuvwxyz"

# Shift a single letter `offset` places


def shift(letter, offset):
    lower = letter.lower()

    if lower in alphabet:
        shift = (alphabet.index(lower) + offset) % 26
        shifted = alphabet[shift]

        if letter.isupper():
            return shifted.upper()

        return shifted

    return lower


# Encode or decode a message with the Caesar cipher
# https://en.wikipedia.org/wiki/Caesar_cipher


def encode(message, offset):
    result = ""

    for letter in message:
        result += shift(letter, offset)

    return result


print(shift("a", 1) == "b")
print(shift("a", 13) == "n")
print(shift("a", 39) == "n")
print(shift("a", -1) == "z")
print(shift("A", 3) == "D")
print(shift("!", 3) == "!")

print(encode("Rovvy gybvn!", -10) == "Hello world!")
print(encode(encode("Hello world!", 10), -10) == "Hello world!")

print(encode("Coding is cool :)", 7))
print(encode("Jvkpun pz jvvs :)", -7))
