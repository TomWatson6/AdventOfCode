from collections import deque

with open(0) as f:
    grid = [list(x.strip("\n")) for x in f.readlines()]

R = len(grid)
C = len(grid[0])

D = {
    (1, 0): "|+ ",
    (0, -1): "-+ ",
    (-1, 0): "|+ ",
    (0, 1): "-+ ",
}

d = 0

start = (0, grid[0].index('|'))

def bfs(start):
    r, c = start
    Q = deque([((r + 1, c), [start])])
    S = set()

    while Q:
        (r, c), path = Q.popleft()

        if grid[r][c] == '+':
            adj = [(rr, cc) for rr, cc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)] if (rr, cc) not in S]
            adj = [(rr, cc) for rr, cc in adj if 0 <= rr < R and 0 <= cc < C]
            adj = [(rr, cc) for rr, cc in adj if grid[rr][cc] != " "]
        else:
            lr, lc = path[-1]
            dr, dc = r - lr, c - lc
            rr, cc = r + dr, c + dc
            adj = [(rr, cc)]

        adj = [(r, c) for r, c in adj if 0 <= r < R and 0 <= c < C]

        for rr, cc in adj:
            S.add((r, c))
            Q.append(((rr, cc), path + [(r, c)]))

    letters = "".join([grid[r][c] for r, c in path if grid[r][c] not in "+-| "])
    last = [i for i, (r, c) in enumerate(path) if grid[r][c] == letters[-1]]

    return letters, last[0] + 1

letters, dist = bfs(start)

print("Part 1:", letters)
print("Part 2:", dist)























