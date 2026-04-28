alphabet = "abcdefghijklmnopqrstuvwxyz"

# Shift a single letter `offset` places


def shift(letter, offset):
    # Copy code from Caesar cipher problem
    pass


# Encode or decode a message with the Vigenère cipher
# https://en.wikipedia.org/wiki/Vigenere_cipher


def translate(message, key, sign):
    result = ""
    pass


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
