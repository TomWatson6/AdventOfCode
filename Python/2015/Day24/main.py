
with open(0) as f:
    lines = list(map(int, [x.strip() for x in f.readlines()]))

def product(items):
    p = 1
    for i in items:
        p *= i
    return p

weight = sum(lines) // 3

def find_groups(lines, weight, group=[]):
    if weight == 0:
        yield group
    elif weight < 0 or not lines:
        return
    else:
        for i in range(len(lines)):
            yield from find_groups(lines[i+1:], weight - lines[i], group + [lines[i]])

def find_smallest_group(lines, weight):
    for group in find_groups(lines, weight):
        yield group

def find_smallest_group_with_smallest_quantum_entanglement(lines, weight):
    for group in find_groups(lines, weight):
        yield group

# Part 1

smallest_group = None
smallest_quantum_entanglement = None
for group in find_smallest_group(lines, weight):
    if smallest_group is None or len(group) < len(smallest_group):
        smallest_group = group
        smallest_quantum_entanglement = product(group)
    elif len(group) == len(smallest_group):
        smallest_quantum_entanglement = min(smallest_quantum_entanglement, product(group))

print("Part 1:", smallest_quantum_entanglement)

# Part 2

smallest_group = None
smallest_quantum_entanglement = None
weight = sum(lines) // 4

for group in find_smallest_group_with_smallest_quantum_entanglement(lines, weight):
    if smallest_group is None or len(group) < len(smallest_group):
        smallest_group = group
        smallest_quantum_entanglement = product(group)
    elif len(group) == len(smallest_group):
        smallest_quantum_entanglement = min(smallest_quantum_entanglement, product(group))

print("Part 2:", smallest_quantum_entanglement)


















