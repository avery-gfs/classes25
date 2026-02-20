import time
import os

hexBlocks = {
    "0": "        ",
    "1": "      ██",
    "2": "    ██  ",
    "3": "    ████",
    "4": "  ██    ",
    "5": "  ██  ██",
    "6": "  ████  ",
    "7": "  ██████",
    "8": "██      ",
    "9": "██    ██",
    "a": "██  ██  ",
    "b": "██  ████",
    "c": "████    ",
    "d": "████  ██",
    "e": "██████  ",
    "f": "████████",
}


def drawFrame(frame):
    output = "┌────────────────┐\n│"

    for index, hexChar in enumerate(frame):
        if index and index % 2 == 0:
            output += "│\n│"

        output += hexBlocks[hexChar]

    os.system("clear")
    output += "│\n└────────────────┘"
    print(output)


def animate(frames, fps):
    while True:
        for frame in frames:
            drawFrame(frame)
            time.sleep(1 / fps)


import demos

# animate(demos.smile, 2)
# animate(demos.gfs, 4)
# animate(demos.arrow, 10)
# animate(demos.bounce, 10)
animate(demos.snake, 12)

custom = [
    "0042001800427e00",
]

# animate(custom, 10)
