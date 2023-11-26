from collections import defaultdict as dd

with open("input.txt") as f:
    input = f.read().split("\n\n")

replacements = tuple([[x[0], x[2]] for x in [y.split(" ") for y in input[0].split("\n")]])
molecule = input[1]
outcomes = set()
DP = {}

def crunch(curr, depth):
    if curr == "e":
        return depth



def find(curr, depth):
    # print(f"Depth: {depth} with {curr}")
    if curr in DP:
        return DP[curr]

    if curr == molecule:
        return depth
    if len(curr) > len(molecule):
        return
    for rep in replacements:
        for i in range(len(curr) - (len(rep[0]) - 1)):
            if curr[i:i + len(rep[0])] == rep[0]:
                res = curr[:i] + rep[1] + curr[i + len(rep[0]):]
                outcome = find(res, depth + 1)
                DP[res] = outcome
                if outcome is not None:
                    print(f"Length of outcomes: {len(outcomes)}")
                    outcomes.add(outcome)

results = set()

for rep in replacements:
    for i in range(len(molecule) - (len(rep[0]) - 1)):
        if molecule[i:i + len(rep[0])] == rep[0]:
            res = molecule[:i] + rep[1] + molecule[i + len(rep[0]):]
            results.add(res)

print("Part 1: {}".format(len(results)))

for rep in replacements:
    assert len(rep[1]) >= len(rep[0])

find("e", 0)

print(f"Part 2: {min(outcomes)} with possibilities being {outcomes}")



