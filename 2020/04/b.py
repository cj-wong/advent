import re
from typing import Dict, List

import config


HCL_RE = re.compile(r'^#[0-9a-f]{6}$', re.IGNORECASE)
PID_RE = re.compile(r'^[0-9]{9}$')


def validate_height(unit: str, value: int) -> bool:
    """Validate the height listed in a passport.

    Args:
        unit (str): 'cm' or 'in'
        value (int): the corresponding height in given unit

    Returns:
        bool: True if the height is acceptable; False otherwise

    """
    hgt_cm_min = 150
    hgt_cm_max = 193 + 1
    hgt_in_min = 59
    hgt_in_max = 76 + 1
    return (unit == 'cm' and value in range(hgt_cm_min, hgt_cm_max)
            or unit == 'in' and value in range(hgt_in_min, hgt_in_max))


def validate_params(params: Dict[str, str]) -> bool:
    """Validate the parameters of a passport.

    Args:
        params (Dict[str, str]): a dictionary of passport parameters

    Returns:
        bool: True if the passport is valid; False otherwise

    """
    byr = int(params['byr'])
    byr_min = 1920
    byr_max = 2002 + 1
    iyr = int(params['iyr'])
    iyr_min = 2010
    iyr_max = 2020 + 1
    eyr = int(params['eyr'])
    eyr_min = 2020
    eyr_max = 2030 + 1
    hgt = params['hgt']
    hgt_unit = hgt[-2:]
    try:
        hgt_val = int(hgt[:-2])
    except ValueError:
        return False
    ecls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return (byr in range(byr_min, byr_max)
            and iyr in range(iyr_min, iyr_max)
            and eyr in range(eyr_min, eyr_max)
            and validate_height(hgt_unit, hgt_val)
            and HCL_RE.match(params['hcl'])
            and params['ecl'] in ecls
            and PID_RE.match(params['pid'])
            )


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
                if validate_params(params):
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
