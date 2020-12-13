from math import ceil
from typing import List

import config


def find_soonest_bus(bus_lines: List[str]) -> None:
    """Find the soonest bus to the given departure time.

    Take the bus ID and multiply it by time to wait since departure time.

    Args:
        bus_lines (List[str]): the bus lines

    """
    departure = int(bus_lines[0])
    buses = bus_lines[1].split(',')
    for bus in buses:
        if bus == 'x':
            continue
        bus = int(bus)
        til_next = (ceil(departure / bus) * bus) % departure
        try:
            if til_next < lowest:
                lowest = til_next
                next_bus = bus
        except NameError:
            lowest = til_next
            next_bus = bus

    return lowest * next_bus

def main() -> None:
    """Confirm the bus schedule."""
    test_answer = 295 # bus 59 * 5 minutes
    file = config.TestFile(test_answer)
    test = find_soonest_bus(file.contents)
    file.test(test)

    file = config.File()
    result = find_soonest_bus(file.contents)
    config.LOGGER.info(result)


if __name__ == '__main__':
    main()
