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


def showTiling(board):
    rows = [""] * 3

    rows[0] += "┌"
    rows[1] += getMiddle("1", board[0])
    rows[2] += "└"

    for index, tile in enumerate(board):
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


print(showTiling("122112"))
