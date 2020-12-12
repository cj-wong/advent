import re
from typing import List

import config


DIRECTIONS = re.compile(r'(.)([0-9]+)')
CARDINAL = ['N', 'E', 'S', 'W']


def manhattan_distance(directions: List[str]) -> int:
    """Navigate given the supplied directions and get Manhattan-distance.

    Args:
        directions (List[str]): directions from the navigation system

    Returns:
        int: the absolute value of both top-bottom and left-right displacements

    """
    last_direction = 'E'
    x = 0
    y = 0
    for direction in directions:
        match = DIRECTIONS.match(direction)
        facing, distance = match.groups()
        distance = int(distance)

        if facing == 'F':
            if last_direction == 'N':
                y += distance
            elif last_direction == 'S':
                y -= distance
            elif last_direction == 'E':
                x += distance
            else:
                x -= distance
        elif facing in 'RL':
            if facing == 'L':
                c = -1
            else:
                c = 1

            offset = distance // 90
            last_index = CARDINAL.index(last_direction)
            last_direction = CARDINAL[(last_index + c * offset) % 4]
        else:
            if facing == 'N':
                y += distance
            elif facing == 'S':
                y -= distance
            elif facing == 'E':
                x += distance
            else:
                x -= distance

    print(x, y)
    return abs(x) + abs(y)


def main() -> None:
    """Navigate given the ship's directions."""
    test_answer = 25 # E 17, S 8
    file = config.TestFile(test_answer)
    test = manhattan_distance(file.contents)
    file.test(test)

    file = config.File()
    result = manhattan_distance(file.contents)
    config.LOGGER.info(result)


if __name__ == '__main__':
    main()
