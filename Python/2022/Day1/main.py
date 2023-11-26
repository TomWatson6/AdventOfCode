

with open("input.txt") as f:
    input = f.read()
    print("Part 1:", max([sum([int(y) for y in x.split("\n")]) for x in input.strip().split("\n\n")]))
    print("Part 2:", sum(sorted([sum([int(y) for y in x.split("\n")]) for x in input.strip().split("\n\n")])[-3:]))

