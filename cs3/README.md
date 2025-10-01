<!-- ## Sorting

## Sorting -->

https://en.wikipedia.org/wiki/Selection_sort

---

## Cartesian Product

<img src="assets/cartesian1.png" />

## Card Deck

<img src="assets/52-card-deck.png" />

## Generating

```py
suits = ["C", "D", "H", "S"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

for suit in suits:
  for rank in ranks:
    print(suit, rank)
```

```txt
C A
C 2
C 3
C 4
C 5
C 6
C 7
C 8
C 9
C 10
C J
C Q
C K
D A
D 2
D 3
D 4
D 5
...
```

## Generating

```py
suits = ["C", "D", "H", "S"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

for rank in ranks:
  for suit in suits:
    print(suit, rank)
```

```txt
C A
D A
H A
S A
C 2
D 2
H 2
S 2
C 3
D 3
H 3
S 3
C 4
D 4
H 4
S 4
C 5
D 5
...
```

## Set Deck

<img src="assets/PNG-Promo-Z1.webp" />

---

## Tiling Representation

`1` and `2` representation

```txt
┌─┐  ┌───┐
│ │  ├───┤
└─┘  └───┘
 1     2
```

Worksheet

## Tiling Representation

`1` and `2` representation

```txt
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

## Tiling String Generation

```py
getTilings(0) # [""]
getTilings(1) # ["1"]
getTilings(2) # ["11", "2"]
getTilings(3) # ["111", "12", "21"]
getTilings(4) # ["1111", "112", "121", "211", "22"]
getTilings(5) # ["11111", "1112", "1121", "1211", "122", "2111", "212", "221"]
# ...
```

---

## Tiles Puzzle

<img src="assets/tiles.png" />

There are `3` distinct ways to tile a `2x3` board with `2x1` tiles.

How many distinct ways are there to tile `2x10` board with `2x1` tiles? Find a
proof for the correctness of your answer.

## Solution

```txt
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, ...
```

$$
F_0 = 0
$$

$$
F_1 = 1
$$

$$
F_n = F_{n - 1} + F_{n - 2}
$$

<img src="assets/fibonacci-tree.png" height="300px" />

## Tiles Proof

```txt
┌─┬─┬─┬─┐   ┌─┐   ┌─┬─┬─┐
│ │ │ │ │ = │ │ + │ │ │ │
└─┴─┴─┴─┘   └─┘   └─┴─┴─┘
   2x4              2x3

┌─┬─┬───┐   ┌─┐   ┌─┬───┐
│ │ ├───┤ = │ │ + │ ├───┤
└─┴─┴───┘   └─┘   └─┴───┘
   2x4              2x3

┌─┬───┬─┐   ┌─┐   ┌───┬─┐
│ ├───┤ │ = │ │ + ├───┤ │
└─┴───┴─┘   └─┘   └───┴─┘
   2x4              2x3

┌───┬─┬─┐   ┌───┐   ┌─┬─┐
├───┤ │ │ = ├───┤ + │ │ │
└───┴─┴─┘   └───┘   └─┴─┘
   2x4               2x2

┌───┬───┐   ┌───┐   ┌───┐
├───┼───┤ = ├───┤ + ├───┤
└───┴───┘   └───┘   └───┘
   2x4               2x2
```

---

## Default Params

```py
def greet(name, greeting="Hello"):
  print(f"{greeting} {name}!")

greet("Avery")       # Prints "Hello Avery!"
greet("Avery", "Hi") # Prints "Hi Avery!"
```

## Recursive Factorial

```py
def factorial(n):
  if n == 0:
    return 1

  return n * factorial(n - 1)

print(factorial(10)) # Prints 3628800
```

## Tail Recursion

```py
def factorial(n, result):
  if n == 0:
    return result

  return factorial(n - 1, n * result)

