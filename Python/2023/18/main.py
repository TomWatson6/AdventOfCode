from collections import deque, defaultdict
import sys
sys.setrecursionlimit(int(100000))

with open(0) as f:
    lines = [x.strip() for x in f.readlines()]

G = set()
pos = (0, 0)
pos2 = (0, 0)
G2 = [pos2]
G.add(pos)

DI = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0),
}

D = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0),
}

boundary = 0

for line in lines:
    d, mag, colour = line.split()

    # Part 2
    colour = colour[2:-1]
    m, di = colour[:-1], colour[-1]
    m, di = int(m, 16), int(di, 16)
    di = DI[di]

    boundary += abs(m * di[0]) + abs(m * di[1])
    pos2 = (pos2[0] + m * di[0], pos2[1] + m * di[1])
    G2.append(pos2)

    # Part 1
    mag = int(mag)
    d = D[d]

    for m in range(mag):
        pos = (pos[0] + d[0], pos[1] + d[1])
        G.add(pos)

r_low = min(G, key = lambda k: k[0])[0] - 1
r_high = max(G, key = lambda k: k[0])[0] + 2
c_low = min(G, key = lambda k: k[1])[1] - 1
c_high = max(G, key = lambda k: k[1])[1] + 2

def bfs(start):
    r, c = start
    if start in G:
        return 0

    Q = deque([(start)])
    S = set()

    while Q:
        pos = Q.popleft()
        r, c = pos

        if r < r_low or r >= r_high or c < c_low or c >= c_high:
            return 0

        if pos in S:
            continue

        S.add(pos)

        for dr, dc in D.values():
            rr = r + dr
            cc = c + dc

            if r_low <= rr < r_high and c_low <= cc < c_high and (rr, cc) not in G:
                Q.append((rr, cc))

    return len(S)

total = 0
totals = set()
found = False
pos = (0, 0)

for dr in [-1, 0, 1]:
    for dc in [-1, 0, 1]:
        if dr == dc == 0 or (dr, dc) in G:
            continue

        totals.add(bfs((dr, dc)))

totals = sorted(totals)
print("Part 1:", totals[0] + len(G))

A = abs(sum(G2[i][0] * (G2[i - 1][1] - G2[(i + 1) % len(G2)][1]) for i in range(len(G2)))) // 2
i = A - boundary // 2 + 1

print("Part 2:", i + boundary)




















# print(G2)
# rows = sorted(list([r for r, c in G2]))
# cols = sorted(list([c for r, c in G2]))

# print(max(rows) - min(rows))
# print(max(cols) - min(cols))

# print(rows, cols)
# # assert len(rows) * 2 == len([r for r, c in G2]), (len(rows), [r for r, c in G2])
# # assert len(cols) * 2 == len([c for r, c in G2]), (len(cols), [c for r, c in G2])


# area = 0
# edges = []
# vertices = []

# # if all corners in grid, then we can include as potentially fillable
# # the check to exclude outliers is by checking if any of it's edges only appears once in edges array, meaning outer edge

# for r in range(1, len(rows) - 1, 2):
#     print("rows:", r)
#     for c in range(1, len(cols) - 1, 2):
#         print("cols:", c, rows[r], rows[r + 1], cols[c], cols[c + 1])
#         if (rows[r], cols[c]) in G2 and (rows[r + 1], cols[c]) in G2 and (rows[r], cols[c + 1]) in G2 and (rows[r + 1], cols[c + 1]) in G2:
#             print("Doing anything")
#             # included
#             if rows[r] == rows[r + 1] or cols[c] == cols[c + 1]:
#                 continue

#             edges += [
#                 tuple(sorted([(rows[r], cols[c]), (rows[r + 1], cols[c])])),
#                 tuple(sorted([(rows[r + 1], cols[c]), (rows[r], cols[c + 1])])),
#                 tuple(sorted([(rows[r], cols[c + 1]), (rows[r + 1], cols[c + 1])])),
#                 tuple(sorted([(rows[r + 1], cols[c + 1]), (rows[r], cols[c])])),
#             ]

#             vertices += [(rows[r], cols[c]), (rows[r + 1], cols[c]), (rows[r], cols[c + 1]), (rows[r + 1], cols[c + 1])]

#             area += (rows[r + 1] + 1) - rows[r] * (cols[c + 1] + 1) - cols[c]

# edge_map = defaultdict(int)

# for e in edges:
#     edge_map[e] += 1

# vertices_map = defaultdict(int)

# for v in vertices:
#     vertices_map[v] += 1

# for k, v in edge_map.items():
#     if v == 2:
#         # + 1 for stripping off the extra vertex
#         area -= abs(k[0][0] - k[1][0]) + abs(k[0][1] - k[1][1]) + 1

# for k, v in vertices_map.items():
#     area -= v - 1

# print(area)
# print(gcd_list(rows))
# print(gcd_list(cols))

# ir = []

# for i in range(len(rows) - 1):
#     ir.append(rows[i + 1] - rows[i])

# print(ir)






















