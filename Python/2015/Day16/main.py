from collections import defaultdict as dd

with open("correct.txt") as f:
    correct = {x[0].strip(":"): int(x[1]) for x in [x.strip().split(" ") for x in f.readlines()]}

with open("input.txt") as f:
    split_lines = [x.strip().split() for x in f.readlines()]
    assert len({len(x): True for x in split_lines}) == 1 # assert all have same amount of facts
    facts = {}
    for l in split_lines:
        facts[int(l[1].strip(":"))] = {}
        facts[int(l[1].strip(":"))][l[2].strip(":")] = int(l[3].strip(","))
        facts[int(l[1].strip(":"))][l[4].strip(":")] = int(l[5].strip(","))
        facts[int(l[1].strip(":"))][l[6].strip(":")] = int(l[7].strip(","))

valid_aunts = []

for k, v in facts.items():
    valid = True
    for k1, v1 in v.items():
        v2 = correct[k1]
        if v1 != v2:
            valid = False
            break
    if valid:
        valid_aunts.append(k)

print("Part 1: {}".format(valid_aunts[0]))

valid_aunts = []

for k, v in facts.items():
    valid = True
    for k1, v1 in v.items():
        v2 = correct[k1]
        if k1 in ["cats", "trees"]:
            if v2 >= v1:
                valid = False
                break
        elif k1 in ["pomeranians", "goldfish"]:
            if v2 <= v1:
                valid = False
                break
        else:
            if v1 != v2:
                valid = False
                break
    if valid:
        valid_aunts.append(k)

print("Part 2: {}".format(valid_aunts[0]))
