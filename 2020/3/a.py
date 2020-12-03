from typing import List

import config


# This file contains the solution for both parts of 2020-12-03.


def count_trees(tree_map: List[str], dx: int, dy: int) -> int:
    """Count trees (`#`) in the tree map.

    Args:
        tree_map (List[str]): a list of `.` and `#` (trees)

    Returns:
        int: number of trees

    """
    count = 0
    for i, row in enumerate(tree_map[::dy]):
        if i == 0:
            continue
        index = (i * dx) % len(row)
        if row[index] == '#':
            count += 1

    return count


def main() -> None:
    """Determine path through a map of trees."""
    # Part A
    test_answer = 7
    file = config.TestFile(test_answer)
    count = count_trees(file.contents, 3, 1)
    file.test(count)

    # Part B
    test_answer = 336 # = 2 * 7 * 3 * 4 * 2
    file = config.TestFile(test_answer)
    slopes = [
        (1, 1),
        # (3, 1), # This slope is already calculated.
        # Rather than calculate the count again, just multiply results from
        # the other slopes onto the existing count.
        (5, 1),
        (7, 1),
        (1, 2),
        ]
    for slope in slopes:
        count *= count_trees(file.contents, *slope)
    file.test(count)

    # Part A
    file = config.File()
    count = count_trees(file.contents, 3, 1)
    config.LOGGER.info(f'A: {count}')
    for slope in slopes:
        count *= count_trees(file.contents, *slope)
    config.LOGGER.info(f'B: {count}')


if __name__ == '__main__':
    main()
