import re
from collections import defaultdict
from itertools import zip_longest
from typing import List

import config


MEM_RE = re.compile(r'mem\[([0-9]+)\] = ([0-9]+)')


def remove_leading_zeroes(mask: List[int]) -> List[int]:
    """Remove leading zeroes from a mask.

    Args:
        mask (List[int]): a zero- or one-only mask

    Returns:
        List[int]: the mask, but with leading zeroes removed

    """
    for i, b in enumerate(mask):
        if b != 0:
            return mask[i:]


def add_leading_zeroes(value: List[int], n: int) -> List[int]:
    """Add padding leading zeroes to a value to be written to memory.

    Args:
        value (List[int]): the value to write to memory as a list of binary
        n (int): number of zeroes to pad

    Returns:
        List[int]: the same value, but with appropriate leading zeroes

    """
    return [0] * n + value


def mask_values(mask: List[int], value: List[int], mask_n: int) -> List[int]:
    """Mask values in reverse order (from least significant to most).

    Args:
        mask (List[int]): the mask
        value (List[int]): the value to mask
        mask_n (int): the value to mask over value

    Returns:
        List[int]: value, but masked

    """
    value = [
        mask_n if m == 1 else v
        for addr, (m, v) in enumerate(
            zip_longest(mask[::-1], value[::-1]))
        ]
    return value[::-1]


def read_program_data(program: List[str]) -> int:
    """Read program data from port computer system.

    Args:
        program (List[str]): the program code containing masks and memory

    Returns:
        int: sum of all values in memory

    """
    memory = defaultdict(int)
    for line in program:
        if line.startswith('mask'):
            _, mask = line.split(' = ')
            ones = remove_leading_zeroes(
                [1 if c == '1' else 0 for c in mask]
                )
            zeroes = remove_leading_zeroes(
                [1 if c == '0' else 0 for c in mask]
                )
            mask_len = max(len(ones), len(zeroes))
        else:
            address, value = [int(n) for n in MEM_RE.match(line).groups()]
            value = [int(b) for b in bin(value)[2:]]
            if len(value) < mask_len:
                value = add_leading_zeroes(value, mask_len - len(value))
            if 1 in ones:
                value = mask_values(ones, value, 1)
            if 1 in zeroes:
                value = mask_values(zeroes, value, 0)
            memory[address] = int(''.join(str(b) for b in value), base=2)
    return sum(memory.values())


def main() -> None:
    """Read program data from port computer system."""
    test_answer = 165
    file = config.TestFile(test_answer)
    test = read_program_data(file.contents)
    file.test(test)

    file = config.File()
    result = read_program_data(file.contents)
    config.LOGGER.info(result)


if __name__ == '__main__':
    main()
