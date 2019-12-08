from collections import Counter
from itertools import zip_longest
from typing import List, Iterable


HEIGHT = 6
WIDTH = 25
PER_LAYER = HEIGHT * WIDTH

COLORS = {
    0: '#',
    1: '-',
    }

# Adapted from:
#   https://docs.python.org/3/library/itertools.html#itertools-recipes
def grouper(iterable: Iterable, n: int):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=None)


def translate_pixel(layers: List[int], y: int, x: int) -> str:
    """Translates a 'pixel' by numbers.

    Args:
        layers (List[int]): each layer, represented by ints
        y (int): y-axis (height)
        x (int): x-axis (width)

    Returns:
        str: representing the pixel

    """
    for pixel in [layer[y][x] for layer in layers]:
        if pixel in COLORS:
            return COLORS[int(pixel)]
    return ' '


def composite_image(layers: List[int]) -> None:
    """Composite an image top to bottom.

    Args:
        layers (List[int]): each layer, represented by ints

    """
    image = []
    for h in range(HEIGHT):
        row = [translate_pixel(layers, h, w) for w in range(WIDTH)]
        image.append(''.join(row))
    print('\n'.join(image))


def convert_to_image(text: str) -> List[int]:
    """Convert 'text' to an image map.

    Args:
        text (str): the text as a str

    Returns:
        List[int]: with each element as a layer

    """
    layers = []
    for l in grouper(text, PER_LAYER):
        layer = []
        for h, row in enumerate(grouper(l, WIDTH)):
            layer.append([int(pixel) for pixel in row])
        layers.append(layer)

    return layers


def main() -> None:
    """Processes inputs."""
    with open('input', 'r') as f:
        text = f.read().strip()

    layers = convert_to_image(text)
    composite_image(layers)


if __name__ == '__main__':
    main()
