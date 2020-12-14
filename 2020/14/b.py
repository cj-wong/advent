import re
from collections import defaultdict
from more_itertools import grouper
from itertools import zip_longest
from typing import List

import config


MEM_RE = re.compile(r'mem\[([0-9]+)\] = ([0-9]+)')

BINS = List[int]


def remove_leading_zeroes(mask: BINS) -> BINS:
    """Remove leading zeroes from a mask.

    Args:
        mask (BINS): a zero- or one-only mask

    Returns:
        BINS: the mask, but with leading zeroes removed

    """
    for i, b in enumerate(mask):
        if b != 0:
            return mask[i:]


def add_leading_zeroes(value: BINS, n: int) -> BINS:
    """Add padding leading zeroes to a value to be written to memory.

    Args:
        value (BINS): the value to write to memory as a list of binary
        n (int): number of zeroes to pad

    Returns:
        BINS: the same value, but with appropriate leading zeroes

    """
    return [0] * n + value


def mask_values(mask: BINS, value: BINS, mask_n: int) -> BINS:
    """Mask values in reverse order (from least significant to most).

    Args:
        mask (BINS): the mask
        value (BINS): the value to mask
        mask_n (int): the value to mask over value

    Returns:
        BINS: value, but masked

    """
    value = [
        mask_n if m == 1 else v
        for m, v in zip_longest(mask[::-1], value[::-1])
        ]
    return value[::-1]


def mask_floating(floating_mask: BINS, address: BINS) -> List[BINS]:
    """Apply floating mask to address and get all possible addresses.

    Args:
        floating_mask (BINS): where 'X' is in the original mask
        address (BINS): an address to get multiple floating addresses

    Returns
        List[BINS]: a list of addresses from the address

    """
    floats = floating_mask.count(1)
    indices = list(range(2 ** floats))
    addresses = [[a for a in address] for _ in indices]

    count = 0

    for index, (f, a) in enumerate(
            zip_longest(floating_mask[::-1], address[::-1])):
        if f != 1:
            continue
        count += 1
        for group_n, subindices in enumerate(
                grouper(indices, len(indices) // (2 ** count))):
            for subindex in subindices:
                addresses[subindex][-index - 1] = group_n % 2

    return addresses


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
            floating = remove_leading_zeroes(
                [1 if c == 'X' else 0 for c in mask]
                )

            mask_len = 36 # This is hard-coded currently and may change
            # if this problem is used in a new context.

        else:
            address, value = [int(n) for n in MEM_RE.match(line).groups()]
            address = [int(a) for a in bin(address)[2:]]
            if len(address) < mask_len:
                address = add_leading_zeroes(address, mask_len - len(address))

            try:
                if 1 in ones:
                    address = mask_values(ones, address, 1)
            except TypeError:
                pass

            if 1 in floating:
                addresses = mask_floating(floating, address)

            for address in addresses:
                address = int(''.join([str(a) for a in address]), base=2)
                memory[address] = value

    return sum(memory.values())


def main() -> None:
    """Read program data from port computer system."""
    test_answer = 208
    file = config.TestFile(test_answer, path='test_input_b.txt')
    test = read_program_data(file.contents)
    file.test(test)

    file = config.File()
    result = read_program_data(file.contents)
    config.LOGGER.info(result)


if __name__ == '__main__':
    main()
