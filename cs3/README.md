<!-- ```py
bestScore = 0 # Keep track of the highest score
bestWord = None # Keep track of the highest scoring word

# Find the word with the highest Scrabble score

for word in words:
    score = 0

    # Loop through each letter in the current word
    for letter in word:
        score += letterPoints[letter]

    # Alternatively, we could use:
    # score = sum(letterPoints[letter] for letter in word)

    if score > bestScore:
        bestScore = score
        bestWord = word
        
print(bestWord)
```
 -->

**Tilings Generator**

- `1` and `2` representation
- *Practice worksheet*
- *Problem*

```
┌─┬─┬─┬─┐   ┌─┐   ┌─┬─┬─┐
│ │ │ │ │ = │ │ + │ │ │ │
└─┴─┴─┴─┘   └─┘   └─┴─┴─┘
 1 1 1 1     1     1 1 1

┌─┬─┬───┐   ┌─┐   ┌─┬───┐
│ │ ├───┤ = │ │ + │ ├───┤
└─┴─┴───┘   └─┘   └─┴───┘
 1 1  2      1     1  2

┌─┬───┬─┐   ┌─┐   ┌───┬─┐
│ ├───┤ │ = │ │ + ├───┤ │
└─┴───┴─┘   └─┘   └───┴─┘
 1  2  1     1      2  1

┌───┬─┬─┐   ┌───┐   ┌─┬─┐
├───┤ │ │ = ├───┤ + │ │ │
└───┴─┴─┘   └───┘   └─┴─┘
  2  1 1      2      1 1

┌───┬───┐   ┌───┐   ┌───┐
├───┼───┤ = ├───┤ + ├───┤
└───┴───┘   └───┘   └───┘
  2   2       2       2
```

---

**Fibonacci Sequence**

https://en.wikipedia.org/wiki/Fibonacci_sequence

**Fibonacci Generator**

- Negative list indices
- *Problem*

**Tilings proof**

- *Proof*

---

**Make a programming quiz question**

- Can be true/false, multiple choice, or short response
- It must be an original question
- It must have a concrete, known answer
- Can ask about the Python language, CS theory, or general problem-solving
- Cannot involve third-party libraries

**Proving properties using invariants**

- *12(3)4 proof*
- *Chessboard proof*
