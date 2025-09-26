print("CS 3 Info")

print(
    {
        "name": "Avery Nortonsmith",
        "email": "anortonsmith@germantownfriends.org",
    }
)

description = """
This class will explore advanced topics and questions in software engineering and problem solving. How can we use algorithmic analysis to predict how our code will perform? How do we translate our intuitive understanding of an algorithm into code? When does using self-reference simplify our code and when does it make it more complex? How does a computer represent text, numbers, and directory structures internally?
"""

print(description.replace("\n", " ").strip())

topics = [
    "Recursion",
    "Functional programming",
    "Algorithm design and analysis",
    "Dynamic programming",
    "Data structures",
    "Low-level programming",
    "Design principles",
    "Proving properties of systems",
    "Programming language internals",
]

print("\n".join(f"• {topic}" for topic in topics))

# █████████████████████████████████
# █▒█     █B█▒▒▒▒▒    █▒▒▒      █ █
# █▒█ ███ █▒█▒███▒█████▒█▒█████ █ █
# █▒█ █ █ █▒▒▒  █▒▒▒▒▒▒▒█▒█▒▒▒█   █
# █▒█ █ █ ███████████ ███▒█▒█▒█████
# █▒  █ █     █     █ █ █▒▒▒█▒▒▒▒▒█
# █▒███ █████ █ ███ █ █ ███████ █▒█
# █▒█▒▒▒▒▒█ █ █ █ █ █       █ █ █▒█
# █▒█▒███▒█ █ █ █ █ █████████ ███▒█
# █▒█▒▒▒█▒▒▒█ █   █   █       █▒▒▒█
# █▒███▒███▒█ ███ ███ █ ███████▒█ █
# █▒█▒▒▒█ █▒█     █ █   █▒▒▒█▒▒▒█ █
# █▒█▒███ █▒███████ █████▒█▒█▒███ █
# █▒█▒▒▒█ █▒▒▒▒▒▒▒█▒▒▒█▒▒▒█▒█▒█ █ █
# █▒███▒█ ███████▒█▒█▒█▒███▒█▒█ █ █
# █▒▒▒▒▒█        ▒▒▒█▒▒▒█  ▒▒▒█   █
# █████████████████████████████████

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


def search(r, c):
    match board[r][c]:
        case "B":
            return True
        case "█" | "▒":
            return False

    update(r, c, "▒")

    if search(r - 1, c) or search(r, c + 1) or search(r + 1, c) or search(r, c - 1):
        return True

    update(r, c, " ")
    return False


search(1, 1)
