# - Iterate as long as both `listA` and `listB` have elements:
#
#   - Compare the first elements of each list
#
#   - If the first element of `listA` is smaller, append it to the result
#     and remove it from `listA`
#
#   - Otherwise, append the first element of `listB` to the result
#     and remove it from `listB`
#
# - Add any leftover values from `listA` and `listB` to `result`
#
# - Note that you can use `list.pop(0)` to get and remove the first value
#   from a list
#
# - Note that you can use `list1.extend(list2)` to add the values from one the
#   `list2` to the `list1`


def merge(listA, listB):
    result = []

    return result


print(merge([0, 6, 15, 22, 39, 43, 46, 46], [2, 2, 12, 15, 23, 37, 43, 45]))

# - If `numbers` is empty or has only a single value return `numbers`
#
# - Otherwise, split `numbers` in half to create two sub-lists
#
# - Sort each sublist and merge them together, returning the result


def sort(numbers):
    half = len(numbers) // 2
    left = numbers[half:]
    right = numbers[:half]


print(sort([22, 15, 39, 6, 46, 46, 0, 43, 37, 45, 23, 15, 2, 43, 12, 2]))
