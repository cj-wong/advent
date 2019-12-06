from typing import List


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


class CelestialBody:
    """Represents a celestial body with orbits."""
    def __init__(self, name: str) -> None:
        """Initialize using a name."""
        self.name = name
        self.parent = None

    def add_parent(self, body) -> None:
        """Add a direct parent `body`.

        Args:
            body (CelestialBody): the parent body

        """
        self.parent = body


def initialize_body(body: str) -> CelestialBody:
    """Initializes a celestial `body`. Only does anything
    if `body` is not in `BODIES`.

    Args:
        body (str): name of the body

    Returns:
        CelestialBody: the represented object

    """
    if body not in BODIES:
        BODIES[body] = CelestialBody(body)
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

    for _, body in BODIES.items():
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
    with open('input', 'r') as f:
        orbit_map = f.read().strip().split('\n')
    parse_map(orbit_map)
    # parse_map(INPUT)


if __name__ == '__main__':
    main()
