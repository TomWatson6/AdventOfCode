from copy import deepcopy

X_MIN = 0
X_MAX = 0
Y_MIN = 0
Y_MAX = 0

def neighbours_on(grid, coord):
    total = 0

    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == 0 and y == 0:
                continue

            c = (coord[0] + x, coord[1] + y)
            if c in grid:
                if grid[c] == '#':
                    total += 1

    return total

def evolve(grid, part2):
    new_grid = {}

    for k, v in grid.items():
        if part2 and k in ((X_MIN, Y_MIN), (X_MIN, Y_MAX), (X_MAX, Y_MIN), (X_MAX, Y_MAX)):
            new_grid[k] = '#'
            continue

        neighbours = neighbours_on(grid, k)
        if v == '#':
            if neighbours in [2, 3]:
                new_grid[k] = '#'
            else:
                new_grid[k] = '.'
        else:
            if neighbours == 3:
                new_grid[k] = '#'
            else:
                new_grid[k] = '.'

    return new_grid

def output(grid):

    for y in range(0, Y_MAX + 1):
        for x in range(0, X_MAX + 1):
            print(grid[(x, y)], end="")
        print()
    print()

        


with open("input.txt") as f:
    input = [[y for y in x if y != "\n"] for x in f.readlines()]

grid = {}

for y, line in enumerate(input):
    for x, char in enumerate(line):
        grid[(x, y)] = char

X_MAX = max(grid.keys(), key=lambda k: k[0])[0]
Y_MAX = max(grid.keys(), key=lambda k: k[1])[1]

grid1 = deepcopy(grid)

for _ in range(100):
    grid1 = evolve(grid1, False)

total = 0

for k, v in grid1.items():
    if v == '#':
        total += 1

print("Part 1: {}".format(total))

grid[(X_MIN, Y_MIN)] = '#'
grid[(X_MIN, Y_MAX)] = '#'
grid[(X_MAX, Y_MIN)] = '#'
grid[(X_MAX, Y_MAX)] = '#'

for _ in range(100):
    grid = evolve(grid, True)

total = 0

for k, v in grid.items():
    if v == '#':
        total += 1

print("Part 2: {}".format(total))



