
with open(0) as f:
    grid = f.read().splitlines()

R = len(grid)
C = len(grid[0])

start = (0, grid[0].index("."))
end = (R - 1, grid[-1].index("."))

points = [start, end]

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == '#':
            continue

        adj = 0

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rr, cc = r + dr, c + dc

            if 0 <= rr < R and 0 <= cc < C and grid[rr][cc] != "#":
                adj += 1

        if adj >= 3:
            points.append((r, c))

dirs = {
    '^': [(-1, 0)],
    'v': [(1, 0)],
    '<': [(0, -1)],
    '>': [(0, 1)],
    '.': [(-1, 0), (1, 0), (0, -1), (0, 1)],
}

def init_graph(p2):
    graph = {pt: {} for pt in points}

    for sr, sc in points:
        stack = [(0, sr, sc)]
        seen = {(sr, sc)}

        while stack:
            n, r, c = stack.pop()

            if n != 0 and (r, c) in points:
                graph[(sr, sc)][(r, c)] = n
                continue

            di = [(-1, 0), (1, 0), (0, -1), (0, 1)] if p2 else dirs[grid[r][c]]

            # for dr, dc in dirs[grid[r][c]]:
            for dr, dc in di:
            # for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#' and (nr, nc) not in seen:
                    stack.append((n + 1, nr, nc))
                    seen.add((nr, nc))

    return graph

seen = set()

def dfs(pt):
    if pt == end:
        return 0

    m = -float("inf")

    seen.add(pt)

    for nx in graph[pt]:
        if nx not in seen:
            m = max(m, dfs(nx) + graph[pt][nx])

    seen.remove(pt)

    return m

graph = init_graph(False)
print("Part 1:", dfs(start))

graph = init_graph(True)
print("Part 2:", dfs(start))

















