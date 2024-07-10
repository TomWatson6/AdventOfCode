from collections import defaultdict as dd

with open("input.txt") as f:
    input = f.read().split("\n\n")

replacements = tuple([[x[0], x[2]] for x in [y.split(" ") for y in input[0].split("\n")]])
molecule = input[1]
results = set()

for rep in replacements:
    for i in range(len(molecule) - (len(rep[0]) - 1)):
        if molecule[i:i + len(rep[0])] == rep[0]:
            res = molecule[:i] + rep[1] + molecule[i + len(rep[0]):]
            results.add(res)

print("Part 1: {}".format(len(results)))

steps = 0

while True:
    done = True

    for k, v in replacements:
        if v in molecule:
            molecule = molecule.replace(v, k, 1)
            steps += 1
            done = False
    if done:
        break

print("Part 2:", steps)



