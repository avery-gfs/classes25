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
    # Move a single disc from the top of tower `src` to tower `dest`.
    #
    # For example, if towers are
    #
    #     towerA = [6, 5, 4]
    #     towerB = [3, 2, 1]
    #     towerC = []
    #
    # and we run
    #
    #     moveSingle(towerA, towerC)
    #
    # then towers will become
    #
    #     towerA = [6, 5]
    #     towerB = [3, 2, 1]
    #     towerC = [4]

    # Your code goes here

    showTowers()


def solve(src, dest, tmp, depth):
    # Using recursion, move the top `depth` discs from tower `src` to tower `dest`.
    #
    # For example, if towers are
    #
    #     towerA = [6, 5, 4, 3, 2, 1]
    #     towerB = []
    #     towerC = []
    #
    # and we run
    #
    #     solve(towerA, towerC, towerB, 3)
    #
    # then towers will become
    #
    #     towerA = [6, 5, 4]
    #     towerB = []
    #     towerC = [3, 2, 1]

    # Your code goes here

    pass


towerA = [6, 5, 4, 3, 2, 1]
towerB = []
towerC = []

# Test moveSingle
moveSingle(towerA, towerB)
moveSingle(towerA, towerC)
moveSingle(towerB, towerC)

# After the above three moveSingle calls we should see:

#        ░             ░             ░
#        ░             ░             ░
#        ░             ░             ░
#     ▇▇▇▇▇▇▇          ░             ░
#    ▇▇▇▇▇▇▇▇▇         ░             ░
#   ▇▇▇▇▇▇▇▇▇▇▇        ░            ▇▇▇
#  ▇▇▇▇▇▇▇▇▇▇▇▇▇       ░           ▇▇▇▇▇
#
#        A             B             C

# Reset towers
towerA = [6, 5, 4, 3, 2, 1]
towerB = []
towerC = []

showTowers()
solve(towerA, towerC, towerB, 6)

# After solving fully we should see:

#        ░             ░             ░
#        ░             ░            ▇▇▇
#        ░             ░           ▇▇▇▇▇
#        ░             ░          ▇▇▇▇▇▇▇
#        ░             ░         ▇▇▇▇▇▇▇▇▇
#        ░             ░        ▇▇▇▇▇▇▇▇▇▇▇
#        ░             ░       ▇▇▇▇▇▇▇▇▇▇▇▇▇
#
#        A             B             C
