from collections import defaultdict


with open("input.txt") as f:
    coords = [t.strip().split(", ") for t in f.readlines()]
    coords = [(int(r), int(c)) for r, c in coords]

r_low = min(coords, key = lambda k: k[0])[0] - 100
r_high = max(coords, key = lambda k: k[0])[0] + 100
c_low = min(coords, key = lambda k: k[1])[1] - 100
c_high = max(coords, key = lambda k: k[1])[1] + 100

G = {}
p2 = []

for r in range(r_low, r_high + 1):
    for c in range(c_low, c_high + 1):
        total_dist = 0
        dist = defaultdict(lambda: [])
        for co in coords:
            # if (r, c) == co:
            #     continue
            d = abs(r - co[0]) + abs(c - co[1])
            total_dist += d
            dist[d].append(co)

        if total_dist < 10000:
            p2.append(total_dist)

        smallest = min(dist.items(), key = lambda k: k[0])
        if len(smallest[1]) == 1:
            G[(r, c)] = smallest[1][0]

wall_coords = []
wall_coords.extend([(r_low, c) for c in range(c_low, c_high + 1)])
wall_coords.extend([(r_high, c) for c in range(c_low, c_high + 1)])
wall_coords.extend([(r, c_low) for r in range(r_low, r_high + 1)])
wall_coords.extend([(r, c_high) for r in range(r_low, r_high + 1)])
wall_coords = set(wall_coords)

exc = set()

for wc in wall_coords:
    if wc in G:
        exc.add(G[wc])

S = defaultdict(lambda: 0)

for v in G.values():
    S[v] += 1

largest = max([(k, v) for k, v in S.items() if k not in exc], key = lambda k: k[1])[0]
ans = S[largest]

print("Part 1:", ans)
print("Part 2:", len(p2))













