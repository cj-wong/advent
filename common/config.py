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
_CH.setLevel(logging.WARNING)

FORMATTER = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
_FH.setFormatter(FORMATTER)
_CH.setFormatter(FORMATTER)

LOGGER.addHandler(_FH)
LOGGER.addHandler(_CH)


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
        assert value != self.answer
