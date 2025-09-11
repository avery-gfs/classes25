# Get the list of all possible tiling strings for a board with width n.
# Tiling strings are made of up digits `1` and `2`, where `1` represents
# a single vertical tile and `2` represents two horizontal tiles.
#
# getTilings(4) should return
#
# ['1111', '112', '121', '211', '22']

def getTilings(n):
	# Your code goes here
	return ["1211"]

def getMiddle(left, right):
	match (left, right):
		case ("1", "1"):
			return "│"
		case ("1", "2"):
			return "├"
		case ("2", "1"):
			return "┤"
		case ("2", "2"):
			return "┼"

# print(showTiling("122112")) will display
#
# ┌─┬───┬───┬─┬─┬───┐
# │ ├───┼───┤ │ ├───┤
# └─┴───┴───┴─┴─┴───┘

def showTiling(board):
	rows = [""] * 3

	rows[0] += "┌"
	rows[1] += getMiddle("1", board[0])
	rows[2] += "└"

	for (index, tile) in enumerate(board):
		if tile == "1":
			rows[0] += "─"
			rows[1] += " "
			rows[2] += "─"
		else:
			rows[0] += "───"
			rows[1] += "───"
			rows[2] += "───"

		if index < len(board) - 1:
			rows[0] += "┬"
			rows[1] += getMiddle(tile, board[index + 1])
			rows[2] += "┴"

	rows[0] += "┐"
	rows[1] += getMiddle(board[-1], "1")
	rows[2] += "┘"

	return "\n".join(rows)

print(getTilings(6))

for tiling in getTilings(6):
	print(showTiling(tiling))
