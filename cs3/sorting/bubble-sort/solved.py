# Implement an optimized bubble sort.
#
# - Loop backwards from the end of the list. This outer loop
#   shrinks the unsorted part of the list with each pass
#
# - In an inner loop, iterate from the start up to the unsorted boundary
#   - Compare each element to the next one
#   - If they are in the wrong order, swap them
#
# - Return the sorted list, which has been modified in-place


def sort(numbers):
    for limit in range(len(numbers) - 1, 0, -1):
        for i in range(limit):
            if numbers[i] > numbers[i + 1]:
                tmp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = tmp

    return numbers


print(sort([22, 15, 39, 6, 46, 46, 0, 43, 37, 45, 23, 15, 2, 43, 12, 2]))
