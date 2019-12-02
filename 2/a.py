from typing import List
from itertools import zip_longest

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


# Adapted from:
#   https://docs.python.org/3/library/itertools.html#itertools-recipes
def grouper(iterable):
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * 4
    return zip_longest(*args)


def run_ops(inputs: List[int]) -> None:
    """Runs the operations defined by `inputs`.
    If `inputs` is not defined, `INPUTS` will be used.

    Args:
        inputs (list): containing op codes;

    """
    for op, x, y, dest in grouper(inputs):
        if op == 99:
            print(inputs)
            return
        elif op == 1:
            inputs[dest] = inputs[x] + inputs[y]
        else:
            inputs[dest] = inputs[x] * inputs[y]
    print(inputs)


def main() -> None:
    """Processes inputs."""
    # with open('input', 'r') as f:
    #     run_ops([int(x) for x in f.read().split(',')])
    for i in INPUTS:
        run_ops(i)


if __name__ == '__main__':
    main()
