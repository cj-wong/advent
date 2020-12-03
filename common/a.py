import config


def main() -> None:
    """TODO."""
    test_answer = 0
    file = config.TestFile(test_answer)
    contents = file.contents
    for line in contents:
        pass

    file = config.File()
    contents = file.contents
    for line in contents:
        pass


if __name__ == '__main__':
    main()
