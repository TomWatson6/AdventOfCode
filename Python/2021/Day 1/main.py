def p1(output):
    print("Part 1:", output)

def p2(output):
    print("Part 2:", output)

f = open("input.txt")
depths = [int(x.strip("\n")) for x in f.readlines()]
f.close()

increasing = 0

for x in range(1, len(depths), 1):
    if depths[x] > depths[x - 1]:
        increasing += 1

p1(increasing)

increasing = 0

for x in range(3, len(depths), 1):
    if depths[x] > depths[x - 3]:
        increasing += 1

p2(increasing)