import math
from collections import defaultdict
from typing import List, Tuple

import astronomy


INPUTS = [
    # Coordinate: (3, 4)
    '.#..#\n.....\n#####\n....#\n...##'
    ]

OUTPUTS = [
    '(3, 4)',
    ]


def main() -> None:
    """Processes inputs."""
    # for i, o in zip(INPUTS, OUTPUTS):
    #     a_map = astronomy.AsteroidField(i)
    #     m = 0
    #     co = None
    #     for (x, y), asteroid in a_map.asteroids.items():
    #         asteroid.map_seen(a_map)
    #         if len(asteroid.seen) > m:
    #             m = len(asteroid.seen)
    #             co = (x, y)
    #     print(f'Maximum sighted: {m} at {co}',)
    #     print('Expected output:', o)

    with open('input', 'r') as f:
        a_map = f.read().strip()
    m = 0
    co = None
    a_map = astronomy.AsteroidField(a_map)
    for (x, y), asteroid in a_map.asteroids.items():
        asteroid.map_seen(a_map)
        if len(asteroid.seen) > m:
            m = len(asteroid.seen)
            co = (x, y)
    print(f'Maximum sighted: {m} at {co}',)


if __name__ == '__main__':
    main()
