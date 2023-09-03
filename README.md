# advent

Simple functional Python library designed for learning and problem solving purposes inspired by APL and Elixir programming languages.

Created mainly for solving [Advent of Code](https://adventofcode.com/) challenges - hence the name `advent`.

### Motivation

While Python is a very versatile and powerful programming language it lacks functional approach found in other languages.

For better demonstration let's look at the puzzle [Calorie Counting](https://adventofcode.com/2022/day/1) from day 1 of Advent of Code 2022.

###### Regular Python with loops
```python
with open('input.txt') as file:
    content = file.read()
    biggest = 0
    for chunk in content.split('\n\n'):
        total = 0
        for line in chunk.split('\n'):
            n = int(line)
            total += n
        if total > biggest:
            biggest = total
    print(biggest)
```

###### More functional oriented Python
```python
with open('input.txt') as file:
    content = file.read()
    parsed = (map(int, line.split('\n')) for line in content.split('\n\n'))
    solution = max(map(sum, parsed))
    print(solution)
```

###### Python with advent
```python
from advent import *

f = read_file('input.txt') | split('\n\n') | map(split('\n') | map(int) | sum()) | max()

print(f())
```

###### Elixir solution for comparision
```elixir
File.read!("input.txt")
  |> String.split("\n\n")
  |> Stream.map(fn line ->
    line
    |> String.split("\n")
    |> Stream.map(&String.to_integer/1)
    |> Enum.sum()
  end)
  |> Enum.max()
  |> IO.puts()
```

### Modules

- Combinators (cb) - creating new functions from existing ones (composition)
- Functions (fn) - operations on ranges
- Generators (gn) - data generation from various sources (e.g. ranges, files)
- Operators (op) - operations on scalars
- Text Modifiers (txt) - easier working with strings

### Features

- Clean interface (arguably)
- Functions piping
- Arguments binding
- Basic combinators

### Some examples

###### Sum of comma separated integers from string

```python
f = txt.split(',') | fn.map(int) | fn.sum()

f('1,2,3,4,5,6') # 21
```

###### Filtering out integers not divisible by 7

```python
f = fn.filter(lambda x: x % 7 == 0) | fn.to(list)

f([ 0, 4, 7, 12, 14, 49 ]) # [ 0, 7, 14, 49 ]
```

###### Multiply number by 2

```python
f = op.mul >> 2

f(1) # 2
f(5) # 10
```

###### Reciprocal of the number

```python
f = op.div << 1

f(2) # 0.5
f(5) # 0.2
```

###### Find how many numbers are larger than the previous ones

```python
f = fn.sliding_reduce(2, op.lt) | fn.sum()

f([ 1, 2, 1, 3, 4, 4, 5 ]) # 4
f([ 3, 2, 1, 0, 0, 1 ]) # 1
```

###### Check if array contains only unique elements

```python
f = cb.train(fn.distinct() | fn.tally(), op.eq, fn.tally())

f([ 1, 2, 3, 4, 5, 6 ]) # True
f([ 0, 55, 1, 8, 55, 4 ]) # False
```

### References

- [Mastering Dyalog APL](https://www.dyalog.com/uploads/documents/MasteringDyalogAPL.pdf)
- [Learning APL](https://xpqz.github.io/learnapl/intro.html) and [APL Cultivations](https://xpqz.github.io/cultivations/Intro.html) by [Stefan Kruger](https://github.com/xpqz)
- [Elixir's pipe operator](https://elixirschool.com/en/lessons/basics/pipe_operator)
