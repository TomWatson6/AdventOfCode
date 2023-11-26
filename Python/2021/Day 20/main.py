
from collections import defaultdict

def print_grid(grid):
    x_low = min(grid.keys(), key=lambda k: k[0])[0]
    x_high = max(grid.keys(), key=lambda k: k[0])[0]
    y_low = min(grid.keys(), key=lambda k: k[1])[1]
    y_high = max(grid.keys(), key=lambda k: k[1])[1]
    
    for r in range(x_low, x_high, 1):
        for c in range(y_low, y_high, 1):
            print('#' if grid.get((r, c)) else ' ', end='')
        print()

def evolve(grid, lookup, x_low, x_high, y_low, y_high):
    x_low -= 3
    x_high += 3
    y_low -= 3
    y_high += 3        

    evolved = dict()

    for r in range(x_low, x_high, 1):
        for c in range(y_low, y_high, 1):
            binary = ""
            for rr in [-1, 0, 1]:
                for cc in [-1, 0, 1]:
                    if grid.get((r + rr, c + cc)):
                        binary += '1'
                    else:
                        binary += '0'
            binary = int(binary, 2)
            evolved[(r, c)] = lookup[binary] == '#'

    evolved2 = dict()

    for r in range(x_low, x_high, 1):
        for c in range(y_low, y_high, 1):
            if r == x_low or r == x_high - 1 or c == y_low or c == y_high - 1:
                continue

            binary = ""
            for rr in [-1, 0, 1]:
                for cc in [-1, 0, 1]:
                    if evolved.get((r + rr, c + cc)):
                        binary += '1'
                    else:
                        binary += '0'
            binary = int(binary, 2)
            evolved2[(r, c)] = lookup[binary] == '#'

    return evolved2 

def p1(output):
    print("Part 1:", output)

def p2(output):
    print("Part 2:", output)

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

lookup = []
i = 0

while True:
    if lines[i] == '':
        break
    lookup.append(lines[i])
    i += 1

lookup = "".join(lookup)
lines = lines[i + 1:]

assert len(lookup) == 512

grid = dict()
grid2 = dict()
dim_y = len(lines)
dim_x = len(lines[0])

x_low = 0
y_low = 0
x_high = len(lines)
y_high = len(lines[0])

for r in range(len(lines)):
    for c in range(len(lines[0])):
        if lines[r][c] == '#':
            grid[(r, c)] = True

for r in range(len(lines)):
    for c in range(len(lines[0])):
        if lines[r][c] == '#':
            grid2[(r, c)] = True

grid = evolve(grid, lookup, x_low, x_high, y_low, y_high)

total = 0

for v in grid.values():
    if v:
        total += 1

p1(total)

for i in range(25):
    grid2 = evolve(grid2, lookup, x_low, x_high, y_low, y_high)
    x_low -= 3
    x_high += 3
    y_low -= 3
    y_high += 3

total = 0

for v in grid2.values():
    if v:
        total += 1

p2(total)

