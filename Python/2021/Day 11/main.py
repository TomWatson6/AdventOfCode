

def flash(grid, coord, flashed):
    affected = []
    for r in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            if r == c == 0:
                continue
            row = coord[0] + r
            column = coord[1] + c
            if 0 <= row < len(grid) and 0 <= column < len(grid[0]):
                if (row, column) not in flashed:
                    grid[row][column] += 1

def print_grid(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            print(grid[r][c], end="")
        print()
    print()

def p1(output):
    print("Part 1:", output)

def p2(output):
    print("Part 2:", output)

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

grid = [list(x) for x in lines]
grid = [[int(x) for x in line] for line in lines]

steps = 100
flashes = 0

for step in range(steps):
    flashed = set()

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] += 1

    snapshot = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] > 9:
                snapshot.append([r, c])

    while len(snapshot) > 0:
        for r, c in snapshot:
            flash(grid, [r, c], flashed)
            flashed.add((r, c))
            flashes += 1
        for r, c in snapshot:
            grid[r][c] = 0
        snapshot = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] > 9:
                    snapshot.append([r, c])

p1(flashes)

grid = [list(x) for x in lines]
grid = [[int(x) for x in line] for line in lines]

flashed = set()
octopuses = sum([len(x) for x in grid])
steps = 0

while len(flashed) != octopuses:
    flashed = set()

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] += 1

    snapshot = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] > 9:
                snapshot.append([r, c])

    while len(snapshot) > 0:
        for r, c in snapshot:
            flash(grid, [r, c], flashed)
            flashed.add((r, c))
            flashes += 1
        for r, c in snapshot:
            grid[r][c] = 0
        snapshot = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] > 9:
                    snapshot.append([r, c])
    steps += 1

p2(steps)