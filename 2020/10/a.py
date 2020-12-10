from typing import List

import config


def calculate_diff_occurrence(joltages: List[int]) -> int:
    """Calculate diff occurrences for differences of 1 and 3.

    Args:
        joltages (List[int]): the joltages of the adapters on hand

    Returns:
        int: the product of numbers of diff of 1 and diff of 3

    """
    lowest = 1
    highest = 3
    device_joltage = max(joltages) + highest
    # Add both the starting (outlet) and ending (device) joltages.
    joltages.append(0)
    joltages.append(device_joltage)
    joltages = sorted(joltages)
    diffs = [
        joltages[i + 1] - joltage for i, joltage in enumerate(joltages[:-1])
        ]
    diffs = {diff: diffs.count(diff) for diff in range(lowest, highest + 1)}
    return diffs[lowest] * diffs[highest]


def main() -> None:
    """Check joltages of the adapters from the outlet to device."""
    test_answer = 35
    file = config.TestFile(test_answer)
    file.contents_to_type(int)
    test = calculate_diff_occurrence(file.contents)
    file.test(test)

    test_answer = 220
    file = config.TestFile(test_answer, path="another_test_input.txt")
    file.contents_to_type(int)
    test = calculate_diff_occurrence(file.contents)
    file.test(test)

    file = config.File()
    file.contents_to_type(int)
    result = calculate_diff_occurrence(file.contents)
    config.LOGGER.info(result)


if __name__ == '__main__':
    main()
