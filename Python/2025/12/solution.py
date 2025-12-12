from collections import deque

input = open("input.txt").read().strip()

def parse(input: str):
    global presents
    blocks = input.split("\n\n")

    presents = {}

    for block in blocks[:-1]:
        index = block[0].strip(":")
        grid = [list(x) for x in block.splitlines()[1:]]
        presents[int(index)] = grid

    regions = blocks[-1].splitlines()
    regions = [region.split(": ") for region in regions]
    regions = [(list(map(int, a.split("x"))), list(map(int, b.split()))) for a, b in regions]

    return regions

presents = {}

def part1(input: str) -> int:
    regions = parse(input)
    total = 0

    for r in regions:
        r_size = r[0][0] * r[0][1]
        p_size = 0

        for i, req in enumerate(r[1]):
            p = sum(sum(len(x) for x in row if x == '#') for row in presents[i])
            p_size += p * req

        if p_size * 1.2 < r_size:
            total += 1

    return total

def part2(input: str) -> int:
    return 0

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















