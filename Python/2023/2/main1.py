with open(0) as f:
    lines = f.readlines()

print(
    sum(
        [
            b[0] + 1 for b in enumerate(
                [
                    {
                        d[1]: int(d[0]) for d in
                        [
                            a.split(" ") for a in z.split(", ")
                        ]
                    } for z in y[1].split("; ")
                ] for y in
                [
                    x.strip().split(": ") for x in lines
                ]
            ) if all(
                [
                    max(c['red'] if 'red' in c else 0 for c in b[1]) <= 12,
                    max(c['green'] if 'green' in c else 0 for c in b[1]) <= 13,
                    max(c['blue'] if 'blue' in c else 0 for c in b[1]) <= 14
                ]
            )
        ]
    ),
    sum(
        [
            max([x[0] for x in t]) *
            max([x[1] for x in t]) *
            max([x[2] for x in t])
            for t in
            [
                [
                    [
                        c['red'] if 'red' in c else 0,
                        c['green'] if 'green' in c else 0,
                        c['blue'] if 'blue' in c else 0
                    ]
                    for c in
                    [
                        {
                            d[1]: int(d[0]) for d in
                            [
                                a.split(" ") for a in z.split(", ")
                            ]
                        } for z in y[1].split("; ")
                    ]
                ] for y in
                [
                    x.strip().split(": ") for x in lines
                ]
            ]
        ]
    )
)










