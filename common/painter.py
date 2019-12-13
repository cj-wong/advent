from collections import defaultdict
from typing import List, Tuple

import intcode


class NoSignalError(ValueError):
    """No signal detected."""
    pass


class Painter(intcode.Interpreter):
    """Represents a painter, a specific Intcode interpreter.

    Attributes:
        coordinates (Tuple[int]): (x,y) of the current position
        direction (int): the current direction:
            0 = up, 1 = right, 2 = down, 3 = left
        displacements (List[Tuple[int]]): a list of vector displacements
            given direction (as the index)
        inputs (List[int]): a list of inputs that change direction
            and paint a color
        map (defaultdict[int]): a pseudo map with coordinates (tuple)
            as keys and color (int) as values

    """

    displacements = [
        (0, 1), #   up
        (1, 0), #   right
        (0, -1), #  down
        (-1, 0), #  left
        ]

    def __init__(
        self, ops: List[str], silent: bool = True
        ) -> None:
        """Initialize the painter with `phase`, defined in
        the main file to be between PHASE_MIN and PHASE_MAX.

        Args:
            ops (List[str]): Intcode operations
            silent (bool, optional): whether to suppress prints;
                defaults to True

        """
        super().__init__(ops, silent=silent)
        self.map = defaultdict(int)
        self.coordinates = (0, 0)
        self.direction = 0
        self.inputs = []

    def init_panel(self, color: int) -> None:
        """Initialize the starting panel with a given `color`.
        0: black, 1: white

        Args:
            color (int): the color to use on panel (0, 0)
        """
        self.map[(0, 0)] = color

    def paint_and_move(self) -> None:
        """Paint and then move the painter to the new panel."""
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
        """Prints `n`. Used for operator 104. Additionally,
        `self.signal_out` is set.

        Args:
            n (int): the direct number to print

        """
        super().print(n)
        self.inputs.append(n)
        self.paint_and_move()

    def print_at(self, index: int) -> None:
        """Print a stored operator/operand at `index`. Additionally,
        `self.signal_out` is set.

        Args:
            index (int): the index of the operator

        """
        super().print_at(index)
        self.inputs.append(self.ops[index])
        self.paint_and_move()

    def store_input(self, index: int) -> None:
        """Store an input (map value) given the current coordinates
        and the map.

        Args:
            index (int): where the stdin input goes

        Raises:
            NoSignalError: if no signal was found

        """
        self.ops[index] = self.map[self.coordinates]

    def render_map(self) -> None:
        all_x = [x for x, y in self.map.keys()]
        min_x = min(all_x)
        max_x = max(all_x)
        all_y = [y for x, y in self.map.keys()]
        min_y = min(all_y)
        max_y = max(all_y)
        # Reverse rows to show the image right-side up
        for y in range(max_y, min_y - 1, -1):
            print(''.join(
                [
                    '.'
                    if self.map[(x, y)] == 0
                    else '#'
                    for x
                    in range(min_x, max_x + 1)
                    ]
                )
            )
