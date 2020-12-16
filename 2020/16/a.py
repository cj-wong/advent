import re
from collections import defaultdict
from typing import List

import config


RULE_RE = re.compile(r'^[a-z]+: [0-9].*$')


def find_sum_all_invalid_values(notes: List[str]) -> int:
    """Parse train ticket for validity and add all invalid values.

    Ignore your own ticket for this function.

    Args:
        notes (List[str]): the notes for ticket rules and your and nearby
            passengers' tickets

    Returns:
        int: the sum of all invalid fields

    """
    sum_invalid = 0
    all_ranges = defaultdict(list)
    nearby_tickets = False
    for line in notes:
        if RULE_RE.match(line):
            field, ranges = line.split(': ')
            ranges = ranges.split(' or ')
            for r in ranges:
                lower, upper = [int(n) for n in r.split('-')]
                all_ranges[field].append(range(lower, upper + 1))
        elif line == 'nearby tickets:':
            nearby_tickets = True
        elif nearby_tickets:
            numbers = [int(n) for n in line.split(',')]
            for number in numbers:
                number_in_ranges = [
                    number in r
                    for ranges in all_ranges.values()
                    for r in ranges
                    ]
                if not any(number_in_ranges):
                    sum_invalid += number

    return sum_invalid


def main() -> None:
    """Parse and read train ticket."""
    test_answer = 71 # 4 + 55 + 12
    file = config.TestFile(test_answer)
    test = find_sum_all_invalid_values(file.contents)
    file.test(test)

    file = config.File()
    result = find_sum_all_invalid_values(file.contents)
    config.LOGGER.info(result)


if __name__ == '__main__':
    main()
