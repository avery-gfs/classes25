import time
import os
import examples


class Cell:
    def __init__(self, active):
        self.active = active  # Whether the cell is active
        self.neighbors = 0  # Number of active neighbors to the cell

    def update(self):
        # Update self.active based on self.neighbors
        self.active = self.neighbors == 3 or self.active and self.neighbors == 2

    def __str__(self):
        # Return "██" if the cell is active, "░░" otherwise
        return "██" if self.active else "░░"


class Board:
    def __init__(self, initial):
        # Convert the starting board string to a grid (list of lists) of cells
        # Save the width and height of the board

        lines = initial.strip().splitlines()

        self.cells = []
        self.height = len(lines)
        self.width = len(lines[0])

        for line in lines:
            assert len(line) == self.width
            row = [Cell(sym != ".") for sym in line]
            self.cells.append(row)

    def get_state(self, r, c):
        # Return the active state of the cell at row `r` and column `c`,
        # or `False` if `r` or `c` are outside the bounds of the board

        if r < 0 or r >= self.height or c < 0 or c >= self.width:
            return False

        return self.cells[r][c].active

    def sum_neighbors(self, r, c):
        # Get the cell at row `r` and column `c`
        # Reset the cell's neighbor count to `0`

        cell = self.cells[r][c]
        cell.neighbors = 0

        # Then, or each active neighbor of the cell, add `1` to the cell's
        # neighbor count, using `self.get_state`

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr or dc:
                    cell.neighbors += self.get_state(r + dr, c + dc)

    def update(self):
        # First call sum_neighbors on each `(r, c)` coordinate of the board
        # where `r` is between `0` and `self.height - 1` and `c` is between
        # `0` and `self.width - 1`

        for r in range(self.height):
            for c in range(self.width):
                self.sum_neighbors(r, c)

        # Then, call `cell.update()` for each cell on the board

        for row in self.cells:
            for cell in row:
                cell.update()

    def __str__(self):
        # Visualize the cells in a 2D grid
        return "\n".join("".join(str(cell) for cell in row) for row in self.cells)


# ---------- Test cases

assert str(Cell(False)) == "░░"
assert str(Cell(True)) == "██"

cell = Cell(False)
cell.neighbors = 2
cell.update()
assert cell.active == False

cell = Cell(False)
cell.neighbors = 3
cell.update()
assert cell.active == True

cell = Cell(False)
cell.neighbors = 4
cell.update()
assert cell.active == False

cell = Cell(True)
cell.neighbors = 2
cell.update()
assert cell.active == True

cell = Cell(True)
cell.neighbors = 3
cell.update()
assert cell.active == True

cell = Cell(True)
cell.neighbors = 4
cell.update()
assert cell.active == False

board = Board(examples.blinker)

assert board.get_state(0, 0) == False
assert board.get_state(1, 2) == True
assert board.get_state(0, 5) == False
assert board.get_state(-1, 0) == False

board.update()

assert board.cells[0][0].neighbors == 0
assert board.cells[1][1].neighbors == 2
assert board.cells[2][1].neighbors == 3

assert str(board) == "░░░░░░░░░░\n░░░░░░░░░░\n░░██████░░\n░░░░░░░░░░\n░░░░░░░░░░"

# ---------- Run simulation

board = Board(examples.glider)

for generation in range(500):
    os.system("clear")
    print(board)
    print(f"generation: {generation}")
    time.sleep(0.2)
    board.update()
