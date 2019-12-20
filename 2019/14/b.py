import math

import nanofactory


INPUTS = [
    [   # ORE: 13312
        '157 ORE => 5 NZVS',
        '165 ORE => 6 DCFZ',
        '44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL',
        '12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ',
        '179 ORE => 7 PSHF',
        '177 ORE => 5 HKGWZ',
        '7 DCFZ, 7 PSHF => 2 XJWVT',
        '165 ORE => 2 GPVTF',
        '3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT',
        ],
    [   # ORE: 2210736
        '171 ORE => 8 CNZTR',
        '7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL',
        '114 ORE => 4 BHXH',
        '14 VRPVC => 6 BMBT',
        '6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL',
        '6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT',
        '15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW',
        '13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW',
        '5 BMBT => 4 WPTQ',
        '189 ORE => 9 KTJDG',
        '1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP',
        '12 VRPVC, 27 CNZTR => 2 XDBXC',
        '15 KTJDG, 12 BHXH => 5 XCVML',
        '3 BHXH, 2 VRPVC => 7 MZWV',
        '121 ORE => 7 VRPVC',
        '7 XCVML => 6 RJRHP',
        '5 BHXH, 4 VRPVC => 5 LTCX',
        ]
    ]

OUTPUTS = [
    82_892_753, #13312,
    460_664, #2210736,
    ]

LIMIT = 1_000_000_000_000


def search_from(nf: nanofactory.Nanofactory, low: int) -> int:
    """Search `nf` starting from `low`, up to a derived `high`. Repeat
    the process as a binary search until `LIMIT` is found or as close
    to `LIMIT` as possible.

    Args:
        nf (nanofactory.Nanofactory): the nanofactory
        low (int): generated from `LIMIT // ore` where `ore` is the
            amount of 'ORE' needed to create 1 'FUEL'

    """
    # Set bounds. To derive `upper_bound`, add 10 to the same magnitude
    # as low. If this is too low, keep adding 10 of the same magnitude.
    offset = 10 ** int(math.log10(low))
    high = low + offset
    lower_bound = nf.solve(qty=low)
    upper_bound = nf.solve(qty=high)
    while upper_bound < LIMIT:
        high += offset
        upper_bound = nf.solve(qty=high)

    n = low

    while True:
        ore = nf.solve(qty=n)
        if ore == LIMIT:
            return n
        # Because we only use integers, at one point `low` will be
        # under LIMIT (above conditional) but `high` will be over it.
        elif low == high - 1:
            return low

        if ore < LIMIT:
            low = n
            lower_bound = ore
        else:
            high = n
            upper_bound = ore

        n = (high + low) // 2


def main() -> None:
    """Processes inputs."""
    # for i, o in zip(INPUTS, OUTPUTS):
    #     nf = nanofactory.Nanofactory(i)
    #     ore = nf.solve()
    #     print(search_from(nf, LIMIT // ore))
    #     print('Expected output:', o)

    with open('input', 'r') as f:
        nf = nanofactory.Nanofactory(
            f.read().strip().split('\n')
            )
    ore = nf.solve()
    print(search_from(nf, LIMIT // ore))


if __name__ == '__main__':
    main()
