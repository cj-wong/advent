import re
from collections import defaultdict
from typing import Dict, List

import config


BAG_QTY = Dict[str, int]
BAG_CHILDREN = {}
BAG_RE = re.compile(r'(.+) bags?', re.IGNORECASE)
RULES = {}


def read_rules(rules: List[str]) -> None:
    """Read the rule into BAG_CHILDREN.

    Args:
        rules (List[str]): a list of rules for bags

    """
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


def calculate_children(color: str) -> None:
    """Calculate children bags of a bag with the specified color.

    Args:
        color (str): color of the bag to calculate children

    """
    children = defaultdict(int)
    for child_color, child_qty in RULES[color].items():
        if child_color not in BAG_CHILDREN:
            calculate_children(child_color)

        for cc_color, cc_qty in BAG_CHILDREN[child_color].items():
            total_c_qty = cc_qty * child_qty
            children[cc_color] += total_c_qty
        children[child_color] += child_qty

    BAG_CHILDREN[color] = children


def calculate_all_children() -> None:
    """Calculate all children of every bag."""
    for color in RULES:
        calculate_children(color)


def contains_colored_bag(color: str = 'shiny gold') -> int:
    """Calculate the number of parent bags containing shiny gold bags.

    Args:
        color (str, optional): the color bag to specify; defaults to
            'shiny gold'

    Returns:
        int: number of bags that can contain at least one shiny gold bag

    """
    count = 0
    for bag, children in BAG_CHILDREN.items():
        if color in children:
            count += 1

    return count


def count_all_children_in_colored_bag(color: str = 'shiny gold') -> int:
    """Calculate all children within a single shiny gold bag.

    Args:
        color (str, optional): the color bag to specify; defaults to
            'shiny gold'

    Returns:
        int: the number of all iterative children

    """
    count = 0
    for children, qty in BAG_CHILDREN[color].items():
        count += qty

    return count


def main() -> None:
    """Process bag rules."""
    # Part A
    test_answer = 4
    file = config.TestFile(test_answer)
    read_rules(file.contents)
    calculate_all_children()
    test = contains_colored_bag()
    file.test(test)

    file = config.File()
    read_rules(file.contents)
    calculate_all_children()
    result = contains_colored_bag()
    config.LOGGER.info(result)

    # Part B
    result = count_all_children_in_colored_bag()
    config.LOGGER.info(result)


if __name__ == '__main__':
    main()
