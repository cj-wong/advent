import robotics


def main() -> None:
    """Processes inputs."""
    with open('input', 'r') as f:
        interpreter = robotics.Painter(
            f.read().strip().split(','),
            silent=True
            )
    interpreter.init_panel(1)
    interpreter.run_ops()
    interpreter.render_map()


if __name__ == '__main__':
    main()
