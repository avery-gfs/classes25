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


# Our original probe function didn't return any value. It also didn't
# stop when it reached the goal, and erased every path it explored,
# including the one that found the goal. Our search function will be
# similar to probe, but it should:
#
# 1) Return `True` if the search branch(es) starting from a given (r, c)
#    position found the goal, and `False` otherwise
#
# 2) Stop searching once the goal is reached
#
# 3) Not erase the succeeding path


def search(r, c):
    cell = board[r][c]

    if cell == "█" or cell == "▒":
        return False

    update(r, c, "▒")

    if cell == "B":
        return True

    # Use the return value from the child search calls to decide
    # whether to keep searching / whether to erase the path

    search(r - 1, c)
    search(r + 1, c)
    search(r, c - 1)
    search(r, c + 1)

    update(r, c, " ")

    return False


search(1, 1)
