import re
from collections import defaultdict
from typing import List

import config


DATE_RE = re.compile(
    r'^\[([0-9]{4})-([0-9]{2})-([0-9]{2}) ([0-9]{2}):([0-9]{2})'
    )
GUARD_RE = re.compile(r'Guard #([0-9]+) begins shift')


def determine_sleepiest_guard(records: List[str]) -> int:
    """Find sleepiest guard according to records.

    Args:
        records (List[str]): guard records

    Returns:
        int: sleepiest guard number * most commonly asleep minute

    """
    guards = {}
    last = None
    for record in records:
        date = DATE_RE.search(record)
        year = date.group(1)
        month = date.group(2)
        day = date.group(3)
        hour = int(date.group(4))
        minute = int(date.group(5))

        match = GUARD_RE.search(record)
        if match:
            last = int(match.group(1))
            if last not in guards:
                guards[last] = defaultdict(int)
        elif 'falls asleep' in record:
            sleep_start = (year, month, day, hour, minute)
        else: # 'wakes up' in record
            # hours = (hour - sleep_start[3]) % 24
            # if minute < sleep_start[-1]:
            #     hours -= 1
            # minutes = (minute - sleep_start[-1]) % 60
            # minutes += hours * 60 - 1
            if minute < sleep_start[-1]:
                for m in range(sleep_start[-1], 60):
                    guards[last][m] += 1
                lower = 0
            else:
                lower = sleep_start[-1]

            for m in range(lower, minute):
                guards[last][m] += 1

    sleepiest = sorted(guards, key=lambda guard: len(guards[guard]))[-1]
    sleep_min = sorted(guards[sleepiest].items(), key=lambda m: m[1])[-1][0]

    print(guards[sleepiest], sleep_min)

    return sleepiest * sleep_min


def main() -> None:
    """Check the guard records."""
    test_answer = 240 # Guard #10 * common minute 24
    file = config.TestFile(test_answer, sort=True)
    test = determine_sleepiest_guard(file.contents)
    file.test(test)

    file = config.File(sort=True)
    file.write_to_file()
    result = determine_sleepiest_guard(file.contents)
    config.LOGGER.info(result)


if __name__ == '__main__':
    main()
