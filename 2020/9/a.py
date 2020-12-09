from math import ceil
from typing import List

import config


def datum_is_sum(datum: str, preamble: List[str]) -> bool:
    """Iterate the preamble numbers and determine whether datum is a sum.

    Args:
        datum (str): a number that should be a sum of any two numbers
            in preamble
        preamble (List[str]): a list of preceeding n numbers where
            n is preamble_size in check_data_for_invalid()

    Returns:
        bool: True if the datum is a sum; False otherwise

    """
    preamble = [int(n) for n in preamble]
    for pre in preamble:
        diff = datum - pre
        # The difference must not be the same as the addend that produced it
        if diff == pre:
            continue
        elif diff in preamble:
            return True

    return False


def check_data_for_invalid(data: List[str], preamble_size: int = 25) -> int:
    """Check the data for a number with an invalid sum.

    Args:
        data (List[str]): data from the data port
        preamble_size (int; optional): the size of the preamble for data;
            defaults to 25

    Returns:
        int: the invalid number

    """
    for i, datum in enumerate(data[preamble_size:]):
        datum = int(datum)
        last_preamble = data[i:i + preamble_size]
        if not datum_is_sum(datum, last_preamble):
            return datum


def main() -> None:
    """Process port data."""
    test_answer = 127
    file = config.TestFile(test_answer)
    test = check_data_for_invalid(file.contents, preamble_size=5)
    file.test(test)

    file = config.File()
    result = check_data_for_invalid(file.contents)
    config.LOGGER.info(result)


if __name__ == '__main__':
    main()
