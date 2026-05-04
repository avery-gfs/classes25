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


# Encode or decode a message with the Vigenère cipher
# https://en.wikipedia.org/wiki/Vigenere_cipher


def translate(message, key, sign):
    result = ""
    index = 0

    for letter in message:
        offset = alphabet.index(key[index])
        result += shift(letter, sign * offset)

        if letter.lower() in alphabet:
            index += 1

        index %= len(key)

    return result


def encode(message, key):
    return translate(message, key, 1)


def decode(message, key):
    return translate(message, key, -1)


# print(encode("a", "g") == "g")
# print(encode("h", "g") == "n")
# print(encode("he", "gf") == "nj")
# print(encode("hello", "gfs") == "njdrt")

# print(decode("g", "g") == "a")
# print(decode("n", "g") == "h")
# print(decode("nj", "gf") == "he")
# print(decode("njdrt", "gfs") == "hello")

# print(encode("Hello world!", "gfs") == "Njdrt ctjri!")
# print(decode("Njdrt ctjri!", "gfs") == "Hello world!")

# print(encode("Coding is cool :)", "gfs"))
# print(decode("Itvosy nk hguq :)", "gfs"))

print(
    encode(
        """
My life flows on in endless song, above Earth's lamentation. I hear the real, though far off hymn, that hails the new creation. Above the tumult and the strife, I hear the music ringing. It sounds an echo in my soul, how can I keep from singing?

What though the tempest loudly roars, I hear the truth, it liveth. What though the darkness round me close, songs in the night it giveth. No storm can shake my inmost calm, while to that rock I'm clinging. Since love is lord of Heaven and Earth, how can I keep from singing?

When tyrants tremble, sick with fear, and hear their death-knell ringing; when friends rejoice both far and near, how can I keep from singing? In prison cell and dungeon vile, our thoughts to them are winging. When friends by shame are undefiled, how can I keep from singing?
""",
        "sing",
    )
)
