from collections import Counter

input = open("input.txt").read().strip()

def parse(input: str):
    return input.splitlines()

def part1(input: str) -> int:
    lines = parse(input)
    columns = list(zip(*lines))
    counts = [Counter(x) for x in columns]

    most_common = "".join([max(c.items(), key = lambda k: k[1])[0] for c in counts])

    return most_common

def part2(input: str) -> int:
    lines = parse(input)
    columns = list(zip(*lines))
    counts = [Counter(x) for x in columns]

    least_common = "".join([min(c.items(), key = lambda k: k[1])[0] for c in counts])

    return least_common

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















