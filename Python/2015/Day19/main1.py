from collections import deque
import os

with open("simple_input.txt") as f:
    input = f.read().split("{}{}".format(os.linesep, os.linesep))

replacements = [[x[0], x[2]] for x in [y.split(" ") for y in input[0].split(os.linesep)]]
molecule = input[1].strip()
target = "e"

replacements = [[x[1], x[0]] for x in replacements]
s = "".join([" " for _ in range(1000)])
count = 0

def crunch(molecule, target, depth):
    global s, count
    print("Crunching: {}".format(molecule))
    # if len(molecule) < len(s):
    #     s = molecule
    #     print(s)
    
    if molecule == target:
        print("reached target")
        return depth
    # print(molecule)
    # if depth > 80:
    #     print("len molecule: {}, {} depth with {}".format(len(molecule), depth, molecule))
    smallest = 1e9
    for before, after in replacements:
        if depth == 0:
            count += 1
            print("Count: {} -> Replacing: {} with {}".format(count, before, after))
        for i in range(len(molecule) - len(before) + 1):
            # print(molecule[i:i + len(before)], before)
            if molecule[i:i + len(before)] == before:
                if depth == 0:
                    print("Found one!")
                last = molecule[i + len(before) + 1:] if i + len(before) + 1 < len(molecule) else ""
                new = molecule[:i] + after + last
                smallest = min(smallest, crunch(new[:], target, depth + 1))

    # print(smallest)
    return smallest

print(crunch(molecule, "e", 0))










