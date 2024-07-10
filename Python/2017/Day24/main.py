from collections import defaultdict
from heapq import heappush, heappop

with open(0) as f:
    lines = [x.strip() for x in f.readlines()]

class Bridge:
    def __init__(self, s):
        s = list(map(int, s.split("/")))
        self.ports = [s[0], s[1]]

    def free_port(self, connected):
        if len(set(self.ports)) == 1:
            return self.ports[0]

        p1 = set(self.ports)
        p2 = set(connected.ports)

        i = p1 & p2
        return int(next(a for a in self.ports if a not in i))

    def can_connect(self, to_connect):
        p1 = set(self.ports)
        p2 = set(to_connect.ports)

        return len(p1 & p2) > 0

    def connects_with(self, port):
        return port in self.ports

    def __repr__(self):
        return f"Bridge<{sorted(self.ports)}>"

    def __str__(self):
        return f"Bridge<{sorted(self.ports)}>"

bridges = []

for line in lines:
    if "0" in line.split("/"):
        start = Bridge(line)
    else:
        bridges.append(Bridge(line))

paths = []

def dfs(curr, last, path, left):
    possible = [x for x in left if x.connects_with(curr.free_port(last))]

    if len(possible) == 0:
        paths.append(tuple(path + [curr]))
        return sum(curr.ports)

    best = 0

    for p in possible:
        best = max(best, dfs(p, curr, path + [curr], [x for x in left if x != p]))

    return best + sum(curr.ports)

print("Part 1:", dfs(start, Bridge("0/0"), [], bridges))

length = max([len(path) for path in paths])
paths = [x for x in paths if len(x) == length]
largest = 0

for path in paths:
    total = 0

    for b in path:
        total += sum(b.ports)

    largest = max(largest, total)

print("Part 2:", largest)

















