# def countChange(goal):
# 	total = 0

# 	for quarters in range(0, goal + 1, 25):
# 		for dimes in range(0, goal + 1 - quarters, 10):
# 			total += (goal - quarters - dimes) // 5 + 1

# 	return total


def countChange(goal, coins):
    if goal == 0:
        return 1

    if not coins:
        return 0

    total = 0

    for n in range(0, goal + 1, coins[0]):
        total += countChange(goal - n, coins[1:])

    return total


print(countChange(50, [25, 10, 5, 1]))
