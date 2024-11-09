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

f = read_file('input.txt') | txt.split_by('\n\n') | map(txt.split_by('\n') | map(int) | sum()) | max()

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
  end)xD
  |> Enum.max()
  |> IO.puts()
```

### Modules

- algorithms
- combinators
- functions
- generators
- operators (op)
- regex (rgx)
- textual (txt)

### Features

- Clean interface (arguably)
- Functions piping
- Arguments binding
- Basic combinators

### References

- [Mastering Dyalog APL](https://www.dyalog.com/uploads/documents/MasteringDyalogAPL.pdf)
- [Learning APL](https://xpqz.github.io/learnapl/intro.html) and [APL Cultivations](https://xpqz.github.io/cultivations/Intro.html) by [Stefan Kruger](https://github.com/xpqz)
- [Elixir's pipe operator](https://elixirschool.com/en/lessons/basics/pipe_operator)
