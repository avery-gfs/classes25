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

    for tower in towers:
        rows = showRows(tower)

        for index, row in enumerate(rows):
            combined[index] += row + " "

    os.system("clear")

    for row in combined:
        print(row)

    time.sleep(0.2)


# https://en.wikipedia.org/wiki/Tower_of_Hanoi#Iterative_solution


def moveSingle(src, dest):
    towers[dest].append(towers[src][-1])
    towers[src].pop()
    showTowers()


def canMove(src, dest):
    if not towers[src]:
        return False

    if not towers[dest]:
        return True

    return towers[src][-1] < towers[dest][-1]


def solve(src, dest, depth):
    if depth:
        tmp = 3 - src - dest
        solve(src, tmp, depth - 1)
        moveSingle(src, dest)
        solve(tmp, dest, depth - 1)


transitionsA = [0, 0, 1]
transitionsB = [1, 2, 2]


def step(n):
    a = transitionsA[n % 3]
    b = transitionsB[n % 3]

    if canMove(a, b):
        moveSingle(a, b)
    else:
        moveSingle(b, a)


towers = [[6, 5, 4, 3, 2, 1], [], []]
showTowers()

for n in range(2**6 - 1):
    step(n)
