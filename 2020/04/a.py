from typing import List

import config


def validate(passport_list: List[str]) -> int:
    """Validate passports. All passports must contain the following parameters.

    Parameters:
    - byr (Birth Year)
    - iyr (Issue Year)
    - eyr (Expiration Year)
    - hgt (Height)
    - hcl (Hair Color)
    - ecl (Eye Color)
    - pid (Passport ID)

    Optional:
    - cid (Country ID)

    Args:
        passport_list (List[str]): the passport file in list form

    """
    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    params = {}
    valid = 0
    for line in passport_list:
        if not line:
            # Flush passport contents
            if required <= set(params.keys()):
                valid += 1
            params = {}
            continue
        for ps in line.split(' '):
            k, v = ps.split(':')
            params[k] = v

    if params:
        if required <= set(params.keys()):
            valid += 1

    return valid


def main() -> None:
    """Read and count valid passports."""
    test_answer = 2
    file = config.TestFile(test_answer)
    test = validate(file.contents)
    file.test(test)

    file = config.File()
    result = validate(file.contents)
    config.LOGGER.info(result)


if __name__ == '__main__':
    main()
