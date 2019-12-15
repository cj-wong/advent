import math
from collections import defaultdict
from typing import List, Tuple


INPUTS = [
    [ # Coordinate: (3, 4)
        '.#..#',
        '.....',
        '#####',
        '....#',
        '...##',
        ],
    ]


ASTEROIDS = defaultdict(str)
LINE_OF_SIGHT = defaultdict(list)


def map_asteroids(ast_map: List[str]) -> None:
    """Map asteroids given an `ast_map`.

    Args:
        ast_map (List[str]): the asteroid map

    """
    for y, row in enumerate(ast_map):
        for x, char in enumerate(row):
            if char == '#':
                ASTEROIDS[(x, y)] = '#'


def map_sights() -> None:
    """Map asteroids in sight."""
    for (x, y) in ASTEROIDS:
        for (x0, y0) in ASTEROIDS:
            if x == x0 and y == y0:
                continue
            f = Vector(x - x0, y - y0).to_tuple()
            if not [line for line in LINE_OF_SIGHT[(x, y)] if line == f]:
                LINE_OF_SIGHT[(x, y)].append(f)

    print(max([len(lines) for lines in LINE_OF_SIGHT.values()]))


class Vector:
    """A 2D vector."""
    def __init__(self, x: int, y: int) -> None:
        """Initialize the vector using both axes. Tries to reduce
        the vector if possible.

        Args:
            x (int): the x-axis offset
            y (int): the y-axis offset

        """
        if x == 0:
            self.x = x
            if y > 0:
                self.y = 1
            else:
                self.y = -1
        elif y == 0:
            self.y = y
            if x > 0:
                self.x = 1
            else:
                self.x = -1
        else:
            gcd = math.gcd(x, y)
            self.x = x / gcd
            self.y = y / gcd

    def to_tuple(self) -> Tuple[int, int]:
        """Create a tuple representation of the vector."""
        return (self.x, self.y)


def main() -> None:
    """Processes inputs."""
    # for i in INPUTS:
    #     map_asteroids(i)
    #     map_sights()
    #     print('Expected output:', '(3, 4)')

    with open('input', 'r') as f:
        a_map = f.read().strip().split('\n')

    map_asteroids(a_map)
    map_sights()


if __name__ == '__main__':
    main()
