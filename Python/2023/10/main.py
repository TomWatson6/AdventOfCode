from collections import deque
from copy import deepcopy
import sys

sys.setrecursionlimit(int(1e9))

def is_connecting(grid, before, after):
    r1, c1 = before
    r2, c2 = after

    if r2 < 0 or r2 >= R or c2 < 0 or c2 >= C:
        return False

    d = (0, 0)

    if r2 > r1:
        d = (1, d[1])
    elif r1 > r2:
        d = (-1, d[1])

    if c2 > c1:
        d = (d[0], 1)
    elif c1 > c2:
        d = (d[0], -1)

    # General connection to adjacent node
    if d == (-1, 0) and grid[r2][c2] in ['|', '7', 'F']:
        return True
    if d == (1, 0) and grid[r2][c2] in ['|', 'L', 'J']:
        return True
    if d == (0, -1) and grid[r2][c2] in ['-', 'L', 'F']:
        return True
    if d == (0, 1) and grid[r2][c2] in ['-', 'J', '7']:
        return True

    # Is valid adjacency to starting node
    if d == (-1, 0) and grid[r2][c2] == 'S' and grid[r1][c1] in ['|', 'L', 'J']:
        return True
    if d == (1, 0) and grid[r2][c2] == 'S' and grid[r1][c1] in ['|', '7', 'F']:
        return True
    if d == (0, -1) and grid[r2][c2] == 'S' and grid[r1][c1] in ['-', 'J', '7']:
        return True
    if d == (0, 1) and grid[r2][c2] == 'S' and grid[r1][c1] in ['-', 'L', 'F']:
        return True

    return False

def find_furthest_point(grid, pos, end, depth, visited):
    if pos == end and depth > 1:
        return [end], depth // 2

    if pos in visited:
        return None

    visited.add(pos)

    adj = [x for x in [(-1, 0), (1, 0), (0, -1), (0, 1)] if is_connecting(grid, (pos[0], pos[1]), (pos[0] + x[0], pos[1] + x[1]))]
    adj = [(pos[0] + x[0], pos[1] + x[1]) for x in adj]

    if depth < 2:
        adj = [x for x in adj if x != end]

    for a in adj:
        output = find_furthest_point(grid, a, end, depth + 1, visited)
        if output is not None:
            return [a] + output[0], output[1]

def inside_loop(loop_coords, pos, visited, depth):
    global r_low, r_high, c_low, c_high

    if pos in visited:
        return True

    visited.add(pos)

    r, c = pos
    if r < r_low or r > r_high or c < c_low or c > c_high:
        # Escaped
        return False

    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if abs(dr) == abs(dc):
                continue
            rr, cc = r + dr, c + dc

            if (rr, cc) in loop_coords:
                continue

            output = inside_loop(loop_coords, (rr, cc), visited, depth + 1)
            if not output:
                return output

    return True

def flood_fill(loop_coords, inside):
    global r_low, r_high, c_low, c_high

    start = (r_low - 10, c_low - 10)
    Q = deque([start])
    S = set()

    while Q:
        r, c = Q.popleft()

        if (r, c) in S:
            continue

        S.add((r, c))

        for dr in [-0.5, 0, 0.5]:
            for dc in [-0.5, 0, 0.5]:
                if abs(int(dr * 2)) == abs(int(dc * 2)):
                    continue

                rr, cc = r + dr, c + dc

                if rr < r_low - 10 or rr > r_high + 10 or cc < c_low - 10 or cc > c_high + 10:
                    continue

                if (rr, cc) in loop_coords:
                    continue

                Q.append((rr, cc))

    to_remove = S.intersection(set(inside))

    return to_remove, len(to_remove)

def refine_loop(loop):
    new_loop = []

    for i in range(len(loop) - 1):
        new_loop.append(loop[i])
        d = (loop[i + 1][0] - loop[i][0], loop[i + 1][1] - loop[i][1])
        new_loop.append((loop[i][0] + d[0] / 2, loop[i][1] + d[1] / 2))

    return set(new_loop)

with open(0) as f:
    grid = [x.strip() for x in f.readlines()]

R = len(grid)
C = len(grid[0])
start = (0, 0)

for r in range(R):
    for c in range(C):
        if grid[r][c] == 'S':
            start = (r, c)
            break
    if start != (0, 0):
        break

L, furthest_node = find_furthest_point(grid, start, start, 0, set())
L = [start] + L

print("Part 1:", furthest_node)

r_low = min(L, key=lambda k: k[0])[0]
r_high = max(L, key=lambda k: k[0])[0]
c_low = min(L, key=lambda k: k[1])[1]
c_high = max(L, key=lambda k: k[1])[1]

total = 0
inside = []

for r in range(r_low, r_high + 1):
    for c in range(c_low, c_high + 1):
        if (r, c) in L:
            continue

        if inside_loop(set(L), (r, c), set(), 0):
            total += 1
            inside.append((r, c))

loop = refine_loop(L)

coords, to_remove = flood_fill(loop, inside)

print("Part 2:", total - to_remove)










