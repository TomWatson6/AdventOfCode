from collections import defaultdict

with open("input.txt") as f:
    connections = [[t.split(", ") for t in x.strip().split(" <-> ")] for x in f.readlines()]

M = defaultdict(lambda: set())
N = set()

for conn in connections:
    for a in conn[0]:
        for b in conn[1]:
            M[a].add(b)
            M[b].add(a)

def find(node, visited):
    global M, N
    total = 0
    for n in M[node]:
        if n not in visited:
            visited.add(n)
            N.add(n)
            total += find(n, visited)

    return total + 1

print("Part 1:", find('0', set()) - 1)

groups = set()

for node in M.keys():
    N = set()
    find(node, set())
    groups.add(tuple(sorted(N)))

print("Part 2:", len(groups))

    



















