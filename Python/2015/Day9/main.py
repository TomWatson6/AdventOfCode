from copy import deepcopy
import time

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

dist = {}

for line in lines:
    parts = line.split(" ")
    if not dist.get(parts[0]):
        dist[parts[0]] = {}
    if not dist.get(parts[2]):
        dist[parts[2]] = {}

    dist[parts[0]][parts[2]] = int(parts[4])
    dist[parts[2]][parts[0]] = int(parts[4])

def check(visited, current, func):
    visited.append(current)
    totals = []

    connections = dist[current]

    for k, v in connections.items():
        if k in visited:
            continue
        total = v + check(deepcopy(visited), k, func)
        totals.append(total)
    if len(totals) > 0:
        return func(totals)

    return 0

func = lambda x: min(x)
totals = []

start = time.time()

for k in dist.keys():
    totals.append(check([], k, func))

p1 = func(totals)
end = time.time()

print("Part 1: {} in {:.3f} seconds".format(p1, end - start))

start = time.time()

func = lambda x: max(x)
totals = []

for k in dist.keys():
    totals.append(check([], k, func))

end = time.time()
p2 = func(totals)

print("Part 2: {} in {:.3f} seconds".format(p2, end - start))
