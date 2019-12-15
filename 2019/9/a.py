import intcode

INPUTS = [
    # Output: a copy of itself
    [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99],
    # Output: 16 digit number
    [1102,34915192,34915192,7,4,7,99,0],
    # Output: 1125899906842624
    [104,1125899906842624,99],
    ]


def main() -> None:
    """Processes inputs."""
    # for i in INPUTS:
    #     interpreter = intcode.Interpreter(i, silent=False)
    #     interpreter.run_ops()

    with open('input', 'r') as f:
        interpreter = intcode.Interpreter(
            f.read().strip().split(','),
            silent=False
            )
        interpreter.run_ops()


if __name__ == '__main__':
    main()
