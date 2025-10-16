# Implement quicksort:
#
# - If the list is empty, return an empty list
# - Otherwise, select the first number in the list as the pivot
#
# - Make three new lists:
#   - `low`: all numbers less than the pivot
#   - `mid`: all numbers equal to the pivot
#   - `high`: all numbers greater than the pivot
#
# - Recursively sort the `low` and `high` lists using the same process
# - Return the concatenation of `sort(low) + mid + sort(high)`, which gives the fully sorted list


def sort(numbers):
    if not numbers:
        return []

    pivot = numbers[0]

    low = [n for n in numbers if n < pivot]
    mid = [n for n in numbers if n == pivot]
    high = [n for n in numbers if n > pivot]

    return sort(low) + mid + sort(high)


print(sort([22, 15, 39, 6, 46, 46, 0, 43, 37, 45, 23, 15, 2, 43, 12, 2]))
