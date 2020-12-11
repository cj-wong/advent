from typing import List

import config


OCCUPIED = '#'
EMPTY = 'L'
FLOOR = '.'


def simulate_seating(rows: List[str]) -> None:
    """Simulate seating on the ferry.

    Args:
        rows (List[str]): rows of seats

    """
    rows = [
        [OCCUPIED if seat == EMPTY else FLOOR for seat in row]
        for row in rows
        ]

    row_len = len(rows[0])
    col_len = len(rows)

    states = [rows]

    while True:
        state = [[FLOOR for _ in range(row_len)] for _ in range(col_len)]
        previous_rows = states[-1]
        for y, row in enumerate(previous_rows):
            for x, seat in enumerate(row):
                occupied = 0
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if dy == 0 and dx == 0:
                            continue

                        try:
                            if (x == 0 and dx == -1) or (y == 0 and dy == -1):
                                raise IndexError
                            c = 1
                            while (previous_rows[y + c * dy][x + c * dx]
                                   == FLOOR):
                                c += 1
                            if (y + c * dy) < 0 or (x + c * dx) < 0:
                                raise IndexError
                            if (previous_rows[y + c * dy][x + c * dx]
                                    == OCCUPIED):
                                occupied += 1
                        except IndexError:
                            pass

                if previous_rows[y][x] == OCCUPIED and occupied >= 5:
                    state[y][x] = EMPTY
                elif previous_rows[y][x] == EMPTY and occupied == 0:
                    state[y][x] = OCCUPIED
                else:
                    state[y][x] = previous_rows[y][x]

        if state == previous_rows:
            return sum([row.count(OCCUPIED) for row in state])

        states.append(state)


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
