from collections import Counter
from typing import List

import image


HEIGHT = 6
WIDTH = 25


def main() -> None:
    """Processes inputs."""
    with open('input', 'r') as f:
        text = f.read().strip()

    image.Image(text, HEIGHT, WIDTH).check_layers()


if __name__ == '__main__':
    main()
