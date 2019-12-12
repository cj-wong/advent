import math
from typing import List

from moon import Moon


def lcm_all(numbers: List[int]) -> int:
    """LCM of all `numbers` in a list.

    Args:
        numbers (List[int]): list of numbers to get LCM

    Returns:
        int: the lowest common multiple

    """
    lcm = numbers.pop(0)
    for number in numbers:
        lcm = number * lcm // math.gcd(number, lcm)

    return lcm


def search(text: str, index: int) -> int:
    """Search position and velocity by axis `index`. When the initial
    position and velocity per index are found, return the step count.

    Args:
        text (str): the starting positions
        index (int): x = 0, y = 1, z = 2

    Returns:
        int: step count for when all moons returns to its original
            position on an axis defined by `index`

    """
    moons = []
    initials = []
    lcms = []
    for t in text.split('\n'):
        moons.append(Moon(t))
        initials.append(moons[-1].position[index])

    step = 0
    while True:
        step += 1
        for moon_a in moons:
            for moon_b in moons:
                if moon_a == moon_b:
                    continue
                moon_a.get_velocity(moon_b)

        for moon in moons:
            moon.move()

        velocities = [moon.velocity[index] for moon in moons]
        positions = [moon.position[index] for moon in moons]
        if velocities.count(0) != len(moons):
            continue
        elif positions != initials:
            continue
        else:
            return step


def main() -> None:
    """Processes inputs."""
    with open('input', 'r') as f:
        text = f.read().strip()

    x = search(text, 0)
    y = search(text, 1)
    z = search(text, 2)

    print(lcm_all([x, y, z]))

    
if __name__ == '__main__':
    main()
