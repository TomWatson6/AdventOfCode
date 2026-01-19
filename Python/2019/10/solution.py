from math import gcd
from collections import defaultdict

input = open("input.txt").read().strip()

R = 0
C = 0

def parse(input: str):
    global R, C

    grid = [[ch == '#' for ch in row] for row in input.splitlines()]

    R = len(grid)
    C = len(grid[0])

    return grid

def normalise(coord):
    d = gcd(coord[0], coord[1])
    if d == 0:
        return (1, 0)
    return (coord[0] // d, coord[1] // d)

station = (0, 0)
best = 0
best_coords = set()

def part1(input: str) -> int:
    global station, best, best_coords
    grid = parse(input)

    asteroids = []

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch:
                asteroids.append((r, c))

    for r1, c1 in asteroids:
        seen = set()

        for r2, c2 in asteroids:
            if r1 == r2 and c1 == c2:
                continue

            rr = r1 - r2
            cc = c1 - c2
            d = gcd(rr, cc)

            seen.add((rr // d, cc // d))

        if len(seen) > best:
            best = len(seen)
            best_coords = set(seen)
            station = (rr, cc)

    return best

def vaporise(grid, count):
    global best_coords
    r, c = station

    top = [(r, c) for r, c in best_coords if r < 0 and c == 0]
    top_right = sorted([(r, c) for r, c in best_coords if r < 0 and c > 0], key = lambda k: k[1] / k[0], reverse = True)
    right = [(r, c) for r, c in best_coords if r == 0 and c > 0]
    bottom_right = sorted([(r, c) for r, c in best_coords if r > 0 and c > 0], key = lambda k: k[1] / k[0], reverse = True)
    bottom = [(r, c) for r, c in best_coords if r > 0 and c == 0]
    bottom_left = sorted([(r, c) for r, c in best_coords if r > 0 and c < 0], key = lambda k: k[1] / k[0], reverse = True)
    left = [(r, c) for r, c in best_coords if r == 0 and c < 0]
    top_left = sorted([(r, c) for r, c in best_coords if r < 0 and c < 0], key = lambda k: k[1] / k[0], reverse = True)

    coords = [*top, *top_right, *right, *bottom_right, *bottom, *bottom_left, *left, *top_left]

    rr, cc = coords[count]

    print(len(top), len(top_right), len(right), len(bottom_right), len(bottom), len(bottom_left), len(left), len(top_left))
    print(coords)
    print(coords[count - 1: count + 2])
    
    rr -= r
    cc -= c

    return cc * 100 + rr

def part2(input: str) -> int:
    grid = parse(input)

    output = vaporise(grid, 200)

    return output

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















