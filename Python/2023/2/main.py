from collections import defaultdict

with open(0) as f:
    lines = [x.strip() for x in f.readlines()]

req = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

G = []

for line in lines:
    parts = [x.split(", ") for x in line.split(": ")[1].split("; ")]
    d = defaultdict(int)
    for p in parts:
        for c in p:
            cubes = c.split(" ")
            d[cubes[1]] = max(int(cubes[0]), d[cubes[1]])

    G.append(d)

total = 0

for i, g in enumerate(G):
    works = True

    for k, v in g.items():
        if v > req[k]:
            works = False
            break

    if works:
        total += i + 1

print("Part 1:", total)

power = 0

for g in G:
    product = 1
    for v in g.values():
        product *= v
    power += product

print("Part 2:", power)



















