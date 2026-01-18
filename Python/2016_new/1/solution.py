
input = open("input.txt").read().strip()

def parse(input: str):
    return input.split(", ")

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def part1(input: str) -> int:
    d = 0
    pos = (0, 0)
    moves = parse(input)

    for di, amt in [(x[0], x[1:]) for x in moves]:
        if di == 'R':
            d = (d + 1) % len(DIRS)
        else:
            d = (d - 1) % len(DIRS)

        di = DIRS[d]

        pos = (pos[0] + di[0] * int(amt), pos[1] + di[1] * int(amt))

    return abs(pos[0]) + abs(pos[1])

def part2(input: str) -> int:
    d = 0
    pos = (0, 0)
    moves = parse(input)
    seen = set()
    seen.add((0, 0))

    for di, amt in [(x[0], x[1:]) for x in moves]:
        if di == 'R':
            d = (d + 1) % len(DIRS)
        else:
            d = (d - 1) % len(DIRS)

        di = DIRS[d]

        for _ in range(int(amt)):
            pos = (pos[0] + di[0], pos[1] + di[1])
            if pos in seen:
                return abs(pos[0]) + abs(pos[1])
            seen.add(pos)

    return 0

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















