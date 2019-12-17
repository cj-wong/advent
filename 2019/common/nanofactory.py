import math
from collections import defaultdict
from typing import List, Tuple


DELIM_IO = ' => '
START = 'ORE'
TARGET = 'FUEL'


class Chemical:
    """Represents a chemical used in the nanofactory."""
    def __init__(self, name: str) -> None:
        """Initialize the chemical with a name."""
        self.name = name

    def requires(
        self, qty: int, ingredients: List[Tuple[int, 'Chemical']]
        ) -> None:
        """The required `ingredients` to create `qty` of itself.

        Args:
            qty (int): the quantity produced after converting
                ingredients
            ingredients (List[Tuple[int, Chemical]]): ingredient list

        """
        self.requirements = ingredients
        self.qty = qty


class Nanofactory:
    """Represents a nanofactory, a fuel converter."""
    def __init__(self, reactions: List[str]) -> None:
        """Initalize the nanofactory with all reactions.

        Args:
            reactions (List[str]): a list of reactions, with comma-
                separated inputs and one output per reaction

        """
        self.chemicals = {}
        for reaction in reactions:
            ingredients, output = reaction.split(DELIM_IO)
            ingredients = [
                ingredient.strip().split(' ')
                for ingredient
                in ingredients.split(',')
                ]
            for qty, chemical in ingredients:
                if chemical not in self.chemicals:
                    self.chemicals[chemical] = Chemical(chemical)
            ingredients = [
                (int(qty), self.chemicals[chemical])
                for qty, chemical
                in ingredients
                ]
            out_qty, output = output.split(' ')
            out_qty = int(out_qty)
            if output not in self.chemicals:
                self.chemicals[output] = Chemical(output)
            self.chemicals[output].requires(out_qty, ingredients)

        self.solution = defaultdict(int)

    def solve(self, qty: int = None, chemical: 'Chemical' = None) -> None:
        """Solve fuel requirements recursively through each child.
        If no parameters are provided, start with 'FUEL'.

        Args:
            qty (int, optional): the current quantity needed for the
                chemical; defaults to None
            chemical (Chemical, optional): the current chemical;
                defaults to None

        """
        if qty is None and chemical is None:
            chemical = self.chemicals['FUEL']
            qty = chemical.qty

        for c_qty, chem in chemical.requirements:
            if chem.name == START:
                self.solution[chemical.name] += qty
            else:
                self.solve(c_qty * qty, chem)
        #return math.ceil(qty / chemical.qty) * ore

    def get_ore_solution(self) -> int:
        """Gets 'ORE' given a solved state."""
        fuel = 0
        for chem, c_qty in self.solution.items():
            chemical = self.chemicals[chem]
            # Because 'ORE' is the only input in a recipe, just take
            # the first (and only) requirement and take its quantity in
            # index 0.
            ore_qty = chemical.requirements[0][0]
            fuel += math.ceil(c_qty / chemical.qty) * ore_qty

        return fuel