print(factorial(10, 1)) # Prints 3628800
```

- Still has base case and recursive case
- Uses an _accumulator_ (result) parameter, which get's returned at the end
- https://en.wikipedia.org/wiki/Recursion_(computer_science)#Tail-recursive_functions

```txt
factorial(10, 1)
factorial(9, 10 * 1)
factorial(8, 10 * 9 * 1)
factorial(7, 10 * 9 * 8 * 1)
factorial(6, 10 * 9 * 8 * 7 * 1)
factorial(5, 10 * 9 * 8 * 7 * 6 * 1)
factorial(4, 10 * 9 * 8 * 7 * 6 * 5 * 1)
factorial(3, 10 * 9 * 8 * 7 * 6 * 5 * 4 * 1)
factorial(2, 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 1)
factorial(1, 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)
factorial(0, 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 * 1)
10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 * 1
```

## Tail Recursion Default Params

```py
def factorial(n, result=1):
  if n == 0:
    return result

  return factorial(n - 1, n * result)

print(factorial(10)) # Prints 3628800
```

## Tail Recursion with Lists

```py
def total(numbers, index=0, result=0):
    # Calculate the sum of the numbers in a list recursively
    # ...
```

```txt
total([5, 6, 7, 8, 9], 0, 0)
total([5, 6, 7, 8, 9], 1, 5 + 0)
total([5, 6, 7, 8, 9], 2, 5 + 6 + 0)
total([5, 6, 7, 8, 9], 3, 5 + 6 + 7 + 0)
total([5, 6, 7, 8, 9], 4, 5 + 6 + 7 + 8 + 0)
total([5, 6, 7, 8, 9], 5, 5 + 6 + 7 + 8 + 9 + 0)
5 + 6 + 7 + 8 + 9 + 0
```

## Why No Tail Recursive Fibonacci?

```py
def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)
```

---

## Recursion

What does this code do?

```py
def hello():
  print("Hello world!")

hello()
```

## Recursion (continued)

What does this code do?

```py
def hello():
  print("Hello world!")
  hello()

hello()
```

## Recursion (continued)

What does this code do?

```py
def hello():
  hello()
  print("Hello world!")

hello()
```

## Recursion (continued)

What does this code do?

```py
def hello(n):
  if n < 10:
    print("Hello world!")
    hello(n + 1)

hello(0)
```

## Recursion (continued)

What does this code do?

```py
def hello(n):
  if n < 10:
    print("Hello world!")
    hello(n + 1)
  else:
    print("Done")

hello(0)
```

## Recursion (continued)

What does this code do?

```py
def hello(n):
  if n < 10:
    print("Hello world!")
    hello(n + 1)
    print("Goodbye")

hello(0)
```

## Koan

> To understand recursion, you must first understand recursion.

## Factorial Definition

```txt
factorial(0) = 1
factorial(n) = n * (n - 1) * ... * 1
```

```txt
factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
```

$n!$ = `factorial(n)`

## Recursive Factorial

```txt
factorial(0) = 1
factorial(n) = n * factorial(n - 1)
```

```txt
factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
```

## Iterative Functions

```py
def factorial(n):
  result = 1

  for i in range(1, n + 1):
    result *= i

  return result

print(factorial(10)) # Prints 3628800
```

## Recursive Functions

```py
def factorial(n):
  if n == 0:
    return 1

  return n * factorial(n - 1)

print(factorial(10)) # Prints 3628800
```

Recursive functions: functions which call themselves

```txt
factorial(10)
10 * factorial(9)
10 * 9 * factorial(8)
10 * 9 * 8 * factorial(7)
10 * 9 * 8 * 7 * factorial(6)
10 * 9 * 8 * 7 * 6 * factorial(5)
10 * 9 * 8 * 7 * 6 * 5 * factorial(4)
10 * 9 * 8 * 7 * 6 * 5 * 4 * factorial(3)
10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * factorial(2)
10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * factorial(1)
10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 * factorial(0)
10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 * 1
```

## Base Case

```py
def factorial(n):
  if n == 0:
    return 1

  return n * factorial(n - 1)

print(factorial(10)) # Prints 3628800
```

Case in which the function doesn't call itself recursively

```txt
0! = 1
```

```py
if n == 0:
  return 1
```

## Recursive Case

```py
def factorial(n):
  if n == 0:
    return 1

  return n * factorial(n - 1)

