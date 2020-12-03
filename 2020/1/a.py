from typing import List

import config


def search(numbers: List[str]) -> int:
    """Search for numbers that satisfy `2020 = x + y`.

    Args:
        numbers (List[str]): a list of numbers in string form

    Returns:
        int: the product of the number with its complement

    """
    SUM = 2020

    for number in numbers:
        num = int(number)
        diff = SUM - num
        if str(diff) in numbers:
            return num * diff


def main() -> int:
    """Read from file and check for two numbers.

    The two numbers when added together equal SUM (2020).

    Returns:
        int: 0 if successful; 1 otherwise

    """
    test_answer = 514579
    file = config.TestFile(test_answer)
    file.test(search(file.contents))

    file = config.File()
    product = search(file.contents)
    if product:
        config.LOGGER.info(product)
        return 0
    else:
        config.LOGGER.error('Could not find matching numbers.')
        return 1


if __name__ == '__main__':
    main()
