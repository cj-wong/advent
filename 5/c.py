"""Because parts a and b share almost the entire same constraints,
this file c.py represents a completion for the day in one file.

"""
import sys
from typing import List, Iterable
from itertools import zip_longest

import intcode


INPUTS = [
    # Output: 3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50
    [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50],
    # Output: 2, 0, 0, 0, 99
    [1, 0, 0, 0, 99],
    # Output: 2, 3, 0, 6, 99
    [2, 3, 0, 3, 99],
    # Output: 2, 4, 4, 5, 99, 9801
    [2, 4, 4, 5, 99, 0],
    # Output: 30, 1, 1, 4, 2, 5, 6, 0, 99
    [1, 1, 1, 4, 99, 5, 6, 0, 99]
    ]


def main() -> None:
    """Processes inputs."""
    with open('input', 'r') as f:
        intcode.Interpreter(f.read().split(',')).run_ops()
    # for i in INPUTS:
    #     intcode.Interpreter(i).run_ops()


if __name__ == '__main__':
    main()
