def product(listA, listB):
    # Generate the cartesian product of the values in listA and listB.
    #
    # You may assume that the values in both lists are strings.
    #
    # Your resulting list should contain strings containing each combination
    # of values from listA and listB with a space character in between.

    results = []

    for a in listA:
        for b in listB:
            results.append(f"{a} {b}")

    return results


def product(listA, listB):
    return [f"{a} {b}" for a in listA for b in listB]


# ----------------------------------------

suits = ["C", "D", "H", "S"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# Generate a list of each unique playing card

deck = product(ranks, suits)

for card in deck:
    print(card)

# ----------------------------------------

counts = ["one", "two", "three"]
shapes = ["diamond", "squiggle", "oval"]
shadings = ["solid", "striped", "open"]
colors = ["red", "green", "purple"]

# Use the product function to generate a list of each unique SET card

set_deck = product(product(product(counts, shapes), shadings), colors)

for card in set_deck:
    print(card)

# ----------------------------------------

# Implement a function that takes a list of lists, and returns the
# cartesian product of all of the lists. You may assume that
# `itemsList` is not empty.


def multiProduct(itemsLists):
    results = itemsLists[0]

    for items in itemsLists[1:]:
        results = product(results, items)

    return results


set_deck = multiProduct([counts, shapes, shadings, colors])

for card in set_deck:
    print(card)
