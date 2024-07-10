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

def fill(sr, sc, s):
    Q = deque([(sr, sc, s)])
    S = set()
    ans = set()

    while Q:
        r, c, s = Q.popleft()

        if s % 2 == 0:
            ans.add((r, c))

        if s == 0:
            continue

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            rr = r + dr
            cc = c + dc

            if rr < 0 or rr >= R or cc < 0 or cc >= C or grid[rr][cc] == '#' or (rr, cc) in S:
                continue

            S.add((rr, cc))

            Q.append((rr, cc, s - 1))

    return len(ans)

print("Part 1:", fill(S[0], S[1], 64))

steps = 26501365
assert R == C
sr, sc = S

size = R

grid_width = steps // size - 1

odd = (grid_width // 2 * 2 + 1) ** 2
even = ((grid_width + 1) // 2 * 2) ** 2

odd_points = fill(sr, sc, size * 2 + 1)
even_points = fill(sr, sc, size * 2)

corner_t = fill(size - 1, sc, size - 1)
corner_r = fill(sr, 0, size - 1)
corner_b = fill(0, sc, size - 1)
corner_l = fill(sr, size - 1, size - 1)

small_tr = fill(size - 1, 0, size // 2 - 1)
small_tl = fill(size - 1, size - 1, size // 2 - 1)
small_br = fill(0, 0, size // 2 - 1)
small_bl = fill(0, size - 1, size // 2 - 1)

large_tr = fill(size - 1, 0, size * 3 // 2 - 1)
large_tl = fill(size - 1, size - 1, size * 3 // 2 - 1)
large_br = fill(0, 0, size * 3 // 2 - 1)
large_bl = fill(0, size - 1, size * 3 // 2 - 1)

total = 0
total += odd * odd_points
total += even * even_points
total += corner_t + corner_r + corner_b + corner_l
total += (grid_width + 1) * (small_tr + small_tl + small_br + small_bl)
total += grid_width * (large_tr + large_tl + large_br + large_bl)

print("Part 2:", total)












