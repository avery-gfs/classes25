import os
import time


def showRow(radius, sym):
    padding = " " * (6 - radius)
    width = radius * 2 + 1
    return padding + sym * width + padding


def showRows(tower):
    numBlanks = 6 - len(tower) + 1
    blanks = [showRow(0, "░")] * numBlanks
    discs = [showRow(row, "▇") for row in reversed(tower)]
    return blanks + discs


def showTowers():
    combined = [" "] * 7

    for tower in [towerA, towerB, towerC]:
        rows = showRows(tower)

        for index, row in enumerate(rows):
            combined[index] += row + " "

    os.system("clear")

    for row in combined:
        print(row)

    print("\n       A             B             C")

    time.sleep(0.2)


# https://en.wikipedia.org/wiki/Tower_of_Hanoi#Recursive_solution


# Tower Labels:
#
#     ░             ░             ░
#     ░             ░             ░
#     ░             ░             ░
#     ░             ░             ░
#     ░             ░             ░
#     ░             ░             ░
#     ░             ░             ░
#
#     A             B             C


def moveSingle(src, dest):
    dest.append(src.pop())
    showTowers()


def solve(src, dest, tmp, depth):
    if depth:
        solve(src, tmp, dest, depth - 1)
        moveSingle(src, dest)
        solve(tmp, dest, src, depth - 1)


towerA = [6, 5, 4, 3, 2, 1]
towerB = []
towerC = []

moveSingle(towerA, towerB)  # Check moveSingle
moveSingle(towerA, towerC)  # Check moveSingle
moveSingle(towerB, towerC)  # Check moveSingle

# Reset towers
towerA = [6, 5, 4, 3, 2, 1]
towerB = []
towerC = []

showTowers()
solve(towerA, towerC, towerB, 6)
