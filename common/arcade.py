from collections import defaultdict
from typing import List

import intcode
import painter


class Game(painter.Painter):
    """Representation of a simple arcade game."""
    tiles = {
        0: 'empty',
        1: 'wall',
        2: 'block',
        3: 'paddle',
        4: 'ball',
        }

    def __init__(self, ops: List[str], silent: bool = True) -> None:
        """Initialize the game with operations `ops`.

        Args:
            ops (List[str]): a list of operators/operands
            silent (bool, optional): whether to suppress prints;
                defaults to True

        """
        intcode.Interpreter.__init__(self, ops, silent=silent)
        self.map = defaultdict(int)
        self.inputs = []
        self.paint_and_move = self.draw_tile

    def insert_quarters(self) -> None:
        """Insert quarters to play."""
        self.ops[0] = 2

    def draw_tile(self) -> None:
        """Draw a tile according to input. Points to 
        `painter.Painter.paint_and_move`.

        """
        if len(self.inputs) == 3:
            x, y, tile = self.inputs
            if x == -1 and y == 0 and tile not in self.tiles:
                print('Current score:', tile)
            else:
                if self.tiles[tile] == 'ball':
                    self.ball = (x, y)
                elif self.tiles[tile] == 'paddle':
                    self.paddle = (x, y)
                self.map[(x, y)] = tile
            self.inputs = []

    def count_tiles(self) -> None:
        """Counts tiles and prints per line."""
        values = list(self.map.values())
        for tile, name in self.tiles.items():
            print(name, 'count:', values.count(tile))

    def store_input(self, index: int) -> None:
        """Store an integer from stdin into index `index`.
        In this overridden method, input is used given the current
        coordinates of both the ball and paddle.

        Args:
            index (int): where the stdin input goes

        Raises:
            NoSignalError: if no signal was found

        """
        if self.ball[0] > self.paddle[0]:
            direction = 1
        elif self.ball[0] < self.paddle[0]:
            direction = -1
        else:
            direction = 0
        self.ops[index] = direction
