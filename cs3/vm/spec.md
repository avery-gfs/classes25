# gfssembly

A toy [assembly language](https://en.wikipedia.org/wiki/Assembly_language) for a
register-based
[virtual machine](https://rosettacode.org/wiki/Compiler/virtual_machine_interpreter),
made for use in CS 3.

## The VM has

- Four registers, which each hold a single integer, which are initialized to `0`
  at the start of the program.

- A fixed-length memory array (a list of numbers).

- An output stream, which can be used to log numbers or print characters.

All numbers in the VM are integers (division results are truncated).

## Instructions

- Instructions with a `rX` parameter store their result in the register `rX`,
  where `rX` is `r0`, `r1`, `r2`, or `r3` All other arguments can be register
  names or number literals.

- Comparison instructions produce a result of `0` if the comparison is false and
  `1` if the comparison is true.

- Logical instructions interpret arguments of `0` as false and arguments of any
  other value as true.

- Jumps are applied relative to the instruction position. Conditional jumps
  whose condition is false proceed to the next instruction.

### `add`

Format: `add rX n`

Action: Add `n` to `rX` and store the result in `rX`

Example: `add r2 r1`

|        |  r0 |  r1 |  r2 |  r3 | memory | output |
| ------ | --: | --: | --: | --: | ------ | ------ |
| before | `0` | `3` | `4` | `0` | `[]`   |        |
| after  | `0` | `3` | `7` | `0` | `[]`   |        |

Example: `add r2 8`

|        |  r0 |  r1 |   r2 |  r3 | memory | output |
| ------ | --: | --: | ---: | --: | ------ | ------ |
| before | `0` | `0` |  `4` | `0` | `[]`   |        |
| after  | `0` | `0` | `12` | `0` | `[]`   |        |

### `sub`

Format: `sub rX n`

Action: Subtract `n` from `rX` and store the result in `rX`

Example: `sub r2 r1`

|        |  r0 |  r1 |   r2 |  r3 | memory | output |
| ------ | --: | --: | ---: | --: | ------ | ------ |
| before | `0` | `7` |  `5` | `0` | `[]`   |        |
| after  | `0` | `7` | -`2` | `0` | `[]`   |        |

Example: `sub r2 3`

|        |  r0 |  r1 |  r2 |  r3 | memory | output |
| ------ | --: | --: | --: | --: | ------ | ------ |
| before | `0` | `0` | `5` | `0` | `[]`   |        |
| after  | `0` | `0` | `2` | `0` | `[]`   |        |

### `mul`

Format: `mul rX n`

Action: Multiply `rX` by `n` and store the result in `rX`

Example: `mul r2 r1`

|        |  r0 |  r1 |   r2 |  r3 | memory | output |
| ------ | --: | --: | ---: | --: | ------ | ------ |
| before | `0` | `3` |  `4` | `0` | `[]`   |        |
| after  | `0` | `3` | `12` | `0` | `[]`   |        |

Example: `mul r2 7`

|        |  r0 |  r1 |   r2 |  r3 | memory | output |
| ------ | --: | --: | ---: | --: | ------ | ------ |
| before | `0` | `0` |  `4` | `0` | `[]`   |        |
| after  | `0` | `0` | `28` | `0` | `[]`   |        |

### `div`

Format: `div rX n`

Action: Divide `rX` by `n` (truncating decimals) and store the result in `rX`

Example: `div r2 r1`

|        |  r0 |  r1 |   r2 |  r3 | memory | output |
| ------ | --: | --: | ---: | --: | ------ | ------ |
| before | `0` | `8` | `20` | `0` | `[]`   |        |
| after  | `0` | `8` |  `2` | `0` | `[]`   |        |

Example: `div r2 4`

|        |  r0 |  r1 |   r2 |  r3 | memory | output |
| ------ | --: | --: | ---: | --: | ------ | ------ |
| before | `0` | `0` | `20` | `0` | `[]`   |        |
| after  | `0` | `0` |  `5` | `0` | `[]`   |        |

### `mod`

Format: `mod rX n`

Action: Compute `rX` modulo `n` and store the result in `rX`

Example: `mod r2 r1`

|        |  r0 |  r1 |   r2 |  r3 | memory | output |
| ------ | --: | --: | ---: | --: | ------ | ------ |
| before | `0` | `7` | `20` | `0` | `[]`   |        |
| after  | `0` | `7` |  `6` | `0` | `[]`   |        |

Example: `mod r2 3`

|        |  r0 |  r1 |   r2 |  r3 | memory | output |
| ------ | --: | --: | ---: | --: | ------ | ------ |
| before | `0` | `0` | `20` | `0` | `[]`   |        |
| after  | `0` | `0` |  `2` | `0` | `[]`   |        |

### `eq`

Format: `eq rX n`

Action: Check if `rX` equals `n` and store the result in `rX`

Example: `eq r2 r1`

|        |  r0 |  r1 |   r2 |  r3 | memory | output |
| ------ | --: | --: | ---: | --: | ------ | ------ |
| before | `0` | `7` | `10` | `0` | `[]`   |        |
| after  | `0` | `7` |  `0` | `0` | `[]`   |        |

Example: `eq r2 5`

|        |  r0 |  r1 |  r2 |  r3 | memory | output |
| ------ | --: | --: | --: | --: | ------ | ------ |
| before | `0` | `0` | `5` | `0` | `[]`   |        |
| after  | `0` | `0` | `1` | `0` | `[]`   |        |

### `lt`

Format: `lt rX n`

Action: Check if `rX` is less than `n` and store the result in `rX`

Example: `lt r2 r1`

|        |  r0 |   r1 |   r2 |  r3 | memory | output |
| ------ | --: | ---: | ---: | --: | ------ | ------ |
| before | `0` | `17` | `10` | `0` | `[]`   |        |
| after  | `0` | `17` |  `1` | `0` | `[]`   |        |

Example: `lt r2 5`

|        |  r0 |  r1 |   r2 |  r3 | memory | output |
| ------ | --: | --: | ---: | --: | ------ | ------ |
| before | `0` | `0` | `10` | `0` | `[]`   |        |
| after  | `0` | `0` |  `0` | `0` | `[]`   |        |

### `gt`

Format: `gt rX n`

Action: Check if `rX` is greater than `n` and store the result in `rX`

Example: `gt r2 r1`

|        |  r0 |   r1 |   r2 |  r3 | memory | output |
| ------ | --: | ---: | ---: | --: | ------ | ------ |
| before | `0` | `17` | `10` | `0` | `[]`   |        |
| after  | `0` | `17` |  `0` | `0` | `[]`   |        |

Example: `gt r2 5`

|        |  r0 |  r1 |   r2 |  r3 | memory | output |
| ------ | --: | --: | ---: | --: | ------ | ------ |
| before | `0` | `0` | `10` | `0` | `[]`   |        |
| after  | `0` | `0` |  `1` | `0` | `[]`   |        |

### `and`

Format: `and rX alt`

Action: Compute logical 'and' of `rX` and `alt` and store the result in `rX`

Example: `and r2 r1`

|        |  r0 |  r1 |  r2 |  r3 | memory | output |
| ------ | --: | --: | --: | --: | ------ | ------ |
| before | `0` | `1` | `0` | `0` | `[]`   |        |
| after  | `0` | `1` | `0` | `0` | `[]`   |        |

### `or`

Format: `or rX alt`

Action: Compute logical 'or' of `rX` and `alt` and store the result in `rX`

Example: `or r2 r1`

|        |  r0 |  r1 |  r2 |  r3 | memory | output |
| ------ | --: | --: | --: | --: | ------ | ------ |
| before | `0` | `1` | `0` | `0` | `[]`   |        |
| after  | `0` | `1` | `1` | `0` | `[]`   |        |

### `not`

Format: `not rX`

Action: Compute logical 'not' of `rX` and store the result in `rX`

Example: `not r2`

|        |  r0 |  r1 |  r2 |  r3 | memory | output |
| ------ | --: | --: | --: | --: | ------ | ------ |
| before | `0` | `0` | `1` | `0` | `[]`   |        |
| after  | `0` | `0` | `0` | `0` | `[]`   |        |

### `jmp`

Format: `jmp n`

Action: Jump by `n` instructions

Example: `jmp n`

|        |  r0 |  r1 |  r2 |  r3 | memory | output |
| ------ | --: | --: | --: | --: | ------ | ------ |
| before | `0` | `0` | `0` | `0` | `[]`   |        |
| after  | `0` | `0` | `0` | `0` | `[]`   |        |

### `jeq`

Format: `jeq n a b`

Action: Jump by `n` instructions if `a` equals `b`

Example: `jeq n a b`

|        |  r0 |  r1 |  r2 |  r3 | memory | output |
| ------ | --: | --: | --: | --: | ------ | ------ |
| before | `0` | `0` | `0` | `0` | `[]`   |        |
| after  | `0` | `0` | `0` | `0` | `[]`   |        |

### `jne`

Format: `jne n a b`

Action: Jump by `n` instructions if `a` does not equal `b`

Example: `jne n a b`

|        |  r0 |  r1 |  r2 |  r3 | memory | output |
| ------ | --: | --: | --: | --: | ------ | ------ |
| before | `0` | `0` | `0` | `0` | `[]`   |        |
| after  | `0` | `0` | `0` | `0` | `[]`   |        |

### `halt`

Format: `halt`

Action: Stop program execution immediately

### `set`

Format: `set rX n`

Action: Set the value of `rX` to `n`

Example: `set r2 5`

|        |  r0 |  r1 |  r2 |  r3 | memory | output |
| ------ | --: | --: | --: | --: | ------ | ------ |
| before | `0` | `0` | `0` | `0` | `[]`   |        |
| after  | `0` | `0` | `5` | `0` | `[]`   |        |

Example: `set r2 r3`

|        |  r0 |  r1 |  r2 |  r3 | memory | output |
| ------ | --: | --: | --: | --: | ------ | ------ |
| before | `0` | `0` | `0` | `7` | `[]`   |        |
| after  | `0` | `0` | `7` | `7` | `[]`   |        |

### `log`

Format: `log n`

Action: Print `n` as a number on a new line

Example: `log r2`

|        |  r0 |  r1 |  r2 |  r3 | memory | output |
| ------ | --: | --: | --: | --: | ------ | ------ |
| before | `0` | `0` | `7` | `0` | `[]`   |        |
| after  | `0` | `0` | `7` | `0` | `[]`   | 7      |

Example: `log 10`

|        |  r0 |  r1 |  r2 |  r3 | memory | output |
| ------ | --: | --: | --: | --: | ------ | ------ |
| before | `0` | `0` | `0` | `0` | `[]`   |        |
| after  | `0` | `0` | `0` | `0` | `[]`   | 10     |

### `print`

Format: `print n`

Action: Print `n` as a character in the current line, converting to unicode

Example: `print r2`

|        |  r0 |  r1 |   r2 |  r3 | memory | output |
| ------ | --: | --: | ---: | --: | ------ | ------ |
| before | `0` | `0` | `97` | `0` | `[]`   |        |
| after  | `0` | `0` | `97` | `0` | `[]`   | a      |

Example: `print 64`

|        |  r0 |  r1 |  r2 |  r3 | memory | output |
| ------ | --: | --: | --: | --: | ------ | ------ |
| before | `0` | `0` | `0` | `0` | `[]`   | @      |
| after  | `0` | `0` | `0` | `0` | `[]`   |        |

### `load`

Format: `load rX index`

Action: Load the number at memory location `index` into `rX`

Example: `load r2 1`

|        |  r0 |  r1 |  r2 |  r3 | memory      | output |
| ------ | --: | --: | --: | --: | ----------- | ------ |
| before | `0` | `0` | `0` | `0` | `[4, 3, 0]` |        |
| after  | `0` | `0` | `3` | `0` | `[4, 3, 0]` |        |

Example: `load r2 r1`

|        |  r0 |  r1 |  r2 |  r3 | memory      | output |
| ------ | --: | --: | --: | --: | ----------- | ------ |
| before | `0` | `0` | `0` | `0` | `[4, 3, 0]` |        |
| after  | `0` | `0` | `4` | `0` | `[4, 3, 0]` |        |

### `store`

Format: `store src index`

Action: Store `src` in memory at location `index`

Example: `store 5 r0`

|        |  r0 |  r1 |  r2 |  r3 | memory      | output |
| ------ | --: | --: | --: | --: | ----------- | ------ |
| before | `1` | `0` | `0` | `0` | `[0, 0, 0]` |        |
| after  | `1` | `0` | `0` | `0` | `[0, 5, 0]` |        |

Example: `store r1 2`

|        |  r0 |  r1 |  r2 |  r3 | memory      | output |
| ------ | --: | --: | --: | --: | ----------- | ------ |
| before | `0` | `8` | `0` | `0` | `[0, 0, 0]` |        |
| after  | `0` | `8` | `0` | `0` | `[0, 0, 8]` |        |

### `mem`

Format: `mem values...`

Action: Set memory array to a given sequence of values

Example: `mem 1 1 2 3 5`

|        |  r0 |  r1 |  r2 |  r3 | memory            | output |
| ------ | --: | --: | --: | --: | ----------------- | ------ |
| before | `0` | `0` | `0` | `0` | `[]`              |        |
| after  | `0` | `0` | `0` | `0` | `[1, 1, 2, 3, 5]` |        |
