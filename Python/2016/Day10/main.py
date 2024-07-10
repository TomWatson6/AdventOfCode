from collections import defaultdict
import re

with open(0) as f:
    lines = [x.strip() for x in f.readlines()]

bots = defaultdict(lambda: [])
values = defaultdict(lambda: [])

for line in lines:
    parts = re.findall(r"(\w+ \d+)", line)
    if len(parts) == 3:
        # bot [x] gives low to bot [y] and high to bot [z]
        bots[parts[0]] = [parts[1], parts[2]]
    elif len(parts) == 2:
        # value [x] goes to bot [y]
        values[parts[1]].append(int(parts[0].split()[1]))
    else:
        assert False, (line, parts)

while True:
    vals = [x for x in values.items() if len(x[1]) == 2]
    if len(vals) == 0:
        break

    for k, v in vals:
        if sorted(v) == [17, 61]:
            print("Part 1:", k.split()[1])

        dest = bots[k]

        if len(dest) <= 1:
            if len(dest) == 0:
                assert False, (k, v)
            continue

        low, high = dest

        values[low].append(min(v))
        values[high].append(max(v))
        values[k] = []

print("Part 2:", values['output 0'][0] * values['output 1'][0] * values['output 2'][0])



























