import re
from typing import List

import config


DIRECTIONS = re.compile(r'(.)([0-9]+)')
CARDINAL = ['N', 'E', 'S', 'W']


def manhattan_distance(directions: List[str]) -> int:
    """Navigate given the supplied directions and get Manhattan-distance.

    Unlike a.py, a secondary set of coordinates will be recorded, because
    most of the revised directions use this second set.

    Args:
        directions (List[str]): directions from the navigation system

    Returns:
        int: the absolute value of both top-bottom and left-right displacements

    """
    x = 0
    y = 0
    # Waypoint relative coordinates
    rx = 10
    ry = 1
    for direction in directions:
        match = DIRECTIONS.match(direction)
        facing, distance = match.groups()
        distance = int(distance)

        if facing == 'F':
            x += distance * rx
            y += distance * ry
        # Note that unlike a.py, this conditional is an `elif`, not `if`!
        elif facing in 'RL':
            if ((facing == 'R' and distance == 90)
                    or (facing == 'L' and distance == 270)):
                rx, ry = ry, -rx
            elif ((facing == 'R' and distance == 270)
                    or (facing == 'L' and distance == 90)):
                rx, ry = -ry, rx
            else: # distance == 180
                rx, ry = -rx, -ry
        else:
            if facing == 'N':
                ry += distance
            elif facing == 'S':
                ry -= distance
            elif facing == 'E':
                rx += distance
            else:
                rx -= distance

    return abs(x) + abs(y)


def main() -> None:
    """Navigate given the ship's directions."""
    test_answer = 286 # E 214, S 72
    file = config.TestFile(test_answer)
    test = manhattan_distance(file.contents)
    file.test(test)

    file = config.File()
    result = manhattan_distance(file.contents)
    config.LOGGER.info(result)


if __name__ == '__main__':
    main()
