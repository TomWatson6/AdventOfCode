from collections import deque

with open(0) as f:
    n = int(f.read().strip())

# x*x + 3*x + 2*x*y + y + y*y + number
dest = (31, 39)

def is_open(x, y, n):
    if x < 0 or y < 0:
        return False

    decimal = x*x + 3*x + 2*x*y + y + y*y + n
    binary = bin(decimal)[2:]
    return len([x for x in binary if x == '1']) % 2 == 0

def get_adjacents(x, y, n):
    coords = []

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if abs(dx) == abs(dy):
                continue
            if is_open(x + dx, y + dy, n):
                coords.append((x + dx, y + dy))

    return coords

def bfs(n, dest):
    Q = deque([((1, 1), 0)])
    S = set()

    while Q:
        (x, y), d = Q.popleft()

        if (x, y) in S:
            continue

        S.add((x, y))

        if x == dest[0] and y == dest[1]:
            return d

        adj = get_adjacents(x, y, n)

        for new_x, new_y in adj:
            Q.append(((new_x, new_y), d + 1))

def bfs2(n, max_depth):
    Q = deque([((1, 1), 0)])
    S = set()

    while Q:
        (x, y), d = Q.popleft()

        if (x, y) in S:
            continue

        if d > max_depth:
            return len(S)

        S.add((x, y))

        adj = get_adjacents(x, y, n)

        for new_x, new_y in adj:
            Q.append(((new_x, new_y), d + 1))


print("Part 1:", bfs(n, dest))
print("Part 2:", bfs2(n, 50))
















