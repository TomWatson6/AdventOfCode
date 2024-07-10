from collections import deque, defaultdict
from copy import deepcopy
import sys
import heapq

sys.setrecursionlimit(int(1e9))


with open(0) as f:
    lines = [x.strip() for x in f.readlines()]

grid = [list(map(int, c)) for c in lines]

R = len(grid)
C = len(grid[0])

start = (0, 0)
dest = (len(grid) - 1, len(grid[0]) - 1)

def dijkstra(grid, start, dest):
    r, c = start
    # cost, row, col, dir, line_length
    Q = [(0, r, c, -1, 0)]
    S = {}

    while Q:
        cost, r, c, d, l = heapq.heappop(Q)

        if (r, c, d, l) in S:
            continue

        S[(r, c, d, l)] = cost

        for nd, (dr, dc) in enumerate([[0, 1], [1, 0], [0, -1], [-1, 0]]):
            rr = r + dr
            cc = c + dc
            new_l = (1 if nd != d else l + 1)

            if 0 <= rr < R and 0 <= cc < C and new_l <= 3 and ((nd + 2) % 4 != d):
                heapq.heappush(Q, (cost + grid[rr][cc], rr, cc, nd, new_l))

    ans = min(v for (r, c, d, l), v in S.items() if (r, c) == dest)

    return ans

def dijkstra2(grid, start, dest):
    r, c = start
    # cost, row, col, dir, line_length
    Q = [(0, r, c, -1, -1)]
    S = {}

    while Q:
        cost, r, c, d, l = heapq.heappop(Q)

        if (r, c, d, l) in S:
            continue

        S[(r, c, d, l)] = cost

        for nd, (dr, dc) in enumerate([[0, 1], [1, 0], [0, -1], [-1, 0]]):
            rr = r + dr
            cc = c + dc
            new_l = (1 if nd != d else l + 1)

            if 0 <= rr < R and 0 <= cc < C and new_l <= 10 and ((nd + 2) % 4 != d) and (nd == d or l >= 4 or l == -1):
                heapq.heappush(Q, (cost + grid[rr][cc], rr, cc, nd, new_l))

    ans = min(v for (r, c, d, l), v in S.items() if (r, c) == dest and 4 <= l <= 10)

    return ans

print("Part 1:", dijkstra(grid, start, dest))
print("Part 2:", dijkstra2(grid, start, dest))























