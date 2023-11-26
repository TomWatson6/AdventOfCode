from collections import defaultdict

with open("input.txt") as f:
    input = [[y for y in x.strip()] for x in f.readlines() if x != ""]

freq = {}

for line in input:
    for i, c in enumerate(line):
        if freq.get(i) == None:
            freq[i] = defaultdict(lambda: 0)

        freq[i][c] += 1

output = ""

for v in freq.values():
    s = sorted(v.items(), key=lambda kv: kv[1], reverse=True)

    output += s[0][0]

print("Part 1: {}".format(output))

output = ""

for v in freq.values():
    s = sorted(v.items(), key=lambda kv: kv[1])

    output += s[0][0]

print("Part 2: {}".format(output))