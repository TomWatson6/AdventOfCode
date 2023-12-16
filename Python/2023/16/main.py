import sys
sys.setrecursionlimit(int(1e9))

with open(0) as f:
    lines = [x.strip() for x in f.readlines()]

def next(grid, ray):
    pos, d = ray

    n = (pos[0] + D[d % len(D)][0], pos[1] + D[d % len(D)][1])

    if n[0] < 0 or n[0] >= len(grid) or n[1] < 0 or n[1] >= len(grid[0]):
        return []

    if grid[n[0]][n[1]] == '/':
        if d % len(D) in [0, 2]:
            d += 1
        else:
            d -= 1
    elif grid[n[0]][n[1]] == '\\':
        if d % len(D) in [0, 2]:
            d -= 1
        else:
            d += 1
    elif grid[n[0]][n[1]] == '-' and d % len(D) in [0, 2]:
        return [(n, 1), (n, 3)]
    elif grid[n[0]][n[1]] == '|' and d % len(D) in [1, 3]:
        return [(n, 0), (n, 2)]

    return [(n, d)]

def print_grid(grid, visited):
    for r in range(len(grid)):
        out = ""
        for c in range(len(grid[0])):
            if (r, c) in visited and grid[r][c] not in ['\\', '/', '|', '-']:
                out += "X"
            else:
                out += grid[r][c]

        print(out)

    print()

def trace(grid, ray, seen, states):
    n = next(grid, ray)
    if len(n) == 0:
        return 0

    if len(n) == 1 and n[0] in states:
        return 0

    total = 0

    if n[0][0] not in seen:
        total += 1

    for a in n:
        if a not in states:
            states.add(a)
            seen.add(a[0])

            total += trace(grid, a, seen, states)

    return total

grid = [list(x) for x in lines]

D = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]

R = len(grid)
C = len(grid[0])

rays = []

rays += [((x, -1), 1) for x in range(R)]
rays += [((x, C), 3) for x in range(R)]
rays += [((-1, x), 2) for x in range(C)]
rays += [((R, x), 0) for x in range(C)]

p1 = 0
p2 = 0

for i, ray in enumerate(rays):
    visited = trace(grid, ray, set(), set())
    if i == 0:
        p1 = visited

    p2 = max(p2, visited)

print("Part 1:", p1)
print("Part 2:", p2)



















