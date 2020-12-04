from typing import List

import config


def TODO(contents: List[str]) -> None:
    """TODO example function.

    Args:
        contents (List[str]): the file contents

    """
    for line in contents:
        pass


def main() -> None:
    """TODO."""
    test_answer = 0
    file = config.TestFile(test_answer)
    test = TODO(file.contents)
    file.test(test)

    file = config.File()
    result = TODO(file.contents)
    config.LOGGER.info(result)


if __name__ == '__main__':
    main()
