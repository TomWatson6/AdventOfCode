

with open("input.txt") as f:
    input = [x.strip() for x in f.readlines()]

dims = [x.split("x") for x in input]
dims = [[int(y) for y in x] for x in dims]

total = 0

for dim in dims:
    x = dim[0] * dim[1] * 2
    y = dim[1] * dim[2] * 2
    z = dim[0] * dim[2] * 2

    total += x + y + z

    s = sorted(dim)
    total += s[0] * s[1]

print("Part 1:", total)

total = 0

for dim in dims:
    s = sorted(dim)
    perim = 2 * (s[0] + s[1])
    volume = dim[0] * dim[1] * dim[2]

    total += perim + volume
    
print("Part 2:", total)