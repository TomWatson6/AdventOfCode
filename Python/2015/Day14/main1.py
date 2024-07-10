import re
from collections import defaultdict

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

TIME = 2503

D = []
P = {}
T = defaultdict(list)

for line in lines:
    name, speed, duration, rest = [line.split(" ")[0]] + [int(x) for x in re.findall(r"\d+", line)]
    D.append((name, speed, duration, rest))

for name, speed, duration, rest in D:
    while len(T[name]) < TIME:
        for _ in range(duration):
            if len(T[name]) == 0:
                T[name].append(speed)
                continue
            T[name].append(T[name][-1] + speed)

        for _ in range(rest):
            T[name].append(T[name][-1])

winner = max([t[TIME - 1] for t in T.values()])
print("Part 1:", winner)

S = defaultdict(int)

for t in range(0, TIME):
    winning = max([x[t] for x in T.values()])
    winners = [k[0] for k in T.items() if k[1][t] == winning]
    for w in winners:
        S[w] += 1

winner = max([s for s in S.values()])
print("Part 2:", winner)





















