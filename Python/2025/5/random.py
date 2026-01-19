
input = open("input.txt").read().strip()

def parse(input: str):
    ranges, ingredients = input.split("\n\n")
    ranges = [list(map(int, x)) for x in [y.split("-") for y in ranges.splitlines()]]
    ingredients = [int(x) for x in ingredients.splitlines()]

    return ranges, ingredients

def combine(r1, r2):
    r1_low, r1_high = r1
    r2_low, r2_high = r2

    # Engulfed
    if r1_low <= r2_low <= r2_high <= r1_high:
        return [r1]

    if r2_low <= r1_low <= r1_high <= r2_high:
        return [r2]

    # Overlapping
    if r1_low <= r2_low <= r1_high <= r2_high:
        return [[r1_low, r2_high]]

    if r2_low <= r1_low <= r2_high <= r1_high:
        return [[r2_low, r1_high]]

    # Non Overlapping
    if r1_high < r2_low or r2_high < r1_low:
        return [r1, r2]

    exit(-1)

def part1(input: str) -> int:
    ranges, ingredients = parse(input)
    total = 0

    for ingredient in ingredients:
        if any(lower <= ingredient <= upper for lower, upper in ranges):
            total += 1

    return total

def part2(input: str) -> int:
    ranges, _ = parse(input)

    i = 0
    j = 1

    ranges = sorted(ranges, key = lambda k: k[0])

    while i != len(ranges) - 1:
        result = combine(ranges[i], ranges[j])

        if len(result) == 1:
            ranges.remove(ranges[j])
            ranges.remove(ranges[i])
            ranges.append(result[0])

            i = 0
            j = i + 1

            continue

        if j == len(ranges) - 1:
            i += 1
            j = i + 1
        else:
            j += 1

    return sum(upper - lower + 1 for lower, upper in ranges)

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















