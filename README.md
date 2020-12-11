# *[Advent of Code][aoc]*: Personal Solutions

## Overview

These are my solutions for *[Advent of Code][aoc]*, done in Python 3.

## Repository Structure

- `YYYY` - year
    - `n` - day
        - `test_input.txt` -  if present, the test input given in the prompt
        - `input` or `input.txt` - if required, the input file to solve the prompt
        - `a.py` - first part
        - `b.py` - second part - may be a symlink to `a.py` if `a.py` contains both parts' solutions
        - `c.py` - [[1]](#note-1) possible rewrite
        - `config.py` - [[4]](#note-4) if present, a symlink to `../../common/config.py`
        - `module.py` - [[3]](#note-3) symbolic link to `../common/module.py`
    - `common` - [[2]](#note-2)
        - `module.py` - [[3]](#note-3)
- `common` - common utilities not specific to any
    - [config.py] - [[4]](#note-4) a file reader, test file tester, and other common utilities
- [prepare.sh] - a simple Bash script that can create skeleton files given a year (`$1`) and day (`$2`, can also be `"latest"`)

----

<a id="note-1">\[1\]</a> Generally after I have implemented a solution, I will try to write the code better, often by implementing a module and class interpretation of the solution. `a.py` and `b.py` are usually rewritten with modules kept in `common` in mind.

If the rewrite is universal between both parts, I may create a `c.py` that replaces functionality in both `a.py` and `b.py`. If `c.py` is present, both `a.py` and `b.py` are considered the originals. [^](#repository-structure)

<a id="note-2">\[2\]</a> The `common` directory is used for modules that may be shared between problems. For example, [2019/common](2019/common) contains modules with classes that may be reused, especially [intcode.py][intcode]. Necessary modules and their dependencies (if applicable) are linked to days that use them. [^](#repository-structure)

<a id="note-3">\[3\]</a> Depending on the needs of a problem, modules in `common` may either be subclassed or grow over time. In either case, modules remain backwards-compatible with earlier problems. [^](#repository-structure)

An example of a subclassed module:
- `Amplifier` in [amplifier.py] was the first subclassed module of `Interpreter` in [intcode.py]. `Amplifier` contains a different approach to solving a problem but uses the underlying *"Intcode"* interpreter.

An example of a growing module:
- Initially in [intcode.py], only `1`, `2`, and `99` were valid operators. Now, `1` through `9` inclusive with optional "parameters" and `99` are valid.

<a id="note-4">\[4\]</a> [config.py] is a general purpose utility module to be imported by solutions. It primarily features a file opener (and a subclass test file opener). The test file opener can also test input against the known answer (supplied in a prompt's description). Rather than manually create files, simply use the module. Use the [bare](common/a.py) file as a reference. [^](#repository-structure)

## Completion

### [2018](2018)

Stars: In Progress...?

### [2019](2019)

Stars: 29

### [2020](2020)

Stars: In Progress

## Disclaimer

This project is not affiliated with or endorsed by *[Advent of Code][aoc]*. See [LICENSE](LICENSE) for more detail.

[aoc]: https://adventofcode.com/
[intcode.py]: 2019/common/intcode.py
[amplifier.py]: 2019/common/amplifier.py
[config.py]: common/config.py
[prepare.sh]: prepare.sh
