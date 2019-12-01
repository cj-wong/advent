def get_fuel_from(mass: int) -> int:
    """Gets fuel from mass.

    Args:
        mass (int): mass for the fuel

    Returns:
        int: fuel necessary for the mass

    """
    return mass // 3 - 2


def main() -> None:
    """Main function. Opens input file and processes."""
    total = 0
    with open('input', 'r') as f:
        for line in f:
            total += get_fuel_from(int(line))
    print(total)


if __name__ == '__main__':
    main()
