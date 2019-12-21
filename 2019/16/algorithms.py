import itertools
from typing import List


# Day 16
class FFT:
    """Represents the "Flawed Frequency Transmission" algorithm.

    Attributes:
        pattern (List[int]): the base pattern: [0, 1, 0, -1]
        patterns (List[List[int]]): patterns generated from `pattern`;
            each value in the base pattern is multiplied in quantity to
            the current digit position
        phases (int): the number of cycles to repeat
        signal (List[int]): a list representation of a signal (numbers)

    """
    def __init__(self, signal: str, phases: int) -> None:
        """Initialize the FFT using an initial `signal` and number of
        `phases` to repeat.

        Args:
            signal (str): the starting signal
            phases (int): number of cycles to repeat

        """
        self.signal = [int(s) for s in str(signal)]
        self.phases = phases
        self.pattern = [0, 1, 0, -1]
        self.patterns = []
        for digit in range(1, len(self.signal) + 1):
            pattern = []
            for i, p in enumerate(self.pattern):
                pattern.extend(list(itertools.repeat(p, digit)))
            self.patterns.append(pattern)

    def run(self) -> List[int]:
        """Run the algorithm with initial values until `phases` is
        reached.

        Returns:
            List[int]: the signal in list form

        """
        for _ in range(self.phases):
            signal = []
            bound = len(self.signal) + 1
            for position in range(1, bound):
                pattern = self.patterns[position - 1] * bound
                pattern.pop(0)
                signal.append(
                    abs(sum([s * p for s, p in zip(self.signal, pattern)])) % 10
                    )
            self.signal = signal
        return self.signal[:8]
