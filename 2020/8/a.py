import re
from typing import List

import config


OP_RE = re.compile(r'^(jm|no)p')


def replace_bad_op(instructions: List[str]) -> int:
    """Replace the bad op that causes infinite loop and get the accumulator.

    Args:
        instructions (List[str]): the game's instructions

    Returns:
        int: the accumulator value after replacing the bad op

    """
    # Record all indices where swapping is allowed.
    # In other words, every index in this list corresponds to either
    # 'jmp' or 'nop' operators.
    swap = [i for i, op in enumerate(instructions) if OP_RE.search(op)]

    while True:
        visited = set()
        step = 0
        acc = 0
        swapped = None
        while step not in visited:
            visited.add(step)
            # Because a valid program is considered when the instruction
            # pointer ends up out of bounds, check for IndexError for
            # the step against the whole instructions list.
            try:
                op, value = instructions[step].split(' ')
                if swapped == step or (swapped is None and step in swap):
                    op = 'jmp' if op == 'nop' else 'nop'
                    swapped = step
            except IndexError:
                return acc

            if op == 'nop':
                step += 1
            elif op == 'acc':
                step += 1
                acc += int(value)
            elif op == 'jmp':
                step += int(value)
            else:
                config.LOGGER.error(f'Unidentified op code: {op}')

        # if step > len(instructions):
        #     return acc

        # The loop exited without going out of bounds (and returning),
        # meaning that this was the wrong operation to swap. Remove it
        # so that next loop it won't be changed.
        swap.remove(swapped)


def iterate_instructions_once(instructions: List[str]) -> int:
    """Iterate through game instructions only once.

    Args:
        instructions (List[str]): the game's instructions

    Returns:
        int: the accumulator value before the infinite loop starts over

    """
    visited = set()
    step = 0
    acc = 0
    while step not in visited:
        visited.add(step)
        op, value = instructions[step].split(' ')
        if op == 'nop':
            step += 1
        elif op == 'acc':
            step += 1
            acc += int(value)
        elif op == 'jmp':
            step += int(value)
        else:
            config.LOGGER.error(f'Unidentified op code: {op}')

    return acc


def main() -> None:
    """Process game instructions."""
    # Part A
    test_answer = 5
    file = config.TestFile(test_answer)
    test = iterate_instructions_once(file.contents)
    file.test(test)

    file = config.File()
    result = iterate_instructions_once(file.contents)
    config.log_part_info('A', result)

    # Part B
    test_answer = 8
    file = config.TestFile(test_answer)
    test = replace_bad_op(file.contents)
    file.test(test)

    file = config.File()
    result = replace_bad_op(file.contents)
    config.log_part_info('B', result)


if __name__ == '__main__':
    main()
