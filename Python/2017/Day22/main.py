
with open(0) as f:
    lines = [list(x.strip()) for x in f.readlines()]

grid = lines[:]
R = len(grid)
C = len(grid[0])

D = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]

sr, sc = R // 2, C // 2
r = R // 2
c = C // 2
d = 0

new_grid = set()

for rr in range(R):
    for cc in range(C):
        if grid[rr][cc] == '#':
            new_grid.add((rr, cc))

grid = new_grid

infections = 0

for i in range(10000):
    if (r, c) in grid:
        d = (d + 1) % len(D)
        grid.remove((r, c))
    else:
        d = (d - 1) % len(D)
        infections += 1
        grid.add((r, c))

    r, c = (r + D[d][0], c + D[d][1])

print("Part 1:", infections)

r, c, d = int(sr), int(sc), 0

grid = lines
new_grid = {}

for rr in range(R):
    for cc in range(C):
        if grid[rr][cc] == '#':
            new_grid[(rr, cc)] = 2
        else:
            new_grid[(rr, cc)] = 0

grid = new_grid
infections = 0

for i in range(10000000):
    if (r, c) not in grid:
        d = (d - 1) % len(D)
        grid[(r, c)] = 1
        r, c = (r + D[d][0], c + D[d][1])
        continue

    if grid[(r, c)] == 0:
        d = (d - 1) % len(D)
        grid[(r, c)] = 1
        r, c = (r + D[d][0], c + D[d][1])
        continue

    if grid[(r, c)] == 1:
        grid[(r, c)] = 2
        infections += 1
        r, c = (r + D[d][0], c + D[d][1])
        continue

    if grid[(r, c)] == 2:
        d = (d + 1) % len(D)
        grid[(r, c)] = 3
        r, c = (r + D[d][0], c + D[d][1])
        continue

    if grid[(r, c)] == 3:
        d = (d + 2) % len(D)
        grid[(r, c)] = 0
        r, c = (r + D[d][0], c + D[d][1])



print("Part 2:", infections)














