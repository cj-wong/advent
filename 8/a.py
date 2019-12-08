from collections import Counter
from typing import List


HEIGHT = 6
WIDTH = 25
PER_LAYER = HEIGHT * WIDTH


def check_layers(layers: List[int]) -> None:
    """Check layers for conditions: least 0s.

    Args:
        layers (List[int]): each layer, represented by ints

    """
    counters = [Counter(layer) for layer in layers]
    target = sorted(counters, key=lambda c: c['0'])[0]
    print(target['1'] * target['2'])


def convert_image(image: str) -> List[int]:
    """Convert a string into an 'image'.

    Args:
        image (str): the image as a str

    Returns:
        List[int]: with each element as a layer

    """
    layers = []
    nlayers = len(image) // PER_LAYER
    for i in range(nlayers):
        layers.append(image[i * PER_LAYER:(i + 1) * PER_LAYER])
        # for w in range(HEIGHT):
        #     for h in range(WIDTH):
    return layers


def main() -> None:
    """Processes inputs."""
    with open('input', 'r') as f:
        image = f.read().strip()

    layers = convert_image(image)
    check_layers(layers)


if __name__ == '__main__':
    main()
