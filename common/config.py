import logging
import random
import re
from pathlib import Path
from typing import Any


_P = Path('.').resolve()
_LOGGER_NAME = f'{_P.parent.stem}-{_P.stem}'

_R = re.compile(r'^[0-9]+-[0-9]+$')
if not _R.match(_LOGGER_NAME):
    _LOGGER_NAME = str(random.randint(0, 10000))

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)

_FH = logging.FileHandler(f'log.log')
_FH.setLevel(logging.DEBUG)

_CH = logging.StreamHandler()
_CH.setLevel(logging.INFO)

FORMATTER = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
_FH.setFormatter(FORMATTER)
_CH.setFormatter(FORMATTER)

LOGGER.addHandler(_FH)
LOGGER.addHandler(_CH)


def log_part_info(part: str, answer: Any) -> None:
    """Log the part of problem and answer as info.

    Args:
        part (str): either 'A' or 'B'
        answer (Any): anything that can be coerced to str

    """
    LOGGER.info(f'{part}: {answer}')


class File:
    """Read file into class.

    Attributes:
        contents (List[str]): a list of strings from a file

    """

    def __init__(self, path: str = "input.txt") -> None:
        """Initialize the file.

        Args:
            path (str): the path to the file

        Raises:
            FileNotFoundError: if the file at `path` is invalid

        """
        try:
            with open(path, 'r') as file:
                self.contents = file.read().rstrip().split('\n')
        except FileNotFoundError as e:
            LOGGER.error(e)
            raise e

    def contents_to_type(self, to_type: type) -> None:
        """Convert self.contents to a type.

        Args:
            to_type (type): the desired end type of each list element

        """
        self.contents = [to_type(content) for content in self.contents]


class TestFile(File):
    """Read a test file."""

    def __init__(self, answer: Any, path: str = "test_input.txt") -> None:
        """Initialize the file.

        Args:
            answer (Any): the answer for the file to check against
            path (str, optional): the path to the file; defaults

        Raises:
            FileNotFoundError: if the file at `path` is invalid

        """
        self.answer = answer
        super().__init__(path)

    def test(self, value: Any) -> None:
        """Test whether value matches the intended answer.

        Args:
            value (Any): the value to check against self.answer

        Raises:
            AssertionError: if the test failed

        """
        assert value == self.answer
