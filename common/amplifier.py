from typing import List

import intcode


class NoSignalError(ValueError):
    """No signal detected."""
    pass


class Amplifier(intcode.Interpreter):
    """Represents an amplifier, a specific Intcode interpreter."""

    def __init__(
        self, ops: List[int], phase: int, silent: bool = True
        ) -> None:
        """Initialize the amplifier with `phase`, defined in
        the main file to be between PHASE_MIN and PHASE_MAX.

        Args:
            ops (List[int]): Intcode operations
            phase (int): the phase setting
            silent (bool, optional): whether to suppress prints;
                defaults to True

        """
        super().__init__(ops, silent=silent)
        self.phase = phase
        self.phase_counter = 0
        self.signal_out = None
        self.jump = 0

    def print(self, n: int) -> None:
        """Prints `n`. Used for operator 104.
        In this overridden method, `self.signal_out` is set.

        Args:
            n (int): the direct number to print

        """
        self.signal_out = n
        super().print(n)

    def print_at(self, index: int) -> None:
        """Print a stored operator/operand at index `index`.
        In this overridden method, `self.signal_out` is set.

        Args:
            index (int): the index of the operator

        """
        self.signal_out = self.ops[index]
        super().print_at(index)

    def store_input(self, index: int) -> None:
        """Store an integer from stdin into index `index`.
        In this overridden method, `sys.argv` is absent. Phases
        are used instead.

        Args:
            index (int): where the stdin input goes

        Raises:
            NoSignalError: if no signal was found

        """
        if self.phase_counter == 0:
            self.ops[index] = self.phase
        elif self.signal is not None:
            self.ops[index] = self.signal
            self.signal = None
        else:
            raise NoSignalError

        self.phase_counter += 1

    def resume(self, signal: int) -> None:
        """Resume amplifier operations. On the first iteration,
        this is functionally the same as `self.run_ops()`.

        Args:
            signal (int): resume using a signal from the previous
                amplifier; E -> A, A -> B, etc.

        """
        self.signal = signal
        self.signal_out = None
        self.run_ops()


class Controller:
    """A controller of amplifiers. Currently, they go up from A to E.

    Attributes:
        names (List[str]): names (letters) of each amplifier
        amplifiers (Dict[str, Amplifier]): amplifiers by name (key)
        signals (List[int]): a list containing signals; these should never
            exceed len 2

    """
    names = ['A', 'B', 'C', 'D', 'E']

    def __init__(
        self, ops: List[int], phases: List[int], silent: bool = True
        ) -> None:
        """Initialize the controller with amplifiers.

        Args:
            ops (List[int]): Intcode operations
            phases (List[int]): phase settings corresponding to
                each amplifier
            silent (bool, optional): whether to suppress prints;
                defaults to True

        """
        self.amplifiers = {
            name: Amplifier(ops, phase, silent)
            for name, phase
            in zip(self.names, phases)
            }
        self.signals = []

    def run(self) -> int:
        """Run the controller in sequence.

        Returns:
            int: the final signal of amplifier 'E'

        """
        while True:
            for name, amplifier in self.amplifiers.items():
                try:
                    # Primes 'A'
                    if not self.signals:
                        signal = 0
                    else:
                        signal = self.signals.pop(0)
                    amplifier.resume(signal)

                    if name == 'E':
                        return amplifier.signal_out

                except NoSignalError:
                    # Because NoSignalError is thrown when an amplifier
                    # runs out of signal input and we need to retrieve
                    # its `signal_out` regardless if NoSignalError is
                    # thrown, just pass.
                    pass

                self.signals.append(amplifier.signal_out)
