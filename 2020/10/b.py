from typing import List

import config


LOWEST = 1
HIGHEST = 3


# def calculate_tree_diffs(joltages: List[int]) -> None:
#     """Calculate tree containing ways to chain adapters.

#     Args:
#         joltages (List[int]): the joltages of the adapters on hand

#     """
#     lowest = 1
#     highest = 3
#     # Add both the starting (outlet) and ending (device) joltages.
#     joltages.append(0)
#     # joltages.append(device_joltage)
#     joltages = sorted(joltages)
#     # The greatest joltage is always present in tree-mapping, so it can be
#     # safely removed from calculations.
#     joltages.pop()

#     penultimate_joltage = joltages[-1]

#     joltage = 0
#     branches = 1
#     while joltage < penultimate_joltage:
#         next_joltages = [
#             (joltage + c)
#             for c in range(lowest, highest + 1)
#             if (joltage + c) in joltages
#             ]
#         branches *= 2 ** (len(next_joltages) - 1)
#         joltage = max(next_joltages)

#     return branches


def calculate_tree_diffs(joltages: List[int]) -> int:
    """Calculate number of branches in tree of adapter choices.

    Args:
        joltages (List[int]): the joltages of the adapters on hand; sorted

    Returns:
        int: number of branches

    """
    config.LOGGER.debug(f'{joltages[0]}')
    sub_branches = 0
    # Stop at the last element.
    if len(joltages) == 1:
        return 1

    joltage = joltages[0]
    next_joltages = [
        c
        for c in range(LOWEST, HIGHEST + 1)
        if (joltage + c) in joltages
        ]

    for n in next_joltages:
        i = joltages.index(n + joltage)
        sub_branches += calculate_tree_diffs(joltages[i:])

    return sub_branches


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
    print(test)
    file.test(test)

    file = config.File()
    file.contents_to_type(int)
    # result = calculate_tree_diffs(file.contents)
    # config.LOGGER.info(result)


if __name__ == '__main__':
    main()
