def factorial(n, result=1):
    # Calculate the factorial of `n` using tail recursion

    if n == 0:
        return result

    return factorial(n - 1, result * n)


print(factorial(10))  # Should print 3628800


def power2(n, result=1):
    # Calculate the `2 ** n` using tail recursion

    pass  # Your code goes here


print(power2(10))  # Should print 1024


def total(numbers, index=0, result=0):
    # Calculate the sum of the numbers in a list using tail recursion

    pass  # Your code goes here


print(total([5, 6, 7, 8, 9]))  # Should print 35


def minimum(numbers, index=0, result=None):
    # Find the minimum value in a list using tail recursion
    # Don't use the built-in `min` or `max` functions

    pass  # Your code goes here


print(minimum([68, 10, 13, 2, 13, 10, 57, 12, 80, 82]))  # Should print 2
