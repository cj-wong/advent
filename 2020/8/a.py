from typing import List

import config


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
    test_answer = 5
    file = config.TestFile(test_answer)
    test = iterate_instructions_once(file.contents)
    file.test(test)

    file = config.File()
    result = iterate_instructions_once(file.contents)
    config.LOGGER.info(result)


if __name__ == '__main__':
    main()
