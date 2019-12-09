from collections import defaultdict
from typing import List

import amplifier


PHASE_MAX = 9 + 1 # 5 <= phase <= 9
PHASE_MIN = 5

INPUTS = [
    # Signal: 139629729
    (
        [9, 8, 7, 6, 5],
        [
            3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
            27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5
            ]
        ),
    # Signal: 18216
    (
        [9, 7, 8, 5, 6],
        [
            3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55,
            1005, 55, 26, 1001, 54, -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008,
            54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4, 53, 1001, 56, -1, 56,
            1005, 56, 6, 99, 0, 0, 0, 0, 10
            ]
        ),
    ]


def iterate(ops: List[int], phases: List[int] = None) -> None:
    """Iterate through operators `ops`.

    Args:
        ops (List[int]): list of operators/operands
        phases (List[int], optional): a specific phase setting to try;
            defaults to None; if not defined, iterate will try every
            possible combination defined by PHASE_MIN and PHASE_MAX

    """
    signal = 0
    if phases:
        interpreter = amplifier.Cluster(ops, phases)
        interpreter.run()
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
                        interpreter = amplifier.Cluster(
                            ops, [a, b, c, d, e]
                            )
                        signals[(a, b, c, d, e)] = interpreter.run()

    print(max(signals.values()))


def main() -> None:
    """Processes inputs."""
    # for phases, ops in INPUTS:
    #     iterate(ops, phases)

    with open('input', 'r') as f:
        iterate(f.read().strip().split(','))


if __name__ == '__main__':
    main()
