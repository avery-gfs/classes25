alphabet = "abcdefghijklmnopqrstuvwxyz"

# Shift a single letter `n` places


def shift(letter, n):
    lower = letter.lower()

    if lower in alphabet:
        shifted = alphabet[(alphabet.index(lower) + n) % 26]

        if letter.isupper():
            return shifted.upper()

        return shifted

    return lower


# Encode or decode a message with the Vigenère cipher
# https://en.wikipedia.org/wiki/Vigenere_cipher


def translate(message, key, sign):
    result = ""
    index = 0

    for letter in message:
        offset = alphabet.index(key[index])
        result += shift(letter, sign * offset)
        index = (index + 1) % len(key)

    return result


def encode(message, key):
    return translate(message, key, 1)


def decode(message, key):
    return translate(message, key, -1)


print(encode("a", "g") == "g")
print(encode("h", "g") == "n")
print(encode("he", "gf") == "nj")
print(encode("hello", "gfs") == "njdrt")

print(decode("g", "g") == "a")
print(decode("n", "g") == "h")
print(decode("nj", "gf") == "he")
print(decode("njdrt", "gfs") == "hello")

print(encode("Hello world!", "gfs") == "Njdrt ctjri!")
print(decode("Njdrt ctjri!", "gfs") == "Hello world!")

print(encode("Coding is cool :)", "gfs"))
print(decode("Itvosy nk hguq :)", "gfs"))

print(encode("Clementine", "bird"))
