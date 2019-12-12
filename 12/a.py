from moon import Moon


def main() -> None:
    """Processes inputs."""
    moons = []
    with open('input', 'r') as f:
        text = f.read().strip()

    for t in text.split('\n'):
        moons.append(Moon(t))

    for _ in range(1000):
        for moon_a in moons:
            for moon_b in moons:
                if moon_a == moon_b:
                    continue
                moon_a.get_velocity(moon_b)

        for moon in moons:
            moon.move()

    total_energy = 0
    for moon in moons:
        total_energy += moon.total_energy

    print(total_energy)


if __name__ == '__main__':
    main()
