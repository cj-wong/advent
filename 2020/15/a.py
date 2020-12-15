from collections import defaultdict
from typing import List

import config


def number_game(numbers: List[str], max_turns: int = 2020) -> int:
    """Simulate the number game.

    Args:
        numbers (List[str]): starting numbers for the game

    Returns:
        int: the 2020th number spoken

    """
    last_turns = defaultdict(list)
    times_spoken = defaultdict(int)
    numbers = numbers.split(',')
    starting_turn = len(numbers) + 1
    for turn, number in enumerate(numbers, start=1):
        last_number = int(number)
        last_turns[last_number].append(turn)
        times_spoken[last_number] += 1

    for turn in range(starting_turn, max_turns + 1):
        if times_spoken[last_number] == 1:
            last_number = 0
        else:
            last_number = (
                last_turns[last_number][-1] - last_turns[last_number][-2])

        last_turns[last_number].append(turn)
        times_spoken[last_number] += 1

    return last_number


def main() -> None:
    """Simulate the number game described in day 15."""
    # Part A
    test_answer = 436
    file = config.TestFile(test_answer)
    test = number_game(file.contents[0])
    file.test(test)

    # Part B
    file.answer = 175594
    test = number_game(file.contents[0], max_turns=30000000)
    file.test(test)

    # Part A
    file = config.File()
    result = number_game(file.contents[0])
    config.log_part_info('A', result)

    # Part B
    result = number_game(file.contents[0], max_turns=30000000)
    config.log_part_info('B', result)


if __name__ == '__main__':
    main()