print(factorial(10)) # Prints 3628800
```

Case in which the function calls itself recursively

```txt
n! = n * (n - 1)!
```

```py
return n * factorial(n - 1)
```

## Visualizing Recursion

https://pythontutor.com/render.html#mode=display

## Recursive Summation

```py
def summation(n):
  if n == 0:
    return 0

  return n + summation(n - 1)

print(summation(10)) # Prints 55
```

```txt
summation(10)
10 + summation(9)
10 + 9 + summation(8)
10 + 9 + 8 + summation(7)
10 + 9 + 8 + 7 + summation(6)
10 + 9 + 8 + 7 + 6 + summation(5)
10 + 9 + 8 + 7 + 6 + 5 + summation(4)
10 + 9 + 8 + 7 + 6 + 5 + 4 + summation(3)
10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + summation(2)
10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + summation(1)
10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 + summation(0)
10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 + 0
```

## Fibonacci is Recursive

```txt
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, ...
```

$$
F_0 = 0
$$

$$
F_1 = 1
$$

$$
F_n = F_{n - 1} + F_{n - 2}
$$

<img src="assets/fibonacci-tree.png" height="300px" />

## Recursion With Lists

```py
def total(numbers, index):
    # Calculate the sum of the numbers in a list recursively
    # ...
```

```txt
total([5, 6, 7, 8, 9], 0)
5 + total([5, 6, 7, 8, 9], 1)
5 + 6 + total([5, 6, 7, 8, 9], 2)
5 + 6 + 7 + total([5, 6, 7, 8, 9], 3)
5 + 6 + 7 + 8 + total([5, 6, 7, 8, 9], 4)
5 + 6 + 7 + 8 + 9 + total([5, 6, 7, 8, 9], 5)
5 + 6 + 7 + 8 + 9 + 0
```

## Recursive Functions

Challenge: recursive minimum

---

## Fibonacci Sequence

https://en.wikipedia.org/wiki/Fibonacci_sequence

$$
F_0 = 0
$$

$$
F_1 = 1
$$

$$
F_n = F_{n - 1} + F_{n - 2}
$$

```txt
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, ...
```

## Fibonacci Worksheet

## Fibonacci Generator

---

## `12(3)4` Puzzle

Starting with a number `n`, you have two choices:

1. You can subtract `3` from `n`:

```txt
n = n - 3
```

2. You can multiply `n` by `2`:

```txt
n = n * 2
```

You may repeat this process as many times as you like.

Starting from `n = 1`, can you reach `n = 24`? Either find a sequence of
transitions using the rules above that gets you from `1` to `24`, or prove that
none exists.

_Hint: Look for a pattern in what numbers can and can't be reached starting from
`1` using these rules. Prove that this pattern always holds no matter how many
times the rules are applied._

## Chessboard Tiling Puzzle

<img src="assets/board.png" height="250px" />

You have a chessboard (an `8x8` grid of checkered light and dark squares) which
is missing its two dark corner squares, leaving `62` squares remaining. Can you
tile this board with `2x1` tiles? Provide a tiling, or a proof that none exists.

_In this problem, "tiling" means covering the board with tiles so that each tile
covers two squares, each square is covered by a tile, and no tiles overlap or
hang off the edge of the board._

_Hint: use the fact that checkered pattern to your advantage._

---

## Maze Worksheet

## Demo Projects

- Maze
- Tower
- VM

## What is CS3

- Practice vs theory
- Programming vs CS
- Hard problems w/ easy solutions vs easy problems w/ hard solutions

## Grading policy

[Link](../shared/grading.md)

## Python setup

Idle:

- [Idle](https://www.python.org/downloads/)

VSCode:

- [VSCode](https://code.visualstudio.com/)
- [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## Review

- Define a variable
- Make an empty list
- Make an infinite loop
- Print out `Hello <name>` based on the value in the variable `name`
- Get a name string from the user as input and print out `Hello <name>`
- Check if a value is in a list
- Add a value to a list
- Remove a value from a list

## To-do List
