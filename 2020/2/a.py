from typing import List

import config
import passwords


def validate(file_contents: List[str], part: str) -> int:
    """Validate file contents using `func`.

    Args:
        file_contents (List[str]): a list of passwords and policies
        part (str): either 'a' or 'b'

    Returns:
        int: number of valid passwords

    """
    valid = 0
    for line in file_contents:
        policy, password = line.split(': ')
        p = passwords.Password(policy, password)
        if p.validate(part):
            valid += 1

    return valid


def main() -> None:
    """Check the number of valid passwords."""
    # Part A
    test_answer = 2 # Number of valid test passwords
    file = config.TestFile(test_answer)
    valid = validate(file.contents, 'a')
    file.test(valid)

    # Part B
    test_answer = 1 # Number of valid test passwords
    file = config.TestFile(test_answer)
    valid = validate(file.contents, 'b')
    file.test(valid)

    # Part A
    file = config.File()
    valid = validate(file.contents, 'a')
    config.log_part_info('A', valid)
    # Part B
    valid = validate(file.contents, 'b')
    config.log_part_info('B', valid)


if __name__ == '__main__':
    main()
