import re
from collections import deque

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

valves = {}
tunnels = {}

for line in lines:
    p = re.findall("[A-Z]{2}|(?<=\=)\d+", line)
    tunnels[p[0]] = p[2:]
    valves[p[0]] = int(p[1])

dists = {}
nonempty = []

for valve in valves:
    if valve != "AA" and not valves[valve]:
        continue

    if valve != "AA":
        nonempty.append(valve)

    dists[valve] = {valve: 0, "AA": 0}
    visited = {valve}

    Q = deque([(0, valve)])

    while Q:
        dist, pos = Q.popleft()

        for neighbour in tunnels[pos]:
            if neighbour in visited:
                continue
            visited.add(neighbour)
            if valves[neighbour]:
                dists[valve][neighbour] = dist + 1
            Q.append((dist + 1, neighbour))

    del dists[valve][valve]
    if valve != "AA":
        del dists[valve]["AA"]

indices = {}

for index, element in enumerate(nonempty):
    indices[element] = index

cache = {}

def dfs(time, valve, bitmask):
    if (time, valve, bitmask) in cache:
        return cache[(time, valve, bitmask)]

    maxval = 0

    for neighbour in dists[valve]:
        bit = 1 << indices[neighbour]
        if bitmask & bit:
            continue

        remtime = time - dists[valve][neighbour] - 1
        if remtime <= 0:
            continue

        maxval = max(maxval, dfs(remtime, neighbour, bitmask | bit) + valves[neighbour] * remtime)

    cache[(time, valve, bitmask)] = maxval

    return maxval

print(f'Part 1: {dfs(30, "AA", 0)}')

b = (1 << len(nonempty)) - 1
m = 0

for i in range((b + 1) // 2):
    m = max(m, dfs(26, "AA", i) + dfs(26, "AA", b ^ i))

print(f'Part 2: {m}')