
from collections import defaultdict

def p1(output):
    print("Part 1:", output)

def p2(output):
    print("Part 2:", output)

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

polymer = lines[0]
first_letter = polymer[0]
last_letter = polymer[-1]

lines = [x.split(" -> ") for x in lines[2:]]

rules = dict()

for line in lines:
    rules[line[0]] = line[1]

p1_pairs = defaultdict(int)
p2_pairs = defaultdict(int)

for x in range(len(polymer) - 1):
    pair = polymer[x:x + 2]
    p1_pairs[pair] += 1 
    p2_pairs[pair] += 1

def evolve(pairs, rules):
    new_pairs = defaultdict(int)

    for k, v in pairs.items():
        if v == 0:
            continue
        insertion = rules[k]
        new_pairs[k[0] + insertion] += v
        new_pairs[insertion + k[1]] += v 
        
    return new_pairs

def count_letters(pairs):
    totals = defaultdict(int)

    for k, v in pairs.items():
        for letter in k:
            totals[letter] += v

    for k, v in totals.items():
        if k in [first_letter, last_letter]:
            totals[k] += 1

    return totals

steps = 40

for step in range(steps):
    if step < 10:
        p1_pairs = evolve(p1_pairs, rules)
    
    p2_pairs = evolve(p2_pairs, rules)

totals1 = count_letters(p1_pairs)

totals1 = [x for x in totals1.values()]
totals1.sort()

p1((totals1[-1] - totals1[0]) // 2)

totals2 = count_letters(p2_pairs)

totals2 = [x for x in totals2.values()]
totals2.sort()

p2((totals2[-1] - totals2[0]) // 2)


