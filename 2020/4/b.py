import re
from typing import Dict, List

import config


HCL_RE = re.compile(r'^#[0-9a-f]{6}$', re.IGNORECASE)
PID_RE = re.compile(r'^[0-9]{9}$')


def validate_params(params: Dict[str, str]) -> bool:
    """Validate the parameters of a passport.

    Args:
        params (Dict[str, str]): a dictionary of passport parameters

    Returns:
        bool: True if the passport is valid; False otherwise

    """
    byr = int(params['byr'])
    iyr = int(params['iyr'])
    eyr = int(params['eyr'])
    hgt = params['hgt']
    hgt_unit = hgt[-2:]
    try:
        hgt_val = int(hgt[:-2])
    except ValueError:
        return False
    ecls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if byr not in range(1920, 2002 + 1):
        return False
    elif iyr not in range(2010, 2020 + 1):
        return False
    elif eyr not in range(2020, 2030 + 1):
        return False
    elif hgt_unit == 'cm' and hgt_val not in range(150, 193 + 1):
        return False
    elif hgt_unit == 'in' and hgt_val not in range(59, 76 + 1):
        return False
    elif not HCL_RE.match(params['hcl']):
        return False
    elif params['ecl'] not in ecls:
        return False
    elif not PID_RE.match(params['pid']):
        return False
    else:
        return True


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
    print(test)
    file.test(test)

    file = config.File()
    result = validate(file.contents)
    config.LOGGER.info(result)


if __name__ == '__main__':
    main()
