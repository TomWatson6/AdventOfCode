from collections import defaultdict

input = open("input.txt").read().strip()

#1 @ 167,777: 23x12
#2 @ 253,106: 10x25
#3 @ 104,622: 11x25
#4 @ 267,61: 14x16
#5 @ 829,831: 19x10
#6 @ 886,374: 22x12
#7 @ 129,812: 18x17
#8 @ 972,677: 14x17
#9 @ 123,249: 12x14
#10 @ 669,330: 11x21

def parse(input: str):
    return input.splitlines()

def part1(input: str) -> int:
    lines = parse(input)
    grid = defaultdict(int)
    overlaps = 0

    for i, (coord, dimensions) in enumerate([l.split('@ ')[1].split(": ") for l in lines]):
        x, y = list(map(int, coord.split(',')))
        width, height = list(map(int, dimensions.split('x')))

        for yy in range(y, y + height):
            for xx in range(x, x + width):
                if (xx, yy) in grid and grid[(xx, yy)] == 1:
                    overlaps += 1

                grid[(xx, yy)] += 1

    return overlaps

def part2(input: str) -> int:
    lines = parse(input)
    fabrics = []

    for i, (coord, dimensions) in enumerate([l.split('@ ')[1].split(": ") for l in lines]):
        fabric = set()
        x, y = list(map(int, coord.split(',')))
        width, height = list(map(int, dimensions.split('x')))

        for yy in range(y, y + height):
            for xx in range(x, x + width):
                fabric.add((xx, yy))

        fabrics.append(fabric)

    for i, f in enumerate(fabrics):
        others = [o for o in fabrics if o != f]
        if all(len(f & o) == 0 for o in others):
            return i + 1

    return -1

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















