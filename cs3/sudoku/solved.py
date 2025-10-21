import os
import time

# board = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 0, 8, 5],
#     [0, 0, 1, 0, 2, 0, 0, 0, 0],
#     [0, 0, 0, 5, 0, 7, 0, 0, 0],
#     [0, 0, 4, 0, 0, 0, 1, 0, 0],
#     [0, 9, 0, 0, 0, 0, 0, 0, 0],
#     [5, 0, 0, 0, 0, 0, 0, 7, 3],
#     [0, 0, 2, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 4, 0, 0, 0, 9],
# ]

# board = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9],
# ]

board = [
    [0, 4, 0, 0, 2, 0, 8, 6, 5],
    [7, 0, 0, 6, 0, 8, 0, 0, 0],
    [1, 0, 0, 0, 0, 4, 7, 0, 2],
    [0, 1, 8, 7, 4, 0, 0, 0, 0],
    [0, 0, 5, 2, 0, 9, 6, 0, 0],
    [0, 0, 0, 0, 8, 6, 1, 5, 0],
    [9, 0, 1, 5, 0, 0, 0, 0, 6],
    [0, 0, 0, 8, 0, 2, 0, 0, 7],
    [8, 7, 3, 0, 6, 0, 0, 2, 0],
]


rows = [
    set(),
    set(),
    set(),
    set(),
    set(),
    set(),
    set(),
    set(),
    set(),
]

cols = [
    set(),
    set(),
    set(),
    set(),
    set(),
    set(),
    set(),
    set(),
    set(),
]

blocks = [
    [
        set(),
        set(),
        set(),
    ],
    [
        set(),
        set(),
        set(),
    ],
    [
        set(),
        set(),
        set(),
    ],
]

for r in range(9):
    for c in range(9):
        n = board[r][c]

        if n > 0:
            rows[r].add(n)
            cols[c].add(n)
            blocks[r // 3][c // 3].add(n)


def solve(r, c):
    if c == 9:
        c = 0
        r += 1

    if r == 9:
        return True

    if board[r][c] > 0:
        return solve(r, c + 1)

    br = r // 3
    bc = c // 3

    for n in range(1, 10):
        if n not in rows[r] and n not in cols[c] and n not in blocks[br][bc]:
            board[r][c] = n
            rows[r].add(n)
            cols[c].add(n)
            blocks[br][bc].add(n)

            showBoard(board)

            if solve(r, c + 1):
                return True

            board[r][c] = 0
            rows[r].remove(n)
            cols[c].remove(n)
            blocks[br][bc].remove(n)

    return False


def showRow(row):
    disp = [str(x) if x else " " for x in row]
    print("{0} {1} {2} | {3} {4} {5} | {6} {7} {8}".format(*disp))


def showBoard(board):
    os.system("clear")

    showRow(board[0])
    showRow(board[1])
    showRow(board[2])

    print("------+-------+------")

    showRow(board[3])
    showRow(board[4])
    showRow(board[5])

    print("------+-------+------")

    showRow(board[6])
    showRow(board[7])
    showRow(board[8])

    time.sleep(0.1)


solve(0, 0)
