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


def merge(listA, listB):
    result = []

    while listA and listB:
        if listA[0] < listB[0]:
            result.append(listA.pop(0))
        else:
            result.append(listB.pop(0))

    return result + listA + listB


# - If `numbers` is empty or has only a single value return `numbers`
#
# - Otherwise, split `numbers` in half to create two sub-lists
#
# - Sort each sublist and merge them together, returning the result


def sort(numbers):
    if len(numbers) <= 1:
        return numbers

    half = len(numbers) // 2
    left = numbers[half:]
    right = numbers[:half]

    return merge(sort(left), sort(right))


print(sort([22, 15, 39, 6, 46, 46, 0, 43, 37, 45, 23, 15, 2, 43, 12, 2]))
