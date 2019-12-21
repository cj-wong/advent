from algorithms import FFT


INPUTS = [
    (12345678, 4),
    (80871224585914546619083218645595, 100),
    (19617804207202209144916044189917, 100),
    (69317163492948606335995924319873, 100),
    ]

OUTPUTS = [
    list('01029498'),
    list('24176176'),
    list('73745418'),
    list('52432133'),
    ]


def main() -> None:
    """Processes inputs."""
    # for (i, p), o in zip(INPUTS, OUTPUTS):
    #     f = FFT(i, p)
    #     print(f.run())
    #     print('Expected output:', o)

    with open('input', 'r') as f:
        f = FFT(f.read().strip(), 100)
    print(f.run())


if __name__ == '__main__':
    main()
