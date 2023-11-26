from collections import deque

with open("input.txt") as f:
    grid = [list(x.strip()) for x in f.readlines()]

R = len(grid)
C = len(grid[0])

E = [[0 for _ in range(C)] for _ in range(R)]

for r in range(R):
    for c in range(C):
        if grid[r][c] == 'S':
            E[r][c] = 1
        elif grid[r][c] == 'E':
            E[r][c] = 26
        else:
            E[r][c] = ord(grid[r][c]) - ord('a') + 1

Q = deque()

for r in range(R):
    for c in range(C):
        if grid[r][c] == 'S':
            Q.append((r, c, 0))

S = set()

def bfs():
    while Q:
        r, c, d = Q.popleft()
        if (r, c) in S:
            continue
        S.add((r, c))
        if grid[r][c] == 'E':
            return d
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rr = r + dr
            cc = c + dc
            if 0 <= rr < R and 0 <= cc < C and E[rr][cc] <= E[r][c] + 1:
                Q.append((rr, cc, d + 1))

ans = bfs()
print("Part 1:", ans)

Q = deque()
S = set()

for r in range(R):
    for c in range(C):
        if E[r][c] == 1:
            Q.append((r, c, 0))

ans = bfs()
print("Part 2:", ans)












