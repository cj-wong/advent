from collections import defaultdict
from typing import List

import config


OUTLET = 0
LOWEST = 1
HIGHEST = 3


def calculate_tree_diffs(joltages: List[int]) -> None:
    """Calculate tree containing ways to chain adapters.

    Args:
        joltages (List[int]): the joltages of the adapters on hand

    """
    # Add the starting (outlet) joltage.
    joltages.append(OUTLET)

    branches = defaultdict(int)

    # Initialize the branches for the first joltages.
    branches[OUTLET] = 1
    branches[1] = 1

    for joltage in joltages[1:]:
        for diff in range(LOWEST, HIGHEST + 1):
            prev = joltage - diff
            branches[joltage] += branches[prev]

    return max(branches.values())


def main() -> None:
    """Check joltages of the adapters from the outlet to device."""
    test_answer = 8
    file = config.TestFile(test_answer, to_type=int, sort=True)
    test = calculate_tree_diffs(file.contents)
    file.test(test)

    test_answer = 19208
    file = config.TestFile(
        test_answer, path="another_test_input.txt", to_type=int, sort=True)
    file.write_to_file()
    test = calculate_tree_diffs(file.contents)
    file.test(test)

    file = config.File(to_type=int, sort=True)
    result = calculate_tree_diffs(file.contents)
    config.LOGGER.info(result)


if __name__ == '__main__':
    main()
