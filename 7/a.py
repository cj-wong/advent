from collections import defaultdict

import intcode


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


def main() -> None:
    """Processes inputs."""
    # for phases, ops in INPUTS:
    #     interpreter = intcode.Interpreter(ops)
    #     interpreter.save_state()
    #     signal = 0
    #     for phase in phases:
    #         interpreter.store_phases(phase, signal)
    #         interpreter.run_ops(silent=True)
    #         signal = interpreter.signal
    #         interpreter.restore_state()
    #     print(signal)
    signals = defaultdict(int)
    with open('input', 'r') as f:
        interpreter = intcode.Interpreter(
            f.read().strip().split(',')
            )
        interpreter.save_state()

    all_phases = [
        (a, b, c, d, e)
        for a in range(0, PHASE_MAX)
        for b in range(0, PHASE_MAX)
        for c in range(0, PHASE_MAX)
        for d in range(0, PHASE_MAX)
        for e in range(0, PHASE_MAX)
        ]

    for a in range(0, PHASE_MAX):
        for b in range(0, PHASE_MAX):
            if b == a:
                continue
            for c in range(0, PHASE_MAX):
                if c in [a, b]:
                    continue
                for d in range(0, PHASE_MAX):
                    if d in [a, b, c]:
                        continue
                    for e in range(0, PHASE_MAX):
                        if e in [a, b, c, d]:
                            continue
                        signal = 0
                        for phase in [a, b, c, d, e]:
                            interpreter.store_phases(phase, signal)
                            interpreter.run_ops(silent=True)
                            signal = interpreter.signal
                            interpreter.restore_state()
                        signals[(a, b, c, d, e)] = signal
    print(max(signals.values()))

if __name__ == '__main__':
    main()
