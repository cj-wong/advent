# *[Advent of Code][aoc]*: Personal Solutions

## Overview

These are my solutions for *[Advent of Code][aoc]*, done in Python 3.

## Repository Structure

- `YYYY` - year
    - `n` - day
        - `input` - the input file if required
        - `a.py` - first part
        - `b.py` - second part
        - `c.py` - `[1]` possible rewrite
        - `module.py` - `[3]` symbolic link to `../common/module.py`
    - `common` - `[2]`
        - `module.py` - `[3]`

----

`[1]` Generally after I have implemented a solution, I will try to write the code better, often by implementing a module and class interpretation of the solution. `a.py` and `b.py` are usually rewritten with modules kept in `common` in mind.

If the rewrite is universal between both parts, I may create a `c.py` that replaces functionality in both `a.py` and `b.py`. If `c.py` is present, both `a.py` and `b.py` are considered the originals.

`[2]` The `common` directory is used for modules that may be shared between problems. For example, [`2019/common`](2019/common) contains modules with classes that may be reused, especially [`intcode.py`][intcode]. Necessary modules and their dependencies (if applicable) are linked to days that use them.

`[3]` Depending on the needs of a problem, modules in `common` may either be subclassed or grow over time. In either case, modules remain backwards-compatible with earlier problems.

An example of a subclassed module:
- `Amplifier` in [`amplifier.py`](2019/common/amplifier.py) was the first subclassed module of `Interpreter` in [`intcode.py`][intcode]. `Amplifier` contains a different approach to solving a problem but uses the underlying *"Intcode"* interpreter.

An example of a growing module:
- Initially in [`intcode.py`][intcode], only `1`, `2`, and `99` were valid operators. Now, `1` through `9` inclusive with optional "parameters" and `99` are valid.

## Completion

### [2018](2018)

Day          | Stars
------------ | -----
[1](2018/1)  | 2
[2](2018/2)  | 2
[3](2018/3)  | 1

### [2019](2019)

In progress

## Disclaimer

This project is not affiliated with or endorsed by *[Advent of Code][aoc]*. See [`LICENSE`](LICENSE) for more detail.

[aoc]: https://adventofcode.com/
[intcode]: 2019/common/intcode.py
