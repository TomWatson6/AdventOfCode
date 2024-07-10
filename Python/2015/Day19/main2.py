from collections import defaultdict, deque

with open(0) as f:
    chunks = f.read().split('\n\n')

M = defaultdict(list)
M_ = {}

for line in chunks[0].split('\n'):
    k, v = line.split(' => ')
    M[k].append(v)
    M_[v] = k

polymer = chunks[1].strip()

# Part 1

molecules = set()

for k, v in M.items():
    for i in range(len(polymer)):
        if polymer[i:i+len(k)] == k:
            for r in v:
                molecules.add(polymer[:i] + r + polymer[i+len(k):])

print(len(molecules))

# Part 2

def crunch(molecule):
    steps = 0

    while True:
        done = True
        for k, v in M_.items():
            if k in molecule:
                molecule = molecule.replace(k, v, 1)
                steps += 1
                done = False
        if done:
            break

    assert molecule == 'e'

    return steps

print(crunch(polymer))























