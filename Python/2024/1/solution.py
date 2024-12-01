from collections import defaultdict

input = open("input.txt").read().strip()

def parse_input(input: str) -> list[list[str]]:
    lines = [[int(t) for t in x.strip().split(" ") if t != ''] for x in input.split("\n")]
    l1 = sorted([l[0] for l in lines])
    l2 = sorted([l[1] for l in lines])
    assert len(l1) == len(l2)

    return l1, l2

def part1(input: str) -> int:
    l1, l2 = parse_input(input)
    total = 0

    for a, b in list(zip(l1, l2)):
        total += abs(a - b)

    return total

def part2(input: str) -> int:
    l1, l2 = parse_input(input)
    counts = defaultdict(int)

    for l in l2:
        counts[l] += 1

    total = 0

    for l in l1:
        if counts[l] != 0:
            total += l * counts[l]

    return total

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















