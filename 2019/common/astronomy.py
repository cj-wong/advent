import math
import sys
from collections import defaultdict
from typing import List, Tuple


# Day 6
class Body:
    """Represents a celestial body with orbits.

    Attributes:
        name (str): name of the celestial body
        parent (Body): this celestial body's parent

    """
    def __init__(self, name: str) -> None:
        """Initialize using a name.

        Args:
            name (str): name of this celestial body

        """
        self.name = name
        self.parent = None

    def add_parent(self, body: 'Body') -> None:
        """Add a direct parent `body`.

        Args:
            body (Body): the parent body

        """
        self.parent = body


# Day 10
class Asteroid:
    """Represents an asteroid.

    Attributes:
        x (int): the x-coordinate of the asteroid
        y (int): the y-coordinate of the asteroid
        seen (List[Tuple[int]]): a list of directly seen asteroids by
            their coordinates (x,y)

    """
    def __init__(self, x: int, y: int) -> None:
        """Initialize the asteroid with its coordinates.

        Args:
            x (int): the x-coordinate of the asteroid
            y (int): the y-coordinate of the asteroid

        """
        self.x = x
        self.y = y
        self.seen = []

    def is_visible_from(self, v: Tuple[int], x: int, y: int) -> bool:
        """Is the asteroid at (x,y) with a vector f visible?
        Removes existing asteroid(s) blocked by this one if they both share
        the same reduced vector.

        Args:
            v (Tuple[int]): the reduced vector of the asteroid
            x (int): x-coordinate of the asteroid potentially seen from
                this asteroid
            y (int): y-coordinate of the asteroid potentially seen from
                this asteroid

        Returns:
            bool: True if visible, even if a previously existing asteroid
                has the same vector but is blocked by the one checked in
                this function; False otherwise

        """
        dx = abs(x - self.x)
        dy = abs(y - self.y)
        for v0, (x0, y0) in self.seen:
            if v0 == v:
                dx0 = abs(x0 - self.x)
                dy0 = abs(y0 - self.y)
                if dx < dx0 or dy < dy0:
                    self.seen.remove((v0, (x0, y0)))
                    return True
                else:
                    return False
        return True

    def map_seen(self, a_map: 'AsteroidField') -> None:
        """Map asteroids that this asteroid can see.

        Args:
            a_map (AsteroidField): the map of the asteroid field

        """
        for (x, y), asteroid in a_map.asteroids.items():
            if asteroid == self:
                continue
            v = Vector(x - self.x, y - self.y).to_tuple()
            result = self.is_visible_from(v, x, y)

            if result:
                self.seen.append((v, (x, y)))

    def count_vaporized(
        self, n: int, target: int, quadrant: List[Tuple[int]],
        reverse: bool = False
        ) -> int:
        """Count vaporized asteroids and if `n` is greater than or equal to
        200, sort the `quadrant` and output the 200th.

        Args:
            n (int): the current number of vaporized asteroids
            quadrant (List[Tuple[int]]): list of coordinates in a quadrant
            reverse (bool, optional): whether to reverse sort;
                defaults to False

        Returns:
            int: `n`, after processing `quadrant`

        """
        if n >= target - len(quadrant):
            results = [
                ((x, y), abs(math.atan2(dy, dx)))
                for (dx, dy, x, y)
                in quadrant
                ]
            fx, fy = sorted(
                results,
                key=lambda r: r[1],
                reverse=reverse
                )[target - 1 - n][0]
            print(f'Vaporized #{target}: ({fx},{fy}); answer:', fx * 100 + fy)
            sys.exit(0)
        return n + len(quadrant)

    def vaporize_until(self, a_map: 'AsteroidField', target: int = 200) -> None:
        """Vaporize asteroids directly seen from this one.

        Note: if a KeyError is raised, you have set `target` higher
        than the total of asteroids.

        Args:
            a_map (AsteroidField): a map of asteroids
            target (int, optional): the nth desired target of vaporization;
                defaults to 200, the target for the Advent problem

        """
        records = []
        n = 0
        while n < target:
            # These aren't the same as mathematical quadrants. Because
            # the "sweeping" arm rotates clockwise, the mathematical q4
            # is the second quadrant to be reached. Likewise for below
            # q's. Furthermore, the y-axis is inverse-order; the "top"
            # is negative relative to the center.
            q1 = [
                (dx, dy, x, y)
                for ((dx, dy), (x, y))
                in self.seen
                if x >= self.x and y < self.y
                ]
            n = self.count_vaporized(n, target, q1, reverse=True)
            q2 = [
                (dx, dy, x, y)
                for ((dx, dy), (x, y))
                in self.seen
                if x >= self.x and y >= self.y
                ]
            n = self.count_vaporized(n, target, q2)
            q3 = [
                (dx, dy, x, y)
                for ((dx, dy), (x, y))
                in self.seen
                if x < self.x and y >= self.y
                ]
            n = self.count_vaporized(n, target, q3)
            q4 = [
                (dx, dy, x, y)
                for ((dx, dy), (x, y))
                in self.seen if x < self.x and y < self.y
                ]
            n = self.count_vaporized(n, target, q4, reverse=True)

            # Haven't reached the nth? Delete all vaporized asteroids.
            for (_, (x, y)) in self.seen:
                del a_map.asteroids[(x, y)]

            # Get the next set of available seen asteroids.
            self.map_seen(a_map)



