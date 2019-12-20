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
        self, ingredients: List[Tuple[int, 'Chemical']], product: int
        ) -> None:
        """The required `ingredients` to create a quantity of `product`
        of itself.

        Args:
            product (int): the quantity produced after converting
                ingredients
            ingredients (List[Tuple[int, Chemical]]): ingredient list

        """
        self.ingredients = ingredients
        self.product = product


class Nanofactory:
    """Represents a nanofactory, a fuel converter."""
    def __init__(self, reactions: List[str]) -> None:
        """Initalize the nanofactory with all reactions.

        Args:
            reactions (List[str]): a list of reactions, with comma-
                separated inputs and one output per reaction

        """
        self.chemicals = {}
        self.coal_outputs = []
        for reaction in reactions:
            ingredients, output = reaction.split(DELIM_IO)
            ingredients = [
                ingredient.strip().split(' ')
                for ingredient
                in ingredients.split(',')
                ]
            for _, chemical in ingredients:
                if chemical not in self.chemicals:
                    self.chemicals[chemical] = Chemical(chemical)
            ingredients = [
                (int(qty), self.chemicals[chemical])
                for qty, chemical
                in ingredients
                ]
            out_qty, output = output.split(' ')
            if ingredients[0][1].name == START:
                self.coal_outputs.append(output)
            out_qty = int(out_qty)
            if output not in self.chemicals:
                self.chemicals[output] = Chemical(output)
            self.chemicals[output].requires(ingredients, out_qty)

        self.excess = defaultdict(int)

    def solve(
        self, qty: int = None, chemical: 'Chemical' = None
        ) -> None:
        """Solve fuel.ingredients recursively through each child.
        Until `START` is reached (this is a reverse search), keep
        recursing.

        If no parameters are provided, start with 'FUEL'.

        Args:
            qty (int, optional): the current quantity needed for the
                chemical; defaults to None
            chemical (Chemical, optional): the current chemical;
                defaults to None
            step (int, optional): the current step, with 1 as the step
                that produces 'FUEL'; defaults to 0

        """
        if qty is None and chemical is None:
            chemical = self.chemicals['FUEL']
            qty = chemical.product
        elif chemical.name == START:
            return qty

        if qty <= self.excess[chemical]:
            self.excess[chemical] -= qty
            return 0
        else:
            qty -= self.excess[chemical]
            self.excess[chemical] = 0

        ratio = math.ceil(qty / chemical.product)
        products = chemical.product * ratio

        # Add any excess generated. `qty` is guaranteed to be less than
        # or equal to `products`, so we only check for excess.
        if qty < products:
            self.excess[chemical] += products - qty

        ore = 0

        for c_qty, chem in chemical.ingredients:
            ore += self.solve(c_qty * ratio, chem)

        return ore
