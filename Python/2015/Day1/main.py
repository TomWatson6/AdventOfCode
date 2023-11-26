

with open("input.txt") as f:
    chars = [x for x in f.read().strip()]

curr = 0

for c in chars:
    if c == "(":
        curr += 1
    else:
        curr -= 1

print("Part 1:", curr)

curr = 0
pos = 0

for i, c in enumerate(chars):
    if c == "(":
        curr += 1
    else:
        curr -= 1

    if curr < 0:
        pos = i + 1
        break

print("Part 2:", pos)