class AsteroidField:
    """Represents a cluster/map of asteroids.

    Attributes:
        asteroids (Dict[Tuple[int], Asteroid]): a pseudo-map of
            asteroids, with keys as coordinates (x,y)

    """
    def __init__(self, a_map: str) -> None:
        """Map asteroids given an `a_map`. The first line is treated as
        y = 0, and the first character of each line is treated as
        x = 0.

        Args:
            a_map (str): the asteroid map, as a multiline string

        """
        self.asteroids = {}
        for y, row in enumerate(a_map.split('\n')):
            for x, char in enumerate(row):
                if char == '#':
                    self.asteroids[(x, y)] = Asteroid(x, y)


class Vector:
    """A simple 2D vector. Used for calculating direction of asteroids.

    Attributes:
        x (int): the x-coordinate of the vector
        y (int): the y-coordinate of the vector

    """
    def __init__(self, x: int, y: int) -> None:
        """Initialize the vector using both axes. Tries to reduce
        the vector if possible.

        Args:
            x (int): the x-axis offset
            y (int): the y-axis offset

        """
        if x == 0:
            self.x = x
            if y > 0:
                self.y = 1
            else:
                self.y = -1
        elif y == 0:
            self.y = y
            if x > 0:
                self.x = 1
            else:
                self.x = -1
        else:
            gcd = math.gcd(x, y)
            self.x = x // gcd
            self.y = y // gcd

    def to_tuple(self) -> Tuple[int, int]:
        """Create a tuple representation of the vector."""
        return (self.x, self.y)


# Day 12
class Moon:
    """Represents a moon (of Jupiter).

    Attributes:
        position (List[int]): a (x,y,z) coordinate of current position
        velocity (List[int]): a (x,y,z) vector of velocity
        potential (int): potential energy derived from position
        kinetic (int): kinetic energy derived from velocity
        total_energy (int): potential * kinetic

    """
    def __init__(self, text: str) -> None:
        """Initialize the moon with its position.

        Args:
            text (str): the coordinates in text form

        """
        self.position = [
            int(co.split('=')[1])
            for co
            in text.strip('<>').split(',')
            ]
        self.velocity = [0, 0, 0]

    def get_velocity(self, other: 'Moon') -> None:
        """Get velocity and store it in `self.velocity` by comparing
        with `other` moons.

        Args:
            other (Moon): the other moon to compare

        """
        velocity = []
        for co_self, co_other in zip(self.position, other.position):
            if co_self > co_other:
                velocity.append(-1)
            elif co_self < co_other:
                velocity.append(1)
            else:
                velocity.append(0)
        self.velocity = [sum(vv) for vv in zip(velocity, self.velocity)]

    def move(self) -> None:
        """Move the moon according to position and velocity.

        Resets velocity to [0, 0, 0] at the end.

        """
        self.position = [sum(pv) for pv in zip(self.position, self.velocity)]
        self.potential = sum([abs(co) for co in self.position])
        self.kinetic = sum([abs(co) for co in self.velocity])
        self.total_energy = self.potential * self.kinetic
