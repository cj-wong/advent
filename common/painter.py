from collections import defaultdict
from typing import List

import intcode


class NoSignalError(ValueError):
    """No signal detected."""
    pass


class Painter(intcode.Interpreter):
    """Represents a painter, a specific Intcode interpreter."""

    displacements = [
        (0, 1), #   up
        (1, 0), #   right
        (0, -1), #  down
        (-1, 0), #  left
        ]

    def __init__(
        self, ops: List[int], silent: bool = True
        ) -> None:
        """Initialize the painter with `phase`, defined in
        the main file to be between PHASE_MIN and PHASE_MAX.

        Args:
            ops (List[int]): Intcode operations
            phase (int): the phase setting
            silent (bool, optional): whether to suppress prints;
                defaults to True

        """
        super().__init__(ops, silent=silent)
        self.map = defaultdict(int)
        self.coordinates = (0, 0)
        self.direction = 0
        self.inputs = []

    def paint_and_move(self) -> None:
        """Paint and then move the painter to the new tile."""
        if len(self.inputs) == 2:
            color, direction = self.inputs
            self.map[self.coordinates] = color
            self.direction += 1 if direction == 1 else -1 
            self.direction %= 4
            displacement = self.displacements[self.direction]
            self.coordinates = (
                self.coordinates[0] + displacement[0],
                self.coordinates[1] + displacement[1]
                )
            self.inputs = []

    def print(self, n: int) -> None:
        """Prints `n`. Used for operator 104.
        In this overridden method, `self.signal_out` is set.

        Args:
            n (int): the direct number to print

        """
        super().print(n)
        self.inputs.append(n)
        self.paint_and_move()

    def print_at(self, index: int) -> None:
        """Print a stored operator/operand at index `index`.
        In this overridden method, `self.signal_out` is set.

        Args:
            index (int): the index of the operator

        """
        super().print_at(index)
        self.inputs.append(self.ops[index])
        self.paint_and_move()

    def store_input(self, index: int) -> None:
        """Store an integer from stdin into index `index`.
        In this overridden method, input is used given the current
        coordinates and the map.

        Args:
            index (int): where the stdin input goes

        Raises:
            NoSignalError: if no signal was found

        """
        self.ops[index] = self.map[self.coordinates]
