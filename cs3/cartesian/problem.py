def product(listA, listB):
    # Generate the cartesian product of the values in listA and listB.
    #
    # You may assume that the values in both lists are strings.
    #
    # Your resulting list should contain strings containing each combination
    # of values from listA and listB with a space character in between.

    results = []

    # Your code goes here

    return results


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

# Generate a list of each unique SET card

set_deck = []  # Your code goes here

for card in set_deck:
    print(card)
