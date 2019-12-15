import sys
from typing import List, Iterable
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
def grouper(iterable) -> Iterable:
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * 2
    return zip_longest(*args)


def store_input(inputs: List[int], index: int) -> None:
    """Store an integer from stdin into `inputs[index]`.

    Args:
        inputs (list): containing op codes
        index (int): where the stdin input goes

    """
    inputs[index] = int(sys.argv[1])


def show_at_index(inputs: List[int], index: int) -> None:
    """Shows what's stored in `inputs[index]`.

    Args:
        inputs (list): containing op codes
        index (int): where the stdin input goes

    """
    print('op: 4, ', inputs[index])


IO = {
    3: store_input,
    4: show_at_index
    }


def run_ops(inputs: List[int]) -> None:
    """Runs the operations defined by `inputs`.
    If `inputs` is not defined, `INPUTS` will be used.

    Args:
        inputs (list): containing op codes

    """
    ops = []
    operands = []
    params = []
    for op, operand in grouper(inputs):
        if ops:
            if not params or params[-1] == 0:
                op = inputs[op]
            if 1 in ops:
                inputs[operand] = operands[0] + op
            else: # 2 in ops
                inputs[operand] = operands[0] * op
            ops = []
            operands = []
            params = []
        else:
            if op == 99:
                print('op:', op, ' ', inputs)
                return

            if op > 99:
                params.extend([int(p) for p in str(op//100)])
                op = op % 100
                if params[-1] == 1:
                    ioperand = operand
                else:
                    ioperand = inputs[operand]
                params = params[:-1]
            else:
                params = []
                ioperand = inputs[operand]

            if op in [1, 2]:
                ops.append(op)
                operands.append(ioperand)
            elif op == 4 and len(params) == 3:
                print('op: 4, ',ioperand)
            else: # op == 3 or op == 4
                IO[op](inputs, operand)

    print('Warning: opcode 99 was not detected.')
    print(inputs)


def main() -> None:
    """Processes inputs."""
    with open('input', 'r') as f:
        run_ops([int(x) for x in f.read().split(',')])
    # for i in INPUTS:
    #     run_ops(i)


if __name__ == '__main__':
    main()
