from knot_hash import *
from collections import deque

with open("input.txt") as f:
    input = f.read().strip()

count = 0
image = []

for i in range(128):
    hashable = input + "-" + str(i)
    hashed = knot_hash(hashable)
    b = ""

    for h in hashed:
        b += bin(int(h, 16))[2:].zfill(4)

    count += len([x for x in b if x == '1'])
    image.append(b)

print("Part 1:", count)

M = set()
DP = set()

def get_adjacents(image, coord):
    adjacents = []

    for r in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            if abs(r) == abs(c):
                continue
            rr = int(coord[0]) + r
            cc = int(coord[1]) + c

            if 0 <= rr < len(image) and 0 <= cc < len(image[0]) and image[rr][cc] == '1':
                adjacents.append((rr, cc))

    return adjacents

def get_region(image, coord):
    global DP

    if coord in DP:
        return

    region = set()
    region.add(coord)

    Q = deque(get_adjacents(image, coord))

    while Q:
        c = Q.popleft()
        DP.add(c)

        if c in region:
            continue
        region.add(c)

        adj = [x for x in get_adjacents(image, c) if x not in DP]

        for a in adj:
            Q.append(a)

    return tuple(sorted(region))

for r in range(len(image)):
    for c in range(len(image[0])):
        if image[r][c] == '0':
            continue
        region = get_region(image, (r, c))

        if region is not None:
            M.add(region)

print("Part 2:", len(M))



















