from collections import defaultdict, deque

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

def orbits(a, b):
    global orbitting

    while a in orbitting:
        a = orbitting[a]
        if a == b:
            return True
        
    return False

def adjacents(a):
    global orbit, orbitting

    adj = []

    if a in orbit:
        for b in orbit[a]:
            adj.append(b)

    if a in orbitting:
            adj.append(orbitting[a])

    return adj

def bfs(a, b):
    adj = adjacents(a)
    Q = deque(zip(adj, [1 for _ in range(len(adj))]))
    S = set()

    while Q:
        node, d = Q.popleft()

        if node in S:
            continue
        S.add(node)

        if node == b:
            return d - 2

        adj = adjacents(node)

        for a in adj:
            Q.append((a, d + 1))

    return -1

orbit = defaultdict(list)
orbitting = {}
planets = set()

for x in lines:
    parts = x.split(")")
    orbit[parts[0]].append(parts[1])
    planets.add(parts[0])
    planets.add(parts[1])

for k, v in orbit.items():
    for o in v:
        orbitting[o] = k

total = 0

for p in planets:
    for q in planets:
        if p == q:
            continue
        if orbits(p, q):
            total += 1

print("Part 1:", total)
print("Part 2:", bfs("YOU", "SAN"))


    





















