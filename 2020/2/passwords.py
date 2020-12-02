class Password:
    """Represents a password with policy."""

    def __init__(self, policy: str, password: str) -> None:
        """Initialize the password class with policy and password.

        Args:
            policy (str): in format x-y z, where:
                x: minimum times z is present
                y: maximum times z is present
                z: a character requirement within password
            password (str): the password

        """
        self.password = password
        counts, self.char = policy.split(' ')
        self.min_char, self.max_char = [int(n) for n in counts.split('-')]
        self.valid = (
            password.count(self.char)
            in range(self.min_char, self.max_char + 1)
            )
