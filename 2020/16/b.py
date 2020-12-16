import re
from collections import defaultdict
from typing import Dict, List

import config


RULE_RE = re.compile(r'^[a-z]+: [0-9].*$')
ALL_RANGES = defaultdict(list)
TICKETS = List[List[int]]


def collect_valid_tickets(notes: List[str]) -> TICKETS:
    """Parse train ticket for validity and keep all valid tickets.

    Ignore your own ticket for this function.

    Args:
        notes (List[str]): the notes for ticket rules and your and nearby
            passengers' tickets

    Returns:
        TICKETS: all valid tickets

    """
    valid_tickets = []
    nearby_tickets = False
    for line in notes:
        if RULE_RE.match(line):
            field, ranges = line.split(': ')
            ranges = ranges.split(' or ')
            for r in ranges:
                lower, upper = [int(n) for n in r.split('-')]
                ALL_RANGES[field].append(range(lower, upper + 1))
        elif line == 'nearby tickets:':
            nearby_tickets = True
        elif nearby_tickets:
            numbers = [int(n) for n in line.split(',')]
            valid_number_check = []
            for number in numbers:
                valid_number_check.append(
                    any(
                        [
                            number in r
                            for ranges in ALL_RANGES.values()
                            for r in ranges
                            ]
                        )
                    )
            if all(valid_number_check):
                valid_tickets.append(numbers)

    return valid_tickets


def match_col_to_rule(tickets: TICKETS) -> Dict[str, int]:
    """Match columns in all valid tickets to their respective rules.

    Args:
        tickets (TICKETS): a list of tickets

    Returns:
        Dict[str, int]: a dictionary mapping rule name to column number

    """
    rules = {}
    ticket_cols_by_idx = {
        i: [ticket[i] for ticket in tickets]
        for i in range(len(tickets[0]))
        }

    for idx, ticket_col in ticket_cols_by_idx.items():
        for rule, ranges in ALL_RANGES.items():
            if idx in rules.values():
                continue
            if all([any([col in r for r in ranges]) for col in ticket_col]):
                rules[rule] = idx
                break

    return rules


def main() -> None:
    """Parse and read train ticket."""
    # Unlike other problems, 2020-12-16 b does not have a test answer.
    test_answer = 0
    file = config.TestFile(test_answer)
    test = collect_valid_tickets(file.contents)
    test = match_col_to_rule(test)
    print(test)
    # file.test(test)

    file = config.File()
    result = collect_valid_tickets(file.contents)
    test = match_col_to_rule(result)
    print(test)

    # config.LOGGER.info(result)


if __name__ == '__main__':
    main()
