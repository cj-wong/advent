from typing import List

import config


OCCUPIED = '#'
EMPTY = 'L'
FLOOR = '.'


def simulate_seating(rows: List[str]) -> int:
    """Simulate seating on the ferry.

    Args:
        rows (List[str]): rows of seats

    Returns:
        int: number of occupied seats

    """
    rows = [
        [OCCUPIED if seat == EMPTY else FLOOR for seat in row]
        for row in rows
        ]

    row_len = len(rows[0])
    col_len = len(rows)

    last = rows

    while True:
        state = [[FLOOR for _ in range(row_len)] for _ in range(col_len)]
        for y, row in enumerate(last):
            for x, seat in enumerate(row):
                occupied = 0
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        # Skip when both dy and dx are 0: the offsets that
                        # just point to the current seat
                        if dy == 0 and dx == 0:
                            continue

                        try:
                            cy = y
                            cx = x
                            while True:
                                cy += dy
                                cx += dx
                                # Because negative indices (within bounds) are
                                # possible in Python, they must be checked if
                                # negative (invalid index).
                                if cy < 0 or cx < 0:
                                    raise IndexError
                                if last[cy][cx] == FLOOR:
                                    continue
                                else:
                                    break
                            if last[cy][cx] == OCCUPIED:
                                occupied += 1

                        except IndexError:
                            pass

                if last[y][x] == OCCUPIED and occupied >= 5:
                    state[y][x] = EMPTY
                elif last[y][x] == EMPTY and occupied == 0:
                    state[y][x] = OCCUPIED
                else:
                    state[y][x] = last[y][x]

        if state == last:
            return sum([row.count(OCCUPIED) for row in state])

        last = state


def main() -> None:
    """Check the seating of the ferry."""
    test_answer = 26
    file = config.TestFile(test_answer)
    test = simulate_seating(file.contents)
    file.test(test)

    file = config.File()
    result = simulate_seating(file.contents)
    config.LOGGER.info(result)


if __name__ == '__main__':
    main()
