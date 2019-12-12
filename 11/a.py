import painter


def main() -> None:
    """Processes inputs."""
    with open('input', 'r') as f:
        interpreter = painter.Painter(
            f.read().strip().split(','),
            silent=True
            )
    interpreter.run_ops()
    print(len(interpreter.map))


if __name__ == '__main__':
    main()
