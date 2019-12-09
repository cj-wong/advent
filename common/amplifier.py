from typing import List

import intcode


class NoSignalError(ValueError):
    """No signal detected."""
    pass


class Amplifier(intcode.Interpreter):
    """Represents an amplifier, a specific Intcode interpreter."""

    def __init__(
        self, ops: str, phase: int, silent: bool
        ) -> None:
        """Initialize the amplifier with `phase`, defined in
        the main file to be between PHASE_MIN and PHASE_MAX.

        Args:
            ops (str): Intcode operations
            phase (int): the phase setting
            silent (bool): whether to suppress prints

        """
        super().__init__(ops, silent=silent)
        self.phase = phase
        self.phase_counter = 0
        self.signal_out = None
        self.jump = 0

    def init_signal(self) -> None:
        """Initialize the signal. Should only be used by amplifier 'A'.
        """
        self.signal = 0

    def load_signal(self, signal: int) -> None:
        """Load a signal `signal` to use."""
        self.signal = signal

    def save_state(self) -> None:
        """Save current state, to restore later."""
        self.state = copy(self.ops)

    def restore_state(self) -> None:
        """Restore a copy of state."""
        self.ops = copy(self.state)

    def print(self, n: int) -> None:
        """Prints `n`. Used for operator 104.
        In this overridden method, `self.signal_out` is set.

        Args:
            n (int): the direct number to print

        """
        self.signal_out = n
        super().print_at(index)

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
        """Resume amplifier operations.

        Args:
            signal (int): resume using a signal from the previous
                amplifier; E -> A, A -> B, etc.

        """
        self.signal = signal
        self.signal_out = None
        self.run_ops()


class Cluster:
    """A cluster of amplifiers. Currently, they go up from A to E."""
    names = ['A', 'B', 'C', 'D', 'E']

    def __init__(
        self, ops: List[int], phases: List[int], silent: bool = True
        ) -> None:
        """Initialize the clusters.

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
        #self.amplifiers['A'].init_signal()

    def run(self) -> int:
        """Run the cluster in sequence.

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
                    pass
                self.signals.append(amplifier.signal_out)
