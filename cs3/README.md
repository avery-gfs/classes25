**Fibonacci Generator**

[Problem](fibonacci/iterative/)

**Tilings Generator**

- `1` and `2` representation
- Generate tiling strings for length `4` manually

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

[Problem](tiles/iterative)

---

**Fibonacci Sequence**

https://en.wikipedia.org/wiki/Fibonacci_sequence

**Tilings proof**

```
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

**Make a programming quiz question**

- Can be true/false, multiple choice, or short response
- It must be an original question
- It must have a concrete, known answer
- Can ask about the Python language, CS theory, or general problem-solving
- Cannot involve third-party libraries

**Proving properties of systems**

- 12(3)4 proof
- Chessboard proof

---

**Maze do now**

**Class intro**

- Practice vs theory
- Programming vs CS
- Hard problems w/ easy solutions vs easy problems w/ hard solutions
- Maze demo
- Towers demo

**Grading policy**

- [Link](../shared/grading.md)

**Python setup**

- [Idle](https://www.python.org/downloads/)
- [VSCode](https://code.visualstudio.com/) +
  [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

**Install Python libraries**

- [Command](../shared/install-python-libraries)

**Review**

- Define a variable
- Make an empty list
- Make an infinite loop
- Print out `Hello <name>` based on the value in the variable `name`
- Get a name string from the user as input and print out `Hello <name>`
- Clear the console
- Check if a value is in a list
- Add a value to a list
- Remove a value from a list

**To do**

- [Problem](to-do)
