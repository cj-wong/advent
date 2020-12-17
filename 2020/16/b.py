import re
from collections import defaultdict
from typing import Dict, List, Union

import config


FIELD_RE = re.compile(r'^[a-z ]+: [0-9].*$')
ALL_RANGES = defaultdict(list)
TICKETS = List[List[int]]
YOUR_TICKET = []


def check_tickets_for_fields(notes: List[str]) -> Dict[int, set]:
    """Parse train ticket for validity and keep all valid tickets.

    Ignore your own ticket for this function.

    Args:
        notes (List[str]): the notes for ticket rules and your and nearby
            passengers' tickets

    Returns:
        Dict[int, set]: a dictionary of column indices to all matching fields

    """
    your_ticket = False
    nearby_tickets = False
    fields = 0
    for line in notes:
        if FIELD_RE.match(line):
            field, ranges = line.split(': ')
            ranges = ranges.split(' or ')
            for r in ranges:
                lower, upper = [int(n) for n in r.split('-')]
                ALL_RANGES[field].append(range(lower, upper + 1))
            fields += 1
        elif line == 'your ticket:':
            your_ticket = True
        elif line == 'nearby tickets:':
            nearby_tickets = True
            col_fields = {i: set(ALL_RANGES.keys()) for i in range(fields)}
        elif your_ticket:
            ticket = [int(n) for n in line.split(',')]
            YOUR_TICKET.extend(ticket)
            your_ticket = False
        elif nearby_tickets:
            ticket = [int(n) for n in line.split(',')]
            ticket_cols = match_cols_to_fields(ticket)
            # Silently discard invalid tickets.
            if not ticket_cols:
                continue
            for col_idx, col in enumerate(ticket_cols):
                col_fields[col_idx] = col_fields[col_idx] & col

    return col_fields


def match_cols_to_fields(ticket: List[int]) -> Union[List[set], None]:
    """Match columns in all valid tickets to their respective fields.

    Args:
        ticket (List[int]): a ticket containing numeric columns/fields

    Returns:
        List[set]: a dictionary mapping rule name to column number
        None: if ticket contains an invalid number

    """
    cols = [set() for _ in ticket]
    for i, number in enumerate(ticket):
        for field, ranges in ALL_RANGES.items():
            if any([number in r for r in ranges]):
                cols[i].add(field)
        if not cols[i]:
            return
    return cols


def determine_field_order(fields: Dict[int, set]) -> int:
    """Determine field order from fields and print answer to 2020-12-16 b.

    Args:
        fields (Dict[int, set]): fields of sets of str

    Returns:
        int: the product of all six 'departure' related fields on your ticket

    """
    ordered_fields = {}
    sorted_fields = sorted(fields.items(), key=lambda field: len(field[1]))
    for col_idx, fields in sorted_fields:
        for field in ordered_fields:
            fields.discard(field)
        field = fields.pop()
        ordered_fields[field] = col_idx

    product = 1
    for field, idx in ordered_fields.items():
        if field.startswith('departure'):
            product *= YOUR_TICKET[idx]

    return product


def main() -> None:
    """Parse and read train ticket."""
    # Unlike other problems, 2020-12-16 b does not have a test answer.
    # test_answer = 0
    # file = config.TestFile(test_answer)
    # test = check_tickets_for_fields(file.contents)
    # # file.test(test)

    file = config.File()
    result = check_tickets_for_fields(file.contents)
    result = determine_field_order(result)
    config.LOGGER.info(result)


if __name__ == '__main__':
    main()
