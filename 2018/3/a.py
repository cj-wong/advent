from typing import List

import config


FABRIC = List[List[int]]
CLAIM_CORNERS = {}
CLAIM_DIMENS = {}


def render_fabric(claims: List[str]) -> FABRIC:
    """Render fabric with claimed areas.

    Args:
        claims (List[str]): the list of claims

    Returns:
        FABRIC: the fabric with patterns roughly rendered

    """
    fabric = [[0 for x in range(1000)] for y in range(1000)]

    for claim in claims:
        claim_id, canvas = claim.split(' @ ')
        offset, dimensions = canvas.split(': ')
        x, y = [int(o) - 1 for o in offset.split(',')]
        w, h = [int(d) for d in dimensions.split('x')]
        claim_id = int(claim_id[1:])
        CLAIM_CORNERS[(x, y)] = claim_id
        CLAIM_DIMENS[claim_id] = (w, h)

        for _h in range(h):
            for _w in range(w):
                fabric[y + _h][x + _w] += 1

    return fabric


def calculate_overlapping_area(fabric: FABRIC) -> int:
    """Calculate the amount of overlapping claimed area in sq. in.

    Args:
        fabric (FABRIC): the roughly rendered fabric

    Returns:
        int: area in sq. in. of overlapping area

    """
    return len([dot for row in fabric for dot in row if dot > 1])


def find_non_overlapping_claim(fabric: FABRIC) -> int:
    """Find the claimed area that doesn't overlap with any others.

    Args:
        fabric (FABRIC): the roughly rendered fabric

    Returns:
        int: the claim ID

    """
    for y, row in enumerate(fabric):
        x = 0
        indices = [i for i, n in enumerate(row) if n == 1]
        for x in indices:
            if (x, y) in CLAIM_CORNERS:
                claim_id = CLAIM_CORNERS[(x, y)]
                w, h = CLAIM_DIMENS[claim_id]
                if not is_overlapping(fabric, x, y, w, h):
                    return claim_id


def is_overlapping(fabric: FABRIC, x: int, y: int, w: int, h: int) -> bool:
    """Check whether a claim overlaps anywhere.

    Overlaps are wherever any spaces are greater than 1.

    Args:
        fabric (FABRIC): the roughly rendered fabric
        x (int): the 0-based x-coordinate from top left corner
        y (int): the 0-based y-coordinate from top left corner
        w (int): width of the claimed area
        h (int): height of the claimed area

    Returns:
        bool: True if overlaps; False otherwise

    """
    for _h in range(h):
        s = set(fabric[y + _h][x:x + w])
        if len(s) > 1 or 1 not in s:
            return True

    return False


def main() -> None:
    """Check overlapping claims on fabric."""
    # Part A
    test_answer = 4
    file = config.TestFile(test_answer)
    fabric = render_fabric(file.contents)
    test = calculate_overlapping_area(fabric)
    file.test(test)

    file = config.File()
    fabric = render_fabric(file.contents)
    result = calculate_overlapping_area(fabric)
    config.LOGGER.info(f'A: {result}')

    # Part B
    test_answer = 3
    file = config.TestFile(test_answer)
    fabric = render_fabric(file.contents)
    test = find_non_overlapping_claim(fabric)
    file.test(test)

    file = config.File()
    fabric = render_fabric(file.contents)
    result = find_non_overlapping_claim(fabric)
    config.LOGGER.info(f'B: {result}')


if __name__ == '__main__':
    main()
