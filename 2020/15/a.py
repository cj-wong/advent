from collections import defaultdict
from typing import List

import config


def number_game(numbers: List[str]) -> int:
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

    for turn in range(starting_turn, 2020 + 1):
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
    test_answer = 436
    file = config.TestFile(test_answer)
    test = number_game(file.contents[0])
    file.test(test)

    file = config.File()
    result = number_game(file.contents[0])
    config.LOGGER.info(result)


if __name__ == '__main__':
    main()
