from collections import defaultdict
from typing import Dict, List, Tuple

import config


ACTIVE = '#'


def iterate_conway_cubes(zeroeth_layer: List[str]) -> Dict[Tuple[int], int]:
    """Iterate 6 cycles for Conway Cubes.

    Args:
        zeroeth_layer (List[str]): the zeroeth layer with cubes

    """
    cube = defaultdict(int)
    offset = len(zeroeth_layer) // 2
    for y, line in enumerate(zeroeth_layer):
        y += offset
        for x, char in enumerate(line):
            x -= offset
            if char == ACTIVE:
                cube[(x, y)] += 1
                cube[(x, y)] %= 2

    return cube


def main() -> None:
    """Simulate cycles for Conway Cubes."""
    test_answer = 112
    file = config.TestFile(test_answer)
    test = iterate_conway_cubes(file.contents)
    file.test(test)

    file = config.File()
    result = iterate_conway_cubes(file.contents)
    config.LOGGER.info(result)


if __name__ == '__main__':
    main()
