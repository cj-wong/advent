from typing import List


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
