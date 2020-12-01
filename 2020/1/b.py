import sys


SUM = 2020


def main() -> int:
    """Read from file and check for three numbers.

    The three numbers when added together equal SUM (2020).

    Returns:
        int: 0 if successful; 1 otherwise

    """
    try:
        with open(sys.argv[1], 'r') as f:
            file = f.read().rstrip().split('\n')
    except IndexError:
        return 1

    for i, line in enumerate(file):
        num = int(line)
        diff = SUM - num
        for j, line2 in enumerate(file[i:]):
            num2 = int(line2)
            diff2 = diff - num2
            if str(diff2) in file[j:]:
                print(num * num2 * diff2)
                return 0
    return 1


if __name__ == '__main__':
    main()
