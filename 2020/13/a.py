from math import ceil, lcm
from typing import List

import config


def find_soonest_bus(bus_lines: List[str]) -> int:
    """Find the soonest bus to the given departure time.

    Take the bus ID and multiply it by time to wait since departure time.

    Args:
        bus_lines (List[str]): the bus lines

    Returns:
        int: next bus ID * time from departure until next bus

    """
    departure = int(bus_lines[0])
    buses = [int(bus) for bus in bus_lines[1].split(',') if bus != 'x']
    for bus in buses:
        til_next = (ceil(departure / bus) * bus) % departure
        try:
            if til_next < lowest:
                lowest = til_next
                next_bus = bus
        except NameError:
            lowest = til_next
            next_bus = bus

    return lowest * next_bus


def find_contest_pattern(bus_lines: List[str]) -> int:
    """Find the earliest value with the contest's pattern.

    Args:
        bus_lines (List[str]): the bus lines

    """
    buses = [int(bus) if bus != 'x' else 1 for bus in bus_lines[1].split(',')]
    lower = max(buses)
    upper = lcm(*buses) // buses[0]
    for i in range(lower, upper):
        minimum = i * buses[0]
        r = [(minimum + j) % bus for j, bus in enumerate(buses[1:], start=1)]
        if len(set(r)) == 1:
            return minimum


def main() -> None:
    """Confirm the bus schedule."""
    # Part A
    test_answer = 295 # bus 59 * 5 minutes
    file = config.TestFile(test_answer)
    test = find_soonest_bus(file.contents)
    file.test(test)

    # Part B
    file.answer = 1068781
    test = find_contest_pattern(file.contents)
    file.test(test)

    # Part A
    file = config.File()
    result = find_soonest_bus(file.contents)
    config.log_part_info('A', result)

    # Part B
    result = find_contest_pattern(file.contents)
    config.log_part_info('B', result)


if __name__ == '__main__':
    main()
