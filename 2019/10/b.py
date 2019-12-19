import math
import sys
from collections import defaultdict
from typing import List, Tuple

import astronomy


INPUTS = [
    [ # Coordinate: (3, 4)
        '.#..#',
        '.....',
        '#####',
        '....#',
        '...##',
        ],
    ]


X, Y = (28, 29)


def main() -> None:
    """Processes inputs."""
    # for i in INPUTS:
    #     map_asteroids(i)
    #     map_sights()

    with open('input', 'r') as f:
        a_map = f.read().strip()

    a_map = astronomy.AsteroidField(a_map)
    center = a_map.asteroids[X, Y]
    center.map_seen(a_map)
    center.vaporize_until(a_map, 200)


if __name__ == '__main__':
    main()
