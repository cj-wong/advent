from typing import Dict


BAG_QTY = Dict[str, int]


def calculate_all_children(rules: BAG_QTY) -> BAG_QTY:
    """Calculate all children of every bag.

    Args:
        rules (BAG_QTY): a dictionary mapping all parent bags to
            immediate children and children qty
        color (str): the color of the bag

    Returns:
        BAG_QTY: the quantity of all children of this bag

    """
    for child, child_qty in rules[color].items():
        pass
