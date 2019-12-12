from collections import Counter
from itertools import zip_longest
from typing import Iterable, Tuple


COLORS = {
    '0': '#',
    '1': '.',
    }


def grouper(iterable: Iterable, n: int) -> Tuple:
    """Groups an `iterable` into smaller chunks. Adapted from:
    https://docs.python.org/3/library/itertools.html#itertools-recipes

    Args:
        iterable (Iterable): any iterable to break into smaller pieces
            with length `n`
        n (int): the length of each chunk

    """
    args = [iter(iterable)] * n
    return zip_longest(*args)


class Image:
    """A text-based image.

    Attributes:
        height (int): the height of the image in "pixels"
        width (int): the width of the image in "pixels"
        per_layer (int): how many characters (height * width) represent
            a layer (2D) from text (1D)
        layers (List[str]): layers of the image, with each str
            representing a row of a layer

    """
    def __init__(self, text: str, height: int, width: int) -> None:
        """Initialize the image and its dimensions.

        Args:
            text (str): the text representation of the image
            height (int): the height of the image in "pixels"
            width (int): the width of the image in "pixels"

        """
        self.height = height
        self.width = width
        self.per_layer = height * width
        self.layers = []
        for layer in grouper(text, self.per_layer):
            self.layers.append(
                [
                    ''.join(list(row))
                    for row
                    in grouper(layer, width)
                    ]
                )

    def check_layers(self) -> None:
        """Check layers for errors. If the layer with least 0s
        outputs a correct value for number of 1s multiplied by
        number 2s, no errors were found.

        """
        counters = [Counter(''.join(layer)) for layer in self.layers]
        target = sorted(counters, key=lambda c: c['0'])[0]
        print(target['1'] * target['2'])

    def translate_pixel(self, y: int, x: int) -> str:
        """Translates a 'pixel' by numbers.

        Args:
            y (int): y-axis (height)
            x (int): x-axis (width)

        Returns:
            str: representing the pixel

        """
        for pixel in [layer[y][x] for layer in self.layers]:
            if pixel in COLORS:
                return COLORS[pixel]
        return ' '

    def render(self) -> None:
        """Renders the image as a text-image. Layers are combined,
        top-down. If a layer has '2' in a given pixel, the next layer(s)
        is (are) used until either a '0' or '1' is found or the end of
        the layers has been reached.

        """
        self.image = []
        for h in range(self.height):
            row = [self.translate_pixel(h, w) for w in range(self.width)]
            self.image.append(''.join(row))
        print('\n'.join(self.image))
