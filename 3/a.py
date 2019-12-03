from collections import defaultdict
from typing import Dict, List, Tuple


INPUTS = [
    [   # Distance: 159
        ('R75','D30','R83','U83','L12','D49','R71','U7','L72'),
        ('U62','R66','U55','R34','D71','R55','D58','R83')
        ],
    [   # Distance: 135
        ('R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'),
        ('U98','R91','D20','R16','D67','R40','U7','R15','U6','R7')
        ]
    ]


def insert_nums(
    m: defaultdict, coord: List[int], rows: int, index: int
    ) -> None:
    """Insert nums into `m`. If `is_x`, insert horizontally. Else,
    insert vertically.

    Args:
        m (defaultdict): the coordinate system
        coord (list): the current coordinates
        rows (int): can be positive or negative; how many rows (y-axis)
            to add
        index (int): indicates which index to modify; 0 = x-axis, 1 = y-axis

    """
    offset = 1 if rows > 0 else -1
    for i in range(coord[index], coord[index] + rows, offset):
        if index == 0:
            m[(i + offset, coord[1])] += 1
        else:
            m[(coord[0], i + offset)] += 1
    coord[index] += rows


def generate_map(inputs: List[Tuple[str]]) -> Dict[Tuple[int, int], int]:
    """Creates a map representing `inputs` directions.

    Args:
        inputs (list): two or more sets of directions

    Returns:
        dict: of all intersections (v > 1)

    """
    # 'o' will represent the origin.
    m = defaultdict(int)
    m[(0, 0)] = 1

    for bbb, it in enumerate(inputs):
        coord = [0, 0]
        for step in enumerate(it):
            direction = step[0]
            delta = int(step[1:])
            if direction == 'U':
                insert_nums(m, coord, delta, 1)
            elif direction == 'D':
                insert_nums(m, coord, -delta, 1)
            elif direction == 'L':
                insert_nums(m, coord, -delta, 0)
            else:
                insert_nums(m, coord, delta, 0)
    return {co: v for co, v in m.items() if v > 1}


def find_shortest(intersections: Dict[Tuple[int, int], int]) -> None:
    """Find the shortest distance intersection to origin.

    Args:
        intersections (dict): the mapping of intersecting inputs

    """
    print(min([sum([abs(x), abs(y)]) for x, y in intersections]))


def main() -> None:
    """Processes inputs."""
    # with open('input', 'r') as f:
    #     i = [t.split(',') for t in f.read().strip().split('\n')]
    # find_shortest(generate_map(i))

    for i in INPUTS:
        find_shortest(generate_map(i))


if __name__ == '__main__':
    main()
