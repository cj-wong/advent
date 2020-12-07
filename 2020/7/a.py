import re
from collections import defaultdict
from typing import Dict, List

import config


BAG_QTY = Dict[str, int]
BAG_CHILDREN = {}
BAG_RE = re.compile(r'(.+) bags?', re.IGNORECASE)
RULES = {}


def read_rules(rules: List[str]) -> None:
    """Read the rule into BAG_CHILDREN."""
    for rule in rules:
        bag, children = rule[:-1].split(' contain ')
        color = BAG_RE.match(bag).group(1)
        RULES[color] = {}
        children = children.split(', ')
        for child in children:
            child_qty, child_bag = child.split(' ', maxsplit=1)
            child_color = BAG_RE.match(child_bag).group(1)
            try:
                RULES[color][child_color] = int(child_qty)
            except ValueError:
                # This bag color has no children.
                pass


def calculate_children(color: str) -> BAG_QTY:
    """Calculate children bags of a bag with the specified color."""
    children = defaultdict(int)
    for child_color, child_qty in RULES[color].items():
        while True:
            try:
                for cc_color, cc_qty in BAG_CHILDREN[child_color].items():
                    total_c_qty = cc_qty * child_qty
                    children[cc_color] += total_c_qty
                children[child_color] += child_qty
                break
            except KeyError:
                calculate_children(child_color)

    BAG_CHILDREN[color] = children


def calculate_all_children() -> BAG_QTY:
    """Calculate all children of every bag.

    Returns:
        BAG_QTY: the quantity of all children of this bag

    """
    for color in RULES:
        calculate_children(color)


def contains_shiny_gold_bag() -> int:
    """Calculate the number of parent bags containing shiny gold bags.

    Returns:
        int: number of bags that can contain at least one shiny gold bag

    """
    count = 0
    for bag, children in BAG_CHILDREN.items():
        if 'shiny gold' in children:
            count += 1

    return count


def main() -> None:
    """Process bag rules."""
    test_answer = 4
    file = config.TestFile(test_answer)
    read_rules(file.contents)
    calculate_all_children()
    test = contains_shiny_gold_bag()
    file.test(test)

    file = config.File()
    read_rules(file.contents)
    calculate_all_children()
    result = contains_shiny_gold_bag()
    config.LOGGER.info(result)


if __name__ == '__main__':
    main()
