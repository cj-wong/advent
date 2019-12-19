# *[Advent of Code][aoc]*: Personal Solutions

## Overview

These are my solutions for *[Advent of Code][aoc]*, done in Python 3. Currently, I only have **[2019](2019)** available. **[2018](2018)** is incomplete but will be eventually attempted.

## Repository Structure

- `YYYY` - year
    - `n` - day
        - `input` - the input file if required
        - `a.py` - first part
        - `b.py` - second part
        - `c.py` - *see note below*
    - `common` - *see note below*

Generally after I have implemented a solution, I will try to write the code better, often by implementing a module and class interpretation of the solution. `a.py` and `b.py` are usually rewritten with modules kept in `common` in mind.

If the rewrite is universal between both parts, I may create a `c.py` that replaces functionality in both `a.py` and `b.py`. If `c.py` is present, both `a.py` and `b.py` are considered the originals.

The `common` directory is used for modules that may be shared between problems. For example, [`2019/common`](2019/common) contains modules with classes that may be reused, especially [`intcode.py`][intcode]. Necessary modules and theirs dependencies (if applicable) are linked to days that use them.

Depending on the needs of a problem, modules in `common` may either be subclassed (e.g. [`amplifier.py`](2019/common/amplifier.py) contains the first subclassed module of `Interpreter` in [`intcode.py`][intcode]) or grow over time (e.g. more operators added to [`intcode.py`][intcode]). In either case, modules remain backwards-compatible with earlier problems.

## Completion

### [2018](2018)

Day          | Stars
------------ | -----
[1](2018/1)  | 2/2
[2](2018/2)  | 2/2
[3](2018/3)  | 1/2

### [2019](2019)

In progress

## Disclaimer

This project is not affiliated with or endorsed by *[Advent of Code][aoc]*. See [`LICENSE`](LICENSE) for more detail.

[aoc]: https://adventofcode.com/
[intcode]: 2019/common/intcode.py
