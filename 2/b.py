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

END = 19690720


def main() -> None:
    """Processes inputs."""
    # for i in INPUTS:
    #     run_ops(i)
    with open('input', 'r') as f:
        ops = f.read().split(',')
    bounds = len(ops)
    interpreter = intcode.Interpreter(ops)
    interpreter.save_state()
    for x in range(bounds):
        for y in range(bounds):
            for index, value in enumerate([x, y], start=1):
                interpreter.store_input(index, value)
            interpreter.run_ops(silent=True)
            if interpreter.ops[0] == END:
                print(
                    f'Solution found: x = {x}, y = {y}, answer =',
                    100 * x + y
                    )
                return
            interpreter.restore_state()


if __name__ == '__main__':
    main()
