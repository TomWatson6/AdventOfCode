import re

D = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0),
}

with open("input.txt") as f:
    moves = [[(x, int(y)) for x, y in re.findall(r"([UDRL])(\d+)", line)] for line in f.readlines()]

pos = [(0, 0), (0, 0)]
C = set()
I = set()

d = 0

for dir, dist in moves[0]:
    for _ in range(dist):
        pos[0] = (pos[0][0] + D[dir][0], pos[0][1] + D[dir][1])
        d += 1
        C.add((pos[0], d))

d = 0

seen = set([x[0] for x in C])

for dir, dist in moves[1]:
    for _ in range(dist):
        pos[1] = (pos[1][0] + D[dir][0], pos[1][1] + D[dir][1])
        d += 1
        if pos[1] in seen:
            I.add((pos[1], d))

S = []

for coord, steps in I:
    s = [x[1] for x in C if x[0] == coord][0]
    S.append(steps + s)

closest = min(I, key=lambda k: abs(k[0][0]) + abs(k[0][1]))
print("Part 1:", abs(closest[0][0]) + abs(closest[0][1]))
print("Part 2:", min(S))



















