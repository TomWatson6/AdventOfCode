from copy import deepcopy
import functools
import sys

sys.setrecursionlimit(int(1e9))
DP = {}

def dfs(mask, crit, index, crit_index, count):
    key = (index, crit_index, count)

    if key in DP:
        return DP[key]

    if index == len(mask):
        if crit_index == len(crit) and count == 0:
            return 1
        elif crit_index == len(crit) - 1 and crit[crit_index] == count:
            return 1
        else:
            return 0

    output = 0

    for c in ['.', '#']:
        if mask[index] == c or mask[index] == '?':
            if c == '.' and count == 0:
                output += dfs(mask, crit, index + 1, crit_index, 0)
            elif c == '.' and count > 0 and crit_index < len(crit) and crit[crit_index] == count:
                output += dfs(mask, crit, index + 1, crit_index + 1, 0)
            elif c == '#':
                output += dfs(mask, crit, index + 1, crit_index, count + 1)

    DP[key] = output

    return output

with open(0) as f:
    lines = [x.strip() for x in f.readlines()]

total = 0
total2 = 0

for i, line in enumerate(lines):
    mask, crit = line.split()
    crit = [int(x) for x in crit.split(",")]

    total += dfs(mask, crit, 0, 0, 0)
    DP.clear()

    mask = "?".join([mask for _ in range(5)])
    crit *= 5

    total2 += dfs(mask, crit, 0, 0, 0)
    DP.clear()

print("Part 1:", total)
print("Part 2:", total2)

















