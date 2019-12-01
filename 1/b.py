def get_fuel_from(mass: int) -> int:
    """Gets fuel from mass.

    Args:
        mass (int): mass for the fuel

    Returns:
        int: fuel necessary for the mass

    """
    return mass // 3 - 2


def get_more_fuel(fuel: int) -> int:
    """Gets fuel needed to fuel the fuel. Oh god.

    Args:
        fuel (int): the fuel needed to propel a mass earlier

    Returns:
        int: the total amount of fuel necessary for a given mass

    """
    total = 0
    while fuel > 0:
        total += fuel
        fuel = get_fuel_from(fuel)
    return total


def main() -> None:
    """Main function. Opens input file and processes."""
    total = 0
    with open('input', 'r') as f:
        for line in f:
            fuel = get_fuel_from(int(line))
            total += get_more_fuel(fuel)
    print(total)


if __name__ == '__main__':
    main()
