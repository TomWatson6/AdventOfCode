

with open("input.txt") as f:
    input = [[int(y) for y in x.strip().split(" ") if y != ""] for x in f.readlines()]

possible = 0

for tri in input:
    tri = sorted(tri)
    if tri[0] + tri[1] > tri[2]:
        possible += 1

print("Part 1: {}".format(possible))

possible = 0

for i in range(0, len(input), 3):
    for j in range(len(input[i])):
        tri = [input[i][j], input[i + 1][j], input[i + 2][j]]
        tri = sorted(tri)
        if tri[0] + tri[1] > tri[2]:
            possible += 1

print("Part 2: {}".format(possible))
