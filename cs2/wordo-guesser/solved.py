import random

with open("words.txt") as file:
    words = file.read().splitlines()

answer = ""

while len(answer) < 5:
    answer = random.choice(words)

position = words.index(answer) + 1
hintLen = 0

while True:
    print(f"answer position: {position}, starts with: {answer[:hintLen]}")
    guess = input("> ")

    if guess == answer:
        break

    if len(guess) < 5:
        print("too short")
        continue

    if guess not in words:
        print("not in words list")
        continue

    hintLen += 1
    guessPos = words.index(guess) + 1
    print(f"guess position: {guessPos}")

print("solved!")
