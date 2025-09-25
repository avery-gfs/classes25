<!-- ## Sorting

## Cartesian

## Sorting -->

## Default Params

```py
def greet(name, greeting="Hello"):
  print(f"{greeting} {name}!")

greet("Avery")       # Prints "Hello Avery!"
greet("Avery", "Hi") # Prints "Hi Avery!"
```

## Recursive Fibonacci

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

https://en.wikipedia.org/wiki/Recursion_(computer_science)#Tail-recursive_functions

## Tail Recursion (Continued)

```py
def factorial(n, result=1):
  if n == 0:
    return result

  return factorial(n - 1, n * result)

print(factorial(10)) # Prints 3628800
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

## Factorial

$$
n! = \prod_{i=1}^{n} i
$$

```txt
n! = n * (n - 1) * ... * 1
```

```txt
0! = 1
```

```txt
5! = 5 * 4 * 3 * 2 * 1 = 120
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

```txt
0! = 1
n! = n * (n - 1)!
```

Recursive functions: functions which call themselves

```py
def factorial(n):
  if n == 0:
    return 1

  return n * factorial(n - 1)

print(factorial(10)) # Prints 3628800
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

## Recursive Summation

```py
def summation(n):
  if n == 0:
    return 0

  return n + summation(n - 1)

print(summation(10)) # Prints 55
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

<!--
  **Tilings Generator**

  - `1` and `2` representation
  - _Practice worksheet_
  - _Problem_

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

  ## Tiles Proof

  ## Tail recursion
 -->
