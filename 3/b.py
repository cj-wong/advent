from collections import defaultdict
from typing import Dict, Iterable, List, Set, Tuple


INPUTS = [
    [   # Steps: 610
        ('R75','D30','R83','U83','L12','D49','R71','U7','L72'),
        ('U62','R66','U55','R34','D71','R55','D58','R83')
        ],
    [   # Steps: 410
        ('R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'),
        ('U98','R91','D20','R16','D67','R40','U7','R15','U6','R7')
        ]
    ]

INTERSECTINGSET = Set[Tuple[int, int]]
INTERSECT_STEPS = Dict[Tuple[int, int], List[int]]


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
            m[(i + offset, coord[1])] = 1
        else:
            m[(coord[0], i + offset)] = 1
    coord[index] += rows


def map_step(
    m: defaultdict, coord: List[int], rows: int, index: int,
    steps: int, intersections: INTERSECTINGSET
    ) -> int:
    """Steps into the map `m` to find any intersections.

    Args:
        m (defaultdict): the coordinate system
        coord (list): the current coordinates
        rows (int): can be positive or negative; how many rows (y-axis)
            to add
        index (int): indicates which index to modify;
            0 = x-axis, 1 = y-axis
        steps (int): how many steps have happened so far,
            prior to this step
        intersections (set): intersections to check during this step

    """
    offset = 1 if rows > 0 else -1
    for s, i in enumerate(
        range(coord[index], coord[index] + rows, offset),
        start=1
        ):
        if index == 0:
            co = (i + offset, coord[1])
        else:
            co = (coord[0], i + offset)
        if co in intersections and co not in m:
            m[co] = steps + s
    coord[index] += rows


def generate_intersections(inputs: List[Tuple[str]]) -> INTERSECTINGSET:
    """Creates a map representing intersections after
    `inputs` directions.

    Args:
        inputs (list): two or more sets of directions

    Returns:
        dict: of all intersections (v > 1)

    """
    sets = []
    for it in inputs:
        sets.append(generate_map(it))
        
    return sets[0] & sets[1]


def generate_map(it: Iterable[str]) -> INTERSECTINGSET:
    """Creates a single map based on one set of instructions.

    Args:
        it (Iterable): the iterable containing instructions

    Returns:
        set: of the directions in coordinate form in place

    """
    m = defaultdict(int)
    coord = [0, 0]

    for step in it:
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

    return set(m.keys())


def traverse_all(
    inputs: List[Tuple[str]], intersections: INTERSECTINGSET
    ) -> INTERSECT_STEPS:
    data = []
    for it in inputs:
        data.append(traverse_map(it, intersections))

    return {co: sum([data[0][co], data[1][co]]) for co in intersections}


def traverse_map(
    it: Iterable[str], intersections: INTERSECTINGSET
    ) -> INTERSECT_STEPS:
    """Traverse a map given instructions in `it`.

    Args:
        it (Iterable): the iterable containing instructions

    Returns:
        dict

    """
    m = defaultdict(int)
    coord = [0, 0]
    steps = 0

    for step in it:
        direction = step[0]
        delta = int(step[1:])
        if direction == 'U':
            map_step(m, coord, delta, 1, steps, intersections)
        elif direction == 'D':
            map_step(m, coord, -delta, 1, steps, intersections)
        elif direction == 'L':
            map_step(m, coord, -delta, 0, steps, intersections)
        else:
            map_step(m, coord, delta, 0, steps, intersections)
        steps += abs(delta)

    return m


def find_shortest(intersections: INTERSECT_STEPS) -> None:
    """Find the shortest distance intersection to origin by steps.
    Modified from part a.

    Args:
        intersections (dict): the mapping of intersecting inputs

    """
    print(min(intersections.values()))


def main() -> None:
    """Processes inputs."""
    with open('input', 'r') as f:
        i = [t.split(',') for t in f.read().strip().split('\n')]
    intersections = generate_intersections(i)
    find_shortest(traverse_all(i, intersections))

    # for i in INPUTS:
    #     intersections = generate_intersections(i)
    #     find_shortest(traverse_all(i, intersections))


if __name__ == '__main__':
    main()
