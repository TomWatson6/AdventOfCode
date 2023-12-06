
with open(0) as f:
    input = f.read().strip()

seeds = list(map(int, input.split("\n")[0].split(" ")[1:]))
M = []

for chunk in input.split("\n\n")[1:]:
    for i, line in enumerate(chunk.split("\n")):
        if i == 0:
            M.append([])
            continue
        dest, start, ran = list(map(int, line.split()))
        M[-1].append((dest, start, ran))

def map_seeds(seeds, mapping):
    mapped = []

    while len(seeds) > 0:
        lower, upper = seeds.pop()

        for dest, source, ran in mapping:
            o_low = max(lower, source)
            o_high = min(upper, source + ran)

            if o_low < o_high:
                mapped.append((o_low - source + dest, o_high - source + dest))

                if o_low > lower:
                    seeds.append((lower, o_low))

                if upper > o_high:
                    seeds.append((o_high, upper))

                break
        else:
            mapped.append((lower, upper))

    return mapped

def lowest_loc(pairs, maps):
    for mapping in maps:
        pairs = map_seeds(pairs, mapping)

    return min(x[0] for x in pairs)

pairs = [(x, x + 1) for x in seeds]

print("Part 1:", lowest_loc(pairs, M))

pairs = []

for i in range(0, len(seeds), 2):
    pairs.append((seeds[i], seeds[i] + seeds[i + 1]))

print("Part 2:", lowest_loc(pairs, M))


















