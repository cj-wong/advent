from typing import List


LOW = 284639
HIGH = 748759


def is_not_descending(digits: List[int]) -> bool:
    """Whether a number represented by `digits` has
    all digits not descending.

    Args:
        digits (list): the number as digits

    Returns:
        bool: True if the digits are not descending;
            False otherwise

    """
    prev = digits.pop(0)
    for digit in digits:
        if prev > digit:
            return False
        else:
            prev = digit
    return True


def has_adjacent_digits(digits: List[int]) -> bool:
    """Whether a number represented by `digits` has
    repeating digits.

    Args:
        digits (list): the number as digits

    Returns:
        bool: True if the number has repeating digits;
            False otherwise

    """
    last = digits.pop(0)
    for digit in digits:
        if digit == last:
            return True
        else:
            last = digit
    return False


def iterate_range() -> None:
    """Iterate from `LOW` to `HIGH` to find the number of valid codes."""
    valids = []
    for i in range(LOW, HIGH + 1):
        l = [int(x) for x in str(i)]
        if is_not_descending(l) and has_adjacent_digits(l):
            valids.append(i)

    print(len(valids))


if __name__ == '__main__':
    iterate_range()
