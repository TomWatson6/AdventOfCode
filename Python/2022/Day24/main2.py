from collections import deque

with open("input.txt") as f:
    input = [list(x.strip()) for x in f.readlines()]

D = {
    (-1, 0): 'v',
    (1, 0): '^',
    (0, -1): '>',
    (0, 1): '<',
}

start = (-1, 0)
grid = []

for r, row in enumerate(input):
    if r == 0 or r == len(input) - 1:
        continue
    R = []
    for c, val in enumerate(row):
        if c == 0 or c == len(row) - 1:
            continue
        R.append(val)
    grid.append(R)

end = (len(grid), len(grid[0]) - 1)

def is_safe(grid, r, c, t):
    for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        rr = (r + (dir[0] * t)) % len(grid)
        cc = (c + (dir[1] * t)) % len(grid[0])

        if r + dir[0] < 0 or r + dir[0] > len(grid) - 1:
            continue

        if grid[rr][cc] == D[dir]:
            return False

    return True

def reconstruct_path(r, c, t, CF):
    path = [(r, c)]

    while (r, c) != start:
        r, c, t = CF[(r, c, t)]
        path.append((r, c))

    return path[::-1]

def get_possible_moves(grid, r, c, start, final):
    M = [(0, 0)]

    for pos in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        p = (pos[0] + r, pos[1] + c)
        is_possible = 0 <= p[0] < len(grid) and 0 <= p[1] < len(grid[0])
        if is_possible or p == start or p == final:
            M.append(pos)

    return M

def search(start, end, start_time):
    moves = 0
    Q = deque()
    Q.append((start, start_time))
    S = set()
    CF = {}

    while Q:
        (r, c), t = Q.popleft()

        if (r, c, t) in S:
            continue

        S.add((r, c, t))

        if t + 1 > moves:
            moves = t + 1

        if (r, c) == end:
            return t - start_time

        for dr, dc in get_possible_moves(grid, r, c, start, end):
            rr = r + dr
            cc = c + dc

            if is_safe(grid, rr, cc, t + 1):
                Q.append(((rr, cc), t + 1))
                CF[(rr, cc, t + 1)] = (r, c, t)

total = 0
m = search(start, end, total)
print(m)
total += m
m = search(end, start, total)
print(m)
total += m
m = search(start, end, total)
print(m)
total += m
print("Part 2:", total)

