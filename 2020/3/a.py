from typing import List

import config


def count_trees(tree_map: List[str]) -> int:
    """Count trees (`#`) in the tree map.

    Args:
        tree_map (List[str]): a list of `.` and `#` (trees)

    Returns:
        int: number of trees

    """
    dx = 3
    count = 0
    for i, row in enumerate(tree_map[1:], start=1):
        index = (i * dx) % len(row)
        if row[index] == '#':
            count += 1

    return count


def main() -> None:
    """Determine path through a map of trees."""
    test_answer = 7
    file = config.TestFile(test_answer)
    count = count_trees(file.contents)
    file.test(count)

    file = config.File()
    count = count_trees(file.contents)
    print(count)


if __name__ == '__main__':
    main()
