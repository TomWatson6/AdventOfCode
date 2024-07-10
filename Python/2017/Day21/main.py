import math

start = """.#.
..#
###
""".split("\n")

start = [x for x in start if x != '']

def split_grid(grid):
    if len(grid) % 2 == 0:
        inc = 2
    else:
        inc = 3

    grids = []

    for r in range(0, len(grid), inc):
        for c in range(0, len(grid[0]), inc):
            grids.append(["".join([grid[rr][cc] for cc in range(c, c + inc)]) for rr in range(r, r + inc)])

    return grids

def assemble(grids):
    grid = []

    if len(grids) == 1:
        return grids[0]

    size = int(math.sqrt(len(grids)))
    assert size**2 == len(grids)

    for r in range(size):
        for i in range(len(grids[0])):
            row = ""
            for c in range(size):
                for j in range(len(grids[0][0])):
                    row += grids[r * size + c][i][j]

            grid.append(row)

    return grid

M = {}

def evolve(grids):
    new_grids = []

    for grid in grids:
        new_grids.append(M["/".join(grid)].split("/"))

    return new_grids

def variations(pattern):
    pattern = pattern.split("/")
    variations = set()

    for _ in range(4):
        variations.add("/".join(pattern))
        pattern = ["".join(reversed(x)) for x in zip(*pattern)]

    pattern = pattern[::-1]

    for _ in range(4):
        variations.add("/".join(pattern))
        pattern = ["".join(reversed(x)) for x in zip(*pattern)]

    return list(variations)

with open(0) as f:
    lines = [x.strip().split(" => ") for x in f.readlines()]

for before, after in lines:
    for v in variations(before):
        M[v] = after

grid = start[:]

def count_on(grid):
    total = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '#':
                total += 1

    return total

for i in range(18):
    grids = split_grid(grid)
    grids = evolve(grids)
    grid = assemble(grids)

    if i == 4:
        print("Part 1:", count_on(grid))

total = count_on(grid)

print("Part 2:", total)




















