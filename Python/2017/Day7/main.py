from collections import defaultdict

M = {}
W = {}

def weight(node):
    total = 0
    if node in M:
        for n in M[node]:
            total += weight(n)

    total += W[node]
    return total

def find(node, weights):
    WS = defaultdict(lambda: 0)
    for m in M[node]:
        WS[weight(m)] += 1

    lower = min(WS.items(), key=lambda t: t[1])[0]
    upper = max(WS.items(), key=lambda t: t[1])[0]
    ws = [lower, upper]

    if len(set([weight(x) for x in M[node]])) != 1:
        for n in M[node]:
            if weight(n) == lower:
                ans = find(n, ws)
                if ans is not None:
                    return ans
    else:
        if len(weights) > 1:
            correction = weights[1] - weights[0]
            return W[node] + correction

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

for line in lines:
    parts = line.split(" -> ")
    disc = parts[0].split(" ")[0]
    w = int(parts[0].split(" ")[1].strip("(").strip(")"))
    W[disc] = w

    if len(parts) > 1:
        M[parts[0].split(" ")[0]] = parts[1].split(", ")

# elem of M such that elem not in any other M val
bottom = [x[0] for x in M.items() if all([x[0] not in t[1] for t in M.items()])][0]

print("Part 1:", bottom)
print("Part 2:", find(bottom, []))









