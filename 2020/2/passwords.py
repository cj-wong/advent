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
                x: left value (min count of z in A., position in B.)
                y: right value (max count of z in A., position in B.)
                z: a character requirement within password
            password (str): the password

        """
        self.password = password
        counts, self.char = policy.split(' ')
        self.l_value, self.r_value = [int(n) for n in counts.split('-')]

    def validate(self, part: str) -> bool:
        """Validate the password given the part of the problem.

        a. sled rental company system
        b. Official Toboggan Corporate Authentication System

        Args:
            part (str): either 'a' or 'b'

        Returns:
            bool: True if password is valid; False otherwise

        Raises:
            ValueError: if part is neither 'a' nor 'b'

        """
        if part not in 'ab':
            raise ValueError

        if part == 'a':
            return (
                self.password.count(self.char)
                in range(self.l_value, self.r_value + 1)
                )
        else:
            return (
                (self.password[self.l_value - 1] == self.char)
                ^ (self.password[self.r_value - 1] == self.char)
                )
