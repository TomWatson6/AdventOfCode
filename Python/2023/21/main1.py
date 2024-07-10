from collections import deque
import sys

sys.setrecursionlimit(int(1e9))

with open(0) as f:
    grid = [list(x.strip()) for x in f.readlines()]

R = len(grid)
C = len(grid[0])
S = (0, 0)

for r in range(R):
    found = False
    for c in range(C):
        if grid[r][c] == 'S':
            S = (r, c)
            found = True
            break
    if found:
        break

assert found
print("Start:", S)

DP = {}

def dfs(start, steps):
    r, c = start
    if (start, steps) in DP:
        return DP[(start, steps)]

    if steps == 0:
        return set([start])

    locations = set()

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        rr = r + dr
        cc = c + dc

        if 0 <= rr < R and 0 <= cc < C and grid[rr][cc] != '#':
            locations |= dfs((rr, cc), steps - 1)

    DP[(start, steps)] = locations

    return locations


print(len(dfs(S, 64)))

total_steps = 26501365

def bfs(start):
    Q = deque([(start, 0, 0, 0)])
    S = set()
    paths = {}

    while Q:
        (r, c), steps, gr, gc = Q.popleft()
        if (r, c) == start:
            print(paths, r, c, steps, gr, gc)

        if (r, c) == start and (gr, gc) not in paths and (gr, gc) != (0, 0):
            paths[(gr, gc)] = steps

        if len(paths) == 8:
            break

        if (r, c, gr, gc) in S:
            continue

        S.add((r, c, gr, gc))

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rr = r + dr
            cc = c + dc

            if rr < 0:
                rr %= R
                if grid[rr][cc] != '#':
                    Q.append(((rr, cc), steps + 1, gr - 1, gc))
                continue
            if rr >= R:
                rr %= R
                if grid[rr][cc] != '#':
                    Q.append(((rr, cc), steps + 1, gr + 1, gc))
                continue
            if cc < 0:
                cc %= C
                if grid[rr][cc] != '#':
                    Q.append(((rr, cc), steps + 1, gr, gc - 1))
                continue
            if cc >= C:
                cc %= C
                if grid[rr][cc] != '#':
                    Q.append(((rr, cc), steps + 1, gr, gc + 1))
                continue

            if grid[rr][cc] != '#':
                Q.append(((rr, cc), steps + 1, gr, gc))

    return [(k[0], k[1], v) for k, v in paths.items()]

paths = bfs(S)
smallest = int(1e16)

def find_tiles(start, paths):
    global smallest
    Q = deque([(0, 0, total_steps)])
    S = set()
    i = 0

    while Q:
        i += 1
        if i % 1000000 == 0:
            print(smallest, len(paths), paths[0])
        r, c, d = Q.popleft()

        if d < smallest:
            smallest = d

        if (r, c) in S:
            continue

        S.add((r, c))

        paths = [(r, c, total_steps - d)] + paths

        for dr, dc, cost in paths:
            rr = r + dr
            cc = c + dc
            if (rr, cc) in S:
                continue

            if cost <= d:
                Q.append((rr, cc, d - cost))

    print(len(S))

find_tiles(S, paths)












