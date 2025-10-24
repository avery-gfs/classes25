import os
import time

maze = """
█████████████████████████████████
█A█     █B█         █         █ █
█ █ ███ █ █ ███ █████ █ █████ █ █
█ █ █ █ █     █       █ █   █   █
█ █ █ █ ███████████ ███ █ █ █████
█   █ █     █     █ █ █   █     █
█ ███ █████ █ ███ █ █ ███████ █ █
█ █     █ █ █ █ █ █       █ █ █ █
█ █ ███ █ █ █ █ █ █████████ ███ █
█ █   █   █ █   █   █       █   █
█ ███ ███ █ ███ ███ █ ███████ █ █
█ █   █ █ █     █ █   █   █   █ █
█ █ ███ █ ███████ █████ █ █ ███ █
█ █   █ █       █   █   █ █ █ █ █
█ ███ █ ███████ █ █ █ ███ █ █ █ █
█     █           █   █     █   █
█████████████████████████████████
"""

board = [list(row) for row in maze.strip().split("\n")]


def update(r, c, symbol):
    board[r][c] = symbol
    os.system("clear")
    print("\n".join("".join(row) for row in board))
    time.sleep(0.05)


def probe(r, c):
    # Edit the code in `probe` to write a function that probes the board

    # Demo code which accesses the character at the current position in the
    # board, updates the board at the current position, and recursively probes
    # the cell below the current one

    cell = board[r][c]
    update(r, c, "▒")
    probe(r + 1, c)


probe(1, 1)
