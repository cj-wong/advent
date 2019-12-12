from typing import List

from astronomy import Body


# Orbits: 42
INPUT = [
    'COM)B',
    'B)C',
    'C)D',
    'D)E',
    'E)F',
    'B)G',
    'G)H',
    'D)I',
    'E)J',
    'J)K',
    'K)L',
    ]

BODIES = {}

CENTER = 'COM'


def initialize_body(body: str) -> Body:
    """Initializes a celestial `body`. Only does anything
    if `body` is not in `BODIES`.

    Args:
        body (str): name of the body

    Returns:
        Body: the represented object

    """
    if body not in BODIES:
        BODIES[body] = Body(body)
    return BODIES[body]


def parse_map(orbit_map: List[str]) -> None:
    """Parse an `orbit_map` to calculate orbits.

    Args:
        map (list): contains the orbit map

    """
    for line in orbit_map:
        center, orbiter = line.split(')')
        center = initialize_body(center)
        orbiter = initialize_body(orbiter)
        orbiter.add_parent(center)

    visited = {}

    for body in BODIES.values():
        if body in visited:
            continue
        orbits = 0
        path = []
        current = body
        while current.name != CENTER:
            orbits += 1
            path.append(current)
            current = current.parent
        for offset, p in enumerate(path):
            visited[p] = orbits - offset

    print(sum(visited.values()))


def main() -> None:
    """Processes inputs."""
    # parse_map(INPUT)
    # print('Expected output:', 42)

    with open('input', 'r') as f:
        orbit_map = f.read().strip().split('\n')
    parse_map(orbit_map)


if __name__ == '__main__':
    main()
