def factorial(n):
    # Calculate the factorial of `n` recursively

    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(10))  # Should print 3628800


def fibonacci(n):
    # Calculate the nth fibonacci number recursively

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))  # Should print 55


def power2(n):
    # Calculate the `2 ** n` recursively, without using the
    # built-in exponentiation functionality

    if n == 0:
        return 1

    return 2 * power2(n - 1)


print(power2(10))  # Should print 1024


def total(numbers, index):
    # Calculate the sum of the numbers in a list recursively

    if index == len(numbers):
        return 0

    return numbers[index] + total(numbers, index + 1)


print(total([5, 6, 7, 8, 9]))  # Should print 35


def contains(items, value, index):
    # Check if a list of items contains a value recursively

    if index == len(items):
        return False

    if items[index] == value:
        return True

    return contains(items, value, index + 1)


print(contains(["a", "s", "d", "f"], "d", 0))  # Should print True
