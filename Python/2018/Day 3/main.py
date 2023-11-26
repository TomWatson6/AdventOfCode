

f = open("input.txt")
lines = [x.strip() for x in f.readlines()]
f.close()

lines = [x.split(" ") for x in lines]

fabric = dict()
elf_covering = dict()
covered_by_elf = dict()
overlap = 0

for line in lines:
    edge_x, edge_y = [int(x.strip(":")) for x in line[2].split(",")]
    dim_x, dim_y = [int(x) for x in line[3].split("x")]
    elf = int(line[0].strip("#"))

    for x in range(edge_x, edge_x + dim_x):
        for y in range(edge_y, edge_y + dim_y):
            if covered_by_elf.get((x, y)) != None:
                covered_by_elf[(x, y)].append(elf)
            else:
                covered_by_elf[(x, y)] = [elf]

            if elf_covering.get(elf) != None:
                elf_covering[elf].append((x, y))
            else:
                elf_covering[elf] = [(x, y)]

            if fabric.get((x, y)) == None:
                fabric[(x, y)] = 1
            elif fabric.get((x, y)) == 1:
                overlap += 1
                fabric[(x, y)] += 1

for covered in covered_by_elf:
    if len(covered_by_elf[covered]) > 1:
        for elf in covered_by_elf[covered]:
            elf_covering[elf] = None

elf = -1

for key in elf_covering:
    if elf_covering.get(key) != None:
        elf = key

print("Part 1:", overlap)
print("Part 2:", elf)