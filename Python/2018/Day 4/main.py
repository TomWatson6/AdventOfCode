import re
from collections import defaultdict

with open("input.txt") as f:
    lines = [re.findall("(\d+)\-(\d+)\-(\d+) (\d+):(\d+)\] (.*)", x.strip())[0] for x in f.readlines()]
    lines = [(tuple(map(int, x[:5])), x[5]) for x in lines]
    lines = sorted(lines, key=lambda k: (k[0][0], k[0][1], k[0][2], k[0][3], k[0][4]))

G = defaultdict(lambda: defaultdict(lambda: 0))
T = defaultdict(lambda: 0)
index = 0
gid = 0

while index < len(lines):
    curr = lines[index]

    if len(curr[1].split(" ")) == 4:
        gid = int(curr[1].split(" ")[1][1:])
        index += 1
        continue

    if curr[1] == "falls asleep":
        wake = lines[index + 1]
        for i in range(curr[0][4], wake[0][4]):
            G[gid][i] += 1
            T[gid] += 1
        index += 2
        continue

    assert False, curr

O = {}

for k, v in G.items():
    count = T[k]
    common = max(v.items(), key=lambda r: r[1])[0]
    O[k] = (common, count)

O1 = {}

for k, v in G.items():
    minute = max(v.items(), key=lambda r: r[1])[1]
    common = max(v.items(), key=lambda r: r[1])[0]
    O1[k] = (common, minute)

output = max(O.items(), key=lambda k: k[1][1])
gid = output[0]
common = output[1][0]

print("Part 1:", gid * common)

output = max(O1.items(), key=lambda k: k[1][1])
gid = output[0]
common = output[1][0]

print("Part 2:", gid * common)

















