from collections import defaultdict
from typing import List, Tuple


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


def insert_verticals(
    m: List[defaultdict], coord: List[int], rows: int
    ) -> None:
    """Inserts vertical lines horizontally.

    Args:
        m (list): the map in progress
        coord (list): the current coordinates
        min_c (list): the top-right most part coordinate
        max_c (list): the bottom-left most part coordinate
        rows (int): can be positive (U) or negative (D); represents
            how many rows will be filled
    
    """
    low = 1 if rows > 0 else -1
    for i in range(low, rows + low):
        try:
            row = m[coord[1] + i]
            row[coord[1]] += 1
        except IndexError:
            m[coord[1] + i] = defaultdict(int)
            row = m[coord[1] + i]
            row[coord[1]] += 1



def generate_map(inputs: List[Tuple[str]]) -> None:
    """Creates an ASCII map given directions.

    Args:
        inputs (list): two or more sets of directions

    """
    # 'o' will represent the origin.
    m = {0: defaultdict(int)}
    m[0][0] = 42
    coord = [0, 0]
    # min_c = [0, 0]
    # max_c = [0, 0]

    for tup in inputs:
        for step in tup:
            print(step, coord, m[coord[1]])
            direction = step[0]
            offset = int(step[1:])
            if direction == 'U':
                insert_verticals(m, coord, offset)
                coord[1] += offset
                # if coord[1] > max_c[1]:
                #     max_c[1] = coord[1]
            elif direction == 'D':
                insert_verticals(m, coord, -offset)
                coord[1] -= offset
            elif direction == 'L':
                for x in range(offset):
                    m[coord[1]][coord[0] - x] += 1
                coord[0] -= offset
            else:
                for x in range(offset):
                    m[coord[1]][coord[0] + x] += 1
                coord[0] += offset
    print(m)


def main() -> None:
    """Processes inputs."""
    # with open('input', 'r') as f:
    #     run_ops([int(x) for x in f.read().split(',')])
    for i in INPUTS:
        generate_map(i)


if __name__ == '__main__':
    main()
