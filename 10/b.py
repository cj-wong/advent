import math
import sys
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
VAPORIZED = []

X, Y = (28, 29)


LINE_OF_SIGHT = []


def map_asteroids(ast_map: List[str]) -> None:
    """Map asteroids given an `ast_map`.

    Args:
        ast_map (List[str]): the asteroid map

    """
    for y, row in enumerate(ast_map):
        for x, char in enumerate(row):
            if char == '#':
                ASTEROIDS[(x, y)] = '#'


def map_sights() -> List[Tuple[int]]:
    """Map asteroids in sight.

    Returns:
        List[Tuple[int]]: a list of coordinates of seen asteroids

    """
    for (x, y) in ASTEROIDS:
        if x == X and y == Y:
            continue
        f = Vector(x - X, y - Y).to_tuple()
        for line, (x0, y0) in LINE_OF_SIGHT:
            if line == f:
                if abs(x) < abs(x0) or abs(y) < abs(y0):
                    LINE_OF_SIGHT.remove((line, (x0, y0)))
                    LINE_OF_SIGHT.append((f, (x, y)))
                break
        LINE_OF_SIGHT.append((f, (x, y)))

    return [(x, y) for _, (x, y) in LINE_OF_SIGHT]


def count_vaporized(n: int, quadrant: List[Tuple[int]]) -> int:
    """Count vaporized asteroids and if `n` is greater than or equal to
    200, sort the `quadrant` and output the 200th.

    Args:
        n (int): the current number of vaporized asteroids
        quadrant (List[Tuple[int]]): list of coordinates in a quadrant

    Returns:
        int: `n`, after processing `quadrant`

    """
    if n >= 200 - len(quadrant):
        print(
            sorted(
                [((x, y), math.atan2(y - Y, x - X)) for (x, y) in quadrant],
                key=lambda r: r[1],
                )[199 - n]
            )
        sys.exit(0)
    return n + len(quadrant)


def vaporize(seen: List[Tuple[int]]) -> None:
    """Vaporize seen asteroids.

    Args:
        seen (List[Tuple[int]]): a list of seen asteroids' coordinates

    """
    records = []
    n = 0
    q1 = [(x, y) for (x, y) in seen if x >= X and y >= Y]
    n = count_vaporized(n, q1)
    # Not the mathematical q2. Because the "sweeping" arm rotates
    # clockwise, the mathematical q4 is the second quadrant to be
    # reached. Likewise for below q's.
    q2 = [(x, y) for (x, y) in seen if x >= X and y < Y]
    n = count_vaporized(n, q2)
    q3 = [(x, y) for (x, y) in seen if x < X and y < Y]
    n = count_vaporized(n, q3)
    q4 = [(x, y) for (x, y) in seen if x < X and y >= Y]
    n = count_vaporized(n, q4)


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
            self.x = x // gcd
            self.y = y // gcd

    def to_tuple(self) -> Tuple[int, int]:
        """Create a tuple representation of the vector."""
        return (self.x, self.y)


def main() -> None:
    """Processes inputs."""
    # for i in INPUTS:
    #     map_asteroids(i)
    #     map_sights()

    with open('input', 'r') as f:
        a_map = f.read().strip().split('\n')

    map_asteroids(a_map)
    seen = map_sights()
    #print(len(seen))
    vaporize(seen)


if __name__ == '__main__':
    main()
