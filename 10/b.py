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
VAPORIZED = []

X, Y = (28, 29)


def vaporize(ast_map: List[str]) -> None:
    """Vaporize asteroids. TODO: should not calculate next asteroid
    by circling around only the perimeter. should account for those in-betweens
    as well, e.g. 1,30

    Args:
        ast_map (List[str]): the asteroid map

    """
    vaporized = 0
    height = len(ast_map)
    width = len(ast_map[0])
    x = X
    y = Y - 1
    diagonals = [
        (width - X) / -Y,
        (width - X) / (height - Y),
        -X / (height - Y),
        X / Y,
        ]
    diagonal = 0
    while True:
        x0, y0 = Vector(x - X, y - Y).to_tuple()
        x1 = x0 + X
        y1 = y0 + Y
        while x1 in range(width) and y1 in range(height):
            if ast_map[y1][x1] == '#' and (x1, y1) not in VAPORIZED:
                VAPORIZED.append((x1, y1))
                vaporized += 1
                if vaporized == 200:
                    print(f'200th: ({x1}, {y1}) {100 * x1 + y1}')
                    return
                break
            x1 += x0
            y1 += y0
        if x == X:
            if y1 < Y:
                x += 1
                diagonal = 0
            else:
                x -= 1
                diagonal = 2
        elif y == Y:
            if x1 < X:
                y -= 1
                diagonal = 3
            else:
                y += 1
                diagonal = 1
        else:
            d = diagonals[diagonal]
            if 




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

    # map_asteroids(a_map)
    # map_sights()
    vaporize(a_map)


if __name__ == '__main__':
    main()
