alphabet = "abcdefghijklmnopqrstuvwxyz"

# Shift a single letter `n` places


def shift(letter, n):
    pass


# Encode or decode a message with the Caesar cipher
# https://en.wikipedia.org/wiki/Caesar_cipher


def encode(message, offset):
    result = ""
    pass


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
