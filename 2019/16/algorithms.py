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
    def __init__(self, signal: str, phases: int, repeat: int = 1) -> None:
        """Initialize the FFT using an initial `signal` and number of
        `phases` to repeat.

        Args:
            signal (str): the starting signal
            phases (int): number of cycles to repeat
            repeat (int, optional): number of times to repeat the
                signal; defaults to 1

        """
        self.signal = [int(s) for s in str(signal)] * repeat
        self.half_signal = self.signal[len(self.signal) // 2:]
        self.phases = phases
        self.bound = len(self.signal) + 1
        self.pattern = [0, 1, 0, -1]
        self.indices = []
        indices = list(range(self.bound - 1))
        for n, _ in enumerate(self.signal, start=1):
            pattern = indices[n - 1::n * 4]
            self.indices.append(pattern)

    def run(self) -> List[int]:
        """Run the algorithm with initial values until `phases` is
        reached.

        Returns:
            List[int]: the signal in list form, up to the 8th index

        """
        for _ in range(self.phases):
            signal = []
            for n, _ in enumerate(self.signal, start=1):
                s = 0
                offset = n
                for index in self.indices[n - 1]:
                    s += sum(self.signal[index:index + offset])
                    negative = index + 2 * n
                    if negative < len(self.signal):
                        s -= sum(self.signal[negative:negative + offset])
                signal.append(abs(s) % 10)
            # for position in range(1, self.bound):
            #     pattern = self.patterns[position - 1] * bound
            #     pattern.pop(0)
            #     signal.append(
            #         abs(sum([s * p for s, p in zip(self.signal, pattern)])) % 10
            #         )
            self.signal = signal
        return self.signal[:8]

    def get_latter_signal_at(self, phase: int) -> List[int]:
        """Get the latter half of the signal at a specified `phase`.

        Args:
            phase (int): the phase to pick

        Returns:
            List[int]: the list of the latter half of the signal

        """
        for p in range(phase):
            for i in range(1, len(self.half_signal)):
                self.half_signal[-i - 1] += self.half_signal[-i]
                self.half_signal[-i - 1] %= 10

        return self.half_signal
