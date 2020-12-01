import config


SUM = 2020


def main() -> int:
    """Read from file and check for three numbers.

    The three numbers when added together equal SUM (2020).

    Returns:
        int: 0 if successful; 1 otherwise

    """
    test_answer = 241861950
    file = config.TestFile(test_answer)
    contents = file.contents
    for i, line in enumerate(contents):
        num = int(line)
        diff = SUM - num
        for j, line2 in enumerate(contents[i:]):
            num2 = int(line2)
            diff2 = diff - num2
            if str(diff2) in contents[j:]:
                file.test(num * num2 * diff2)

    file = config.File()
    contents = file.contents

    for i, line in enumerate(contents):
        num = int(line)
        diff = SUM - num
        for j, line2 in enumerate(contents[i:]):
            num2 = int(line2)
            diff2 = diff - num2
            if str(diff2) in contents[j:]:
                print(num * num2 * diff2)
                return 0
    return 1


if __name__ == '__main__':
    main()
