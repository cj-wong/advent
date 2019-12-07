from collections import defaultdict

import intcode

PHASE_MAX = 1
# phase = range(0, PHASE_MAX + 1)


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
    signal = defaultdict(int)
    for phases, ops in INPUTS:
        interpreter = intcode.Interpreter(ops)
        interpreter.save_state()
        previous = 0
        for phase in phases:
            interpreter.store_phases(phase, previous)
            interpreter.run_ops(silent=True)
            previous = interpreter.previous
            interpreter.restore_state()
        print(previous)
    # with open('input', 'r') as f:
    #     interpreter = intcode.Interpreter(
    #         f.read().split(',')
    #         )
    #     interpreter.save_state()
    # for a in range(0, PHASE_MAX):
    #     for b in range(0, PHASE_MAX):
    #         for c in range(0, PHASE_MAX):
    #             for d in range(0, PHASE_MAX):
    #                 for e in range(0, PHASE_MAX):
    #                     interpreter.store_phases([a, b, c, d, e])
    #                     interpreter.run_ops()
    #                     interpreter.restore_state()


if __name__ == '__main__':
    main()
