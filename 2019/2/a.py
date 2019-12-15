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

STATE = [
    (1, 12),
    (2, 2)
    ]


def main() -> None:
    """Processes inputs."""
    # for i in INPUTS:
    #     intcode.Interpreter(i).run_ops()

    with open('input', 'r') as f:
        interpreter = intcode.Interpreter(f.read().split(','))
        for index, value in STATE:
            interpreter.store_input(index, value)
        interpreter.run_ops()
        print(interpreter.ops[0])


if __name__ == '__main__':
    main()
