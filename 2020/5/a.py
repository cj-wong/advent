from math import ceil
from typing import List, Tuple

import config


SEAT_METADATA = Tuple[int, int, int]
ALL_SEAT_METADATA = List[SEAT_METADATA]


def determine_row_col(
        pass_part: List[str], char: str, left: int, right: int) -> int:
    """Check the bounds of the boarding pass section provided.

    The section of the boarding pass will loop until the last element,
    and then determine the value with that last element.

    Args:
        pass_part (List[str]): part of the boarding pass
        char (str): the character representing direction toward the end
        left (int): left (lower) bound
        right (int): right (upper) bound

    Returns:
        int: the row or column

    """
    for direction in pass_part[:-1]:
        if direction == char:
            right = (left + right) // 2
        else:
            left = ceil((left + right) / 2)

    return right if pass_part[-1] != char else left


def boarding_pass_to_data(passes: List[str]) -> ALL_SEAT_METADATA:
    """Convert the boarding pass to metadata.

    Args:
        passes (List[str]): the boarding passes

    """
    row_first = 0
    row_last = 127
    col_first = 0
    col_last = 7
    answers = []
    for line in passes:
        row = determine_row_col(line[:7], 'F', row_first, row_last)
        col = determine_row_col(line[7:], 'L', col_first, col_last)
        seat_id = row * 8 + col
        answers.append((row, col, seat_id))

    return answers


def get_highest_seat_id(pass_data: ALL_SEAT_METADATA) -> int:
    """Get the highest seat ID (row * 8 + col) from boarding pass data.

    Args:
        pass_data (ALL_SEAT_METADATA): boarding pass metadata;
            (row: int, col: int, seat_id: int)

    Returns:
        int: the highest seat ID

    """
    return sorted(pass_data, key=lambda data: data[2], reverse=True)[0][2]


def find_empty_seat_id(pass_data: ALL_SEAT_METADATA) -> SEAT_METADATA:
    """Find the seat with adjacent filled seats and get its metadata.

    Args:
        pass_data (ALL_SEAT_METADATA): boarding pass metadata;
            (row: int, col: int, seat_id: int)

    Returns:
        Tuple[int, int, int]: the missing seat's metadata

    """
    seat_ids = sorted([seat_id for row, col, seat_id in pass_data])

    last = seat_ids[0]

    for seat_id in seat_ids[1:]:
        if seat_id == last + 2:
            return seat_id - 1
        last = seat_id


def main() -> None:
    """Process boarding passes."""
    # Part A only
    test_answer = [
        (44, 5, 357), # FBFBBFFRLR
        (70, 7, 567), # BFFFBBFRRR
        (14, 7, 119), # FFFBBBFRRR
        (102, 4, 820) # BBFFBBFRLL
        ]
    file = config.TestFile(test_answer)
    tests = boarding_pass_to_data(file.contents)
    file.test(tests)

    file = config.File()
    result = boarding_pass_to_data(file.contents)
    config.LOGGER.info(f'A: {get_highest_seat_id(result)}')

    # Part B
    result = find_empty_seat_id(result)
    config.LOGGER.info(f'B: {result}')


if __name__ == '__main__':
    main()
