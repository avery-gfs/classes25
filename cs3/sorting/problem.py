def isSorted(numbers):
    pass  # Your code goes here


print(isSorted([22, 15, 39, 6, 46, 46, 0, 43, 37, 45, 23, 15]))
print(isSorted([0, 6, 15, 15, 22, 23, 37, 39, 43, 45, 46, 46]))

# Implement selection sort
#
# - Copy the input list to avoid modifying it
# - Make an empty result list
# - While the (copied) input list has values:
#   - Find the minimum value
#   - Add it to the result list
#   - Remove it from the input list
# - Return the result list once the input is empty


def sort(numbers):
    numbers = numbers.copy()
    pass  # Your code goes here


print(sort([0, 6, 15, 15, 22, 23, 37, 39, 43, 45, 46, 46]))

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
    pass  # Your code goes here


print(quicksort([0, 6, 15, 15, 22, 23, 37, 39, 43, 45, 46, 46]))
