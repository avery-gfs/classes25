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
# - Return the concatenation of `quicksort(low) + mid + quicksort(high)`, which gives the fully sorted list


def quicksort(numbers):
    if not numbers:
        return []

    pivot = numbers[0]

    low = [n for n in numbers if n < pivot]
    mid = [n for n in numbers if n == pivot]
    high = [n for n in numbers if n > pivot]

    return quicksort(low) + mid + quicksort(high)


print(quicksort([1, 4, 2, 7, 3, 1]))

print(
    quicksort(
        [
            22,
            15,
            39,
            6,
            46,
            49,
            0,
            43,
            37,
            45,
            23,
            20,
            15,
            24,
            13,
            23,
            46,
            26,
            17,
            18,
        ]
    )
)
