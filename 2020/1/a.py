import config


SUM = 2020


def main() -> int:
    """Read from file and check for two numbers.

    The two numbers when added together equal SUM (2020).

    Returns:
        int: 0 if successful; 1 otherwise

    """
    test_answer = 514579
    file = config.TestFile(test_answer)
    contents = file.contents
    for line in contents:
        num = int(line)
        diff = SUM - num
        if str(diff) in contents:
            file.test(num * diff)

    file = config.File()
    contents = file.contents

    for line in contents:
        num = int(line)
        diff = SUM - num
        if str(diff) in contents:
            print(num * diff)
            return 0
    return 1


if __name__ == '__main__':
    main()
