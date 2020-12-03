from typing import List

import config


def search(numbers: List[str]) -> int:
    """Search for numbers that satisfy `2020 = x + y + z`.

    x = num
    y = num2
    z = diff2
    diff = y + z

    Args:
        numbers (List[str]): a list of numbers in string form

    Returns:
        int: the product of the number with its complement

    """
    SUM = 2020

    for i, number in enumerate(numbers):
        num = int(number)
        diff = SUM - num
        for j, second in enumerate(numbers[i:]):
            num2 = int(second)
            diff2 = diff - num2
            if str(diff2) in numbers[j:]:
                return num * num2 * diff2


def main() -> int:
    """Read from file and check for three numbers.

    The three numbers when added together equal SUM (2020).

    Returns:
        int: 0 if successful; 1 otherwise

    """
    test_answer = 241861950
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
