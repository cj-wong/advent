from collections import defaultdict
from typing import List

import amplifier


PHASE_MIN = 0
PHASE_MAX = 4 + 1 # 0 <= phase <= 4

INPUTS = [
    # Signal: 43210
    (
        [4, 3, 2, 1, 0],
        [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
        ),
    # Signal: 54321
    (
        [0, 1, 2, 3, 4],
        [
            3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23,
            1, 24, 23, 23, 4, 23, 99, 0, 0
            ]
        ),
    # Signal: 65210
    (
        [1, 0, 4, 3, 2],
        [
            3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 
            1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0
            ]
        )
    ]


def iterate(ops: List[int], phases: List[int] = None) -> None:
    """Iterate through operators `ops`.

    Args:
        ops (List[int]): list of operators/operands
        phases (List[int], optional): a specific phase setting to try;
            defaults to None; if not defined, iterate will try every
            possible combination defined by PHASE_MIN and PHASE_MAX

    """
    if phases:
        interpreter = amplifier.Controller(ops, phases)
        print(interpreter.run())
        return

    signals = defaultdict(int)
    for a in range(PHASE_MIN, PHASE_MAX):
        for b in range(PHASE_MIN, PHASE_MAX):
            if b in [a]:
                continue
            for c in range(PHASE_MIN, PHASE_MAX):
                if c in [a, b]:
                    continue
                for d in range(PHASE_MIN, PHASE_MAX):
                    if d in [a, b, c]:
                        continue
                    for e in range(PHASE_MIN, PHASE_MAX):
                        if e in [a, b, c, d]:
                            continue
                        interpreter = amplifier.Controller(
                            ops, [a, b, c, d, e]
                            )
                        signals[(a, b, c, d, e)] = interpreter.run()

    print('Maximum signal:', max(signals.values()))


def main() -> None:
    """Processes inputs."""
    # for phases, ops in INPUTS:
    #     iterate(ops, phases)

    with open('input', 'r') as f:
        iterate(f.read().strip().split(','))


if __name__ == '__main__':
    main()
