import re
from collections import defaultdict

def value(c):
    return ord(c) - ord('A') + 1

with open("input.txt") as f:
    reqs = [(x[0][1], x[0][0]) for x in [re.findall(" ([A-Z]).*([A-Z]) ", l.strip()) for l in f.readlines()]]

R = defaultdict(lambda: [])
nodes = set()

for r in reqs:
    nodes.add(r[0])
    nodes.add(r[1])
    R[r[0]].append(r[1])

todo = []

for n in list(nodes):
    if n in R:
        continue
    todo.append(n)

seq = []

while len(todo) > 0:
    todo = sorted(todo, reverse = True)
    curr = todo.pop()
    seq.append(curr)
    to_remove = []
    for k, v in R.items():
        if curr in v:
            R[k] = [x for x in v if x != curr]
            if len(R[k]) == 0:
                to_remove.append(k)
    for r in to_remove:
        del R[r]
    todo = []
    for n in list(nodes):
        if n in R or n in seq:
            continue
        todo.append(n)

print("Part 1:", "".join(seq))

with open("input.txt") as f:
    reqs = [(x[0][1], x[0][0]) for x in [re.findall(" ([A-Z]).*([A-Z]) ", l.strip()) for l in f.readlines()]]

R = defaultdict(lambda: [])
nodes = set()

for r in reqs:
    nodes.add(r[0])
    nodes.add(r[1])
    R[r[0]].append(r[1])

todo = []

for n in list(nodes):
    if n in R:
        continue
    todo.append(n)

time_offset = 60
T = {n: value(n) + time_offset for n in nodes}

seq = []
time = 0
elves = 5
tasks = []

while len(todo) > 0 or len(tasks) > 0:
    to_remove = []
    for k, v in R.items():
        for t in tasks:
            if t[1] == 0 and t[0] in v:
                R[k] = [x for x in v if x != t[0]]
                if len(R[k]) == 0:
                    to_remove.append(k)

    for r in to_remove:
        assert r in R, r
        del R[r]

    new_tasks = []

    for t in tasks:
        if t[1] != 0:
            new_tasks.append(t)
        else:
            elves += 1
            seq.append(t[0])

    tasks = new_tasks

    todo = []
    for n in list(nodes):
        if n in R or n in seq or n in [x[0] for x in tasks]:
            continue
        todo.append(n)

    todo = sorted(todo, reverse = True)

    while elves > 0 and len(todo) > 0:
        elves -= 1
        work = todo.pop()
        tasks.append((work, T[work]))
    
    for i in range(len(tasks)):
        tasks[i] = (tasks[i][0], tasks[i][1] - 1)

    time += 1

print("Part 2:", time - 1)
    


    # find ends to the tree that aren't yet in done, order the list, and pop the next one off until all in done

















