

with open("input.txt") as f:
    input = f.read().strip()

p1 = 0
p2 = 0

for i in range(len(input) - 3):
    s = set()
    [s.add(input[x]) for x in range(i, i + 4)]
    if len(s) == 4 and p1 == 0:
        p1 = i + 4
    
    s2 = set()
    [s2.add(input[x]) for x in range(i, i + 14)]
    if len(s2) == 14:
        p2 = i + 14
        break

print("Part 1:", p1)
print("Part 2:", p2)











