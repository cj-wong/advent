import sys
from typing import List, Iterable
from itertools import zip_longest


JUMPS = {
    1: 4,
    2: 4,
    3: 2,
    4: 2,
    5: 3,
    6: 3,
    7: 4,
    8: 4,
    }


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
    print('op: 4,', inputs[index])


def get_params(opcode: int) -> List[int]:
    """Get params from an `opcode`.

    Args:
        opcode (int): the opcode to extract params

    Returns:
        list: of length 0-2

    """
    if opcode < 100:
        return []
    return [int(p) for p in str(opcode//100)]


def run_ops(inputs: List[int], jump: int = 0) -> None:
    """Runs the operations defined by `inputs`.
    If `inputs` is not defined, `INPUTS` will be used.

    Args:
        inputs (list): containing op codes

    """
    ops = []
    operands = []
    params = []
    # yay for arbitrary instruction lengths
    while True:
        op = inputs[jump]
        params = get_params(op)
        op %= 100

        if op == 99:
            print('op: 99,', inputs)
            return

        if op in [1, 2, 7, 8]:
            x, y, dest = inputs[jump+1:jump+4]
            if not params:
                x = inputs[x]
                y = inputs[y]
            elif len(params) == 2 and params[-1] == 0:
                x = inputs[x]
            elif len(params) == 1:
                y = inputs[y]
        elif op in [5, 6]:
            z, dest = inputs[jump+1:jump+3]
            if not params:
                z = inputs[z]
                dest = inputs[dest]
            elif len(params) == 2 and params[-1] == 0:
                z = inputs[z]
            elif len(params) == 1:
                dest = inputs[dest]

        if op == 1:
            inputs[dest] = x + y
        elif op == 2:
            inputs[dest] = x * y
        elif op == 3:
            store_input(inputs, inputs[jump+1])
        elif op == 4:
            if params:
                print('op: 4,', inputs[jump+1])
            else:
                show_at_index(inputs, inputs[jump+1])
        elif op == 5:
            if z != 0:
                return run_ops(inputs, dest)
        elif op == 6:
            if z == 0:
                return run_ops(inputs, dest)
        elif op == 7:
            inputs[dest] = 1 if x < y else 0
        else:
            inputs[dest] = 1 if x == y else 0

        jump += JUMPS[op]


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
