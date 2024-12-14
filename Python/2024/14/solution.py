import re
from collections import defaultdict

input = open("input.txt").read().strip()

def parse_robots(input: str) -> dict[tuple[int, int], list[tuple[int, int]]]:
    lines = input.splitlines()
    robots = defaultdict(list)

    for px, py, vx, vy in list(map(int, x) for x in list(re.findall(r"(-?\d+)", l) for l in lines)):
        robots[(px, py)].append((vx, vy))

    return robots

def move(robots, dim_x, dim_y, steps):
    new_robots = defaultdict(list)

    for (px, py), robs in robots.items():
        for vx, vy in robs:
            nx, ny = (px + vx * steps) % dim_x, (py + vy * steps) % dim_y
            new_robots[(nx, ny)].append((vx, vy))

    robots = new_robots

    return robots

def get_quadrants(robots, dim_x, dim_y):
    quads = [0, 0, 0, 0]

    for x in range(dim_x):
        for y in range(dim_y):
            if x < dim_x // 2 and y < dim_y // 2:
                quads[0] += len(robots[(x, y)])
            elif x > dim_x // 2 and y < dim_y // 2:
                quads[1] += len(robots[(x, y)])
            elif x < dim_x // 2 and y > dim_y // 2:
                quads[2] += len(robots[(x, y)])
            elif x > dim_x // 2 and y > dim_y // 2:
                quads[3] += len(robots[(x, y)])

    product = 1

    for q in quads:
        product *= q

    return product

def resembles_xmas_tree(robots, dim_x, dim_y):
    if not all(len(r) == 1 for r in robots.values()):
        return False

    return True

def part1(input: str, dim_x: int, dim_y: int) -> int:
    robots = parse_robots(input)

    robots = move(robots, dim_x, dim_y, 100)

    return get_quadrants(robots, dim_x, dim_y)

def part2(input: str, dim_x: int, dim_y: int) -> int:
    robots = parse_robots(input)
    i = 0

    while not resembles_xmas_tree(robots, dim_x, dim_y):
        robots = move(robots, dim_x, dim_y, 1)
        i += 1

    return i

if __name__ == "__main__":
    print("Part 1:", part1(input, 101, 103))
    print("Part 2:", part2(input, 101, 103))















