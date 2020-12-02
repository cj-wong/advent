class Password:
    """Represents a password with policy.

    Attributes:
        password (str): the password itself
        l_value (int): min value of z in A., position in B.
        r_value (int): max value of z in A., position in B.

    """

    def __init__(self, policy: str, password: str) -> None:
        """Initialize the password class with policy and password.

        Args:
            policy (str): in format x-y z, where:
                x: left value (min value of z in A., position in B.)
                y: right value (max value of z in A., position in B.)
                z: a character requirement within password
            password (str): the password

        """
        self.password = password
        counts, self.char = policy.split(' ')
        self.l_value, self.r_value = [int(n) for n in counts.split('-')]

    def validate_a(self) -> None:
        """Validate using policy from part a. From sled rental policy."""
        return (
            self.password.count(self.char)
            in range(self.l_value, self.r_value + 1)
            )

    def validate_b(self) -> None:
        """Validate using policy from part b.

        From Official Toboggan Corporate Authentication System.

        """
        return (
            (self.password[self.l_value - 1] == self.char)
            ^ (self.password[self.r_value - 1] == self.char)
            )
