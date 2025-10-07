list1 = [1, 4, 2, 7, 3, 1]
list2 = [22, 15, 39, 6, 46, 49, 0, 43, 37, 45, 23, 20, 15, 24, 13, 23, 46, 26, 17, 18]

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
    pass


print(sort(list1))
print(sort(list2))

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
    pass


print(quicksort(list1))
print(quicksort(list2))
