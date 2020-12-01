import sys


SUM = 2020


def main() -> int:
    """Read from file and check for two numbers.

    The two numbers when added together equal SUM (2020).

    Returns:
        int: 0 if successful; 1 otherwise

    """
    try:
        with open(sys.argv[1], 'r') as f:
            file = f.read().rstrip().split('\n')
    except IndexError:
        return 1

    for line in file:
        num = int(line)
        diff = SUM - num
        if str(diff) in file:
            print(num * diff)
            return 0
    return 1


if __name__ == '__main__':
    main()
