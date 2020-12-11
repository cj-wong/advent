from typing import List

import config


def datum_is_sum(datum: int, preamble: List[int]) -> bool:
    """Iterate the preamble numbers and determine whether datum is a sum.

    Args:
        datum (int): a number that should be a sum of any two numbers
            in preamble
        preamble (List[int]): a list of preceeding n numbers where
            n is preamble_size in check_data_for_invalid()

    Returns:
        bool: True if the datum is a sum; False otherwise

    """
    for pre in preamble:
        diff = datum - pre
        # The difference must not be the same as the addend that produced it
        if diff == pre:
            continue
        elif diff in preamble:
            return True

    return False


def check_data_for_invalid(data: List[int], preamble_size: int = 25) -> int:
    """Check the data for a number with an invalid sum.

    Args:
        data (List[int]): data from the data port
        preamble_size (int; optional): the size of the preamble for data;
            defaults to 25

    Returns:
        int: the invalid number

    """
    for i, datum in enumerate(data[preamble_size:]):
        last_preamble = data[i:i + preamble_size]
        if not datum_is_sum(datum, last_preamble):
            return datum


def get_range_sums_to_invalid(data: List[int], invalid: int) -> List[int]:
    """Get the range of consecutive numbers that add up to the invalid number.

    Args:
        data (List[int]): data from the data port
        invalid (int): the sum that doesn't add up from any of its prior 25

    Returns:
        List[int]: the range of integers

    """
    for i, datum in enumerate(data):
        s = [datum]
        while sum(s) < invalid:
            i += 1
            s.append(data[i])

        if sum(s) == invalid:
            return s


def main() -> None:
    """Process port data."""
    # Part A
    test_answer = 127
    file = config.TestFile(test_answer, to_type=int)
    test = check_data_for_invalid(file.contents, preamble_size=5)
    file.test(test)
    # Part B
    file.answer = 62
    test = get_range_sums_to_invalid(file.contents, test)
    test = min(test) + max(test)
    file.test(test)

    # Part A
    file = config.File(to_type=int)
    result = check_data_for_invalid(file.contents)
    config.log_part_info('A', result)
    # Part B
    result = get_range_sums_to_invalid(file.contents, result)
    result = min(result) + max(result)
    config.log_part_info('B', result)


if __name__ == '__main__':
    main()
