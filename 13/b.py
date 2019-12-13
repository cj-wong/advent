import arcade


def main() -> None:
    """Processes inputs."""
    with open('input', 'r') as f:
        interpreter = arcade.Game(
            f.read().strip().split(','),
            silent=True
            )
        interpreter.insert_quarters()
        interpreter.run_ops()


if __name__ == '__main__':
    main()
