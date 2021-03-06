from typing import List

from astronomy import Body


# Minimum orbits: 4
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
    'K)YOU',
    'I)SAN',
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

    for b in ['YOU', 'SAN']:
        body = BODIES[b]
        path = []
        current = body
        while current.name != CENTER:
            path.append(current)
            current = current.parent
        visited[b] = path

    for offset, body in enumerate(visited['YOU'][::-1]):
        if body not in visited['SAN']:
            # -1 because we aren't counting starting bodies
            your_path = len(visited['YOU']) - offset - 1
            santa_path = len(visited['SAN']) - offset - 1
            print(your_path + santa_path)
            return


def main() -> None:
    """Processes inputs."""
    # parse_map(INPUT)
    # print('Expected output:', 4)

    with open('input', 'r') as f:
        orbit_map = f.read().strip().split('\n')
    parse_map(orbit_map)


if __name__ == '__main__':
    main()
