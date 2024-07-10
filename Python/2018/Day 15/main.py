from collections import deque
from copy import deepcopy

with open(0) as f:
    G = [[c for c in r.strip()] for r in f.readlines()]

Copy = deepcopy(G)
assert len(G) > 0

DP = {}

finished = False
R = len(G)
C = len(G[0])
attack_power = 3
elf_power = 3
elves_dead = 0

HP = {}

for r in range(R):
    for c in range(C):
        if G[r][c] in ['G', 'E']:
            HP[(G[r][c], (r, c))] = 200

def move(start, dest):
    unit = G[start[0]][start[1]]
    HP[(unit, dest)] = HP[(unit, start)]
    del(HP[(unit, start)])
    G[dest[0]][dest[1]] = unit
    G[start[0]][start[1]] = '.'

def get_adjacents(pos):
    adj = []
    r, c = pos

    for rr, cc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        dr = r + rr
        dc = c + cc
        if 0 <= dr < R and 0 <= dc < C and G[dr][dc] == '.':
            adj.append((dr, dc))

    return adj

def dist(start, dest):
    return abs(start[0] - dest[0]) + abs(start[1] - dest[1])

def bfs(start, dest):
    Q = deque()
    Q.append((start, []))
    S = set()

    while Q:
        pos, path = Q.popleft()

        if pos in S:
            continue
        S.add(pos)

        if dist(pos, dest) == 0:
            return path

        adj = get_adjacents(pos)
        for a in adj:
            # if dist(a, dest) < dist(pos, dest):
            p = deepcopy(path)
            p.append(a)
            Q.append((a, p))

def get_enemies(ch):
    enemies = []
    e = 'G'
    if ch == 'G':
        e = 'E'

    for r in range(R):
        for c in range(C):
            if G[r][c] == e:
                enemies.append((r, c))

    return enemies

def attack(target):
    key = (G[target[0]][target[1]], target)
    if G[target[0]][target[1]] == 'E':
        HP[key] -= attack_power
    else:
        HP[key] -= elf_power
    if HP[key] <= 0:
        if G[target[0]][target[1]] == 'E':
            global elves_dead
            elves_dead += 1
        del(HP[key])
        G[target[0]][target[1]] = '.'

def path_len(start, dest):
    path = bfs(start, dest)
    if path is None:
        return 1e9
    return len(path)

def next_round():
    moved = set()
    for r in range(R):
        for c in range(C):
            if (r, c) in moved:
                continue
            rr, cc = r, c
            if G[r][c] not in ['G', 'E']:
                continue
            enemies = get_enemies(G[r][c])
            if len(enemies) == 0:
                global finished
                finished = True
                return

            if all([dist((r, c), e) > 1 for e in enemies]):
                adj = set()

                for e in enemies:
                    adj = adj.union(set(get_adjacents(e)))

                if len(adj) == 0:
                    continue

                adj = sorted(list(adj))
                # p = {}
                # for a in adj:
                #     if ((r, c), a) in DP:
                #         p[((r, c), a)] = DP[(r, c), a]
                #     else:
                #         l = path_len((r, c), a)
                #         p[((r, c), a)] = l
                #         DP[((r, c), a)] = l

                # selected = min(adj, key=lambda a: p[((r, c), a)])
                selected = min(adj, key=lambda a: (path_len((r, c), a), a))

                path = bfs((r, c), selected)
                if path == None:
                    continue

                move((r, c), path[0])
                moved.add(path[0])
                rr, cc = path[0]

            in_range = [e for e in enemies if dist((rr, cc), e) == 1]
            
            if len(in_range) > 0:
                target = min(in_range, key=lambda e: HP[(G[e[0]][e[1]], e)])
                targets = sorted([x for x in in_range if HP[(G[x[0]][x[1]], x)] == HP[(G[target[0]][target[1]], target)]])
                attack(targets[0])

def print_grid():
    global G

    for r in range(R):
        for c in range(C):
            print(G[r][c], end="")

        print()

    print()

rounds = 0

# print_grid()
# print(HP)

while not finished:
    next_round()
    rounds += 1

# print("After Round: " + str(rounds))
# print_grid()
# print(HP)

print(f"Part 1: {str((rounds - 1) * sum([v[1] for v in HP.items()]))}")

while elves_dead != 0:
    elves_dead = 0
    finished = False
    rounds = 0
    G = deepcopy(Copy)
    elf_power += 1

    HP = {}

    for r in range(R):
        for c in range(C):
            if G[r][c] in ['G', 'E']:
                HP[(G[r][c], (r, c))] = 200

    while not finished:
        next_round()
        rounds += 1
    print(f"Tested with elf power {elf_power} up to {rounds} rounds with {elves_dead} elves getting killed")

print(f"Part 2: {str(rounds - 1)} * {sum(v[1] for v in HP.items())} = {str((rounds - 1) * sum(v[1] for v in HP.items()))}")
    
























