# Calculate the nth fibonacci number
#
# fibonacci(10) should return 55


def fibonacci(n):
    if n == 0:
        return 0

    oldF = 0
    currentF = 1

    for i in range(n - 1):
        newF = currentF + oldF
        oldF = currentF
        currentF = newF

    return currentF


print(fibonacci(10))
