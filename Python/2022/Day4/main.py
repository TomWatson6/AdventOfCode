

with open("input.txt") as f:
    ranges = [x.strip().split(",") for x in f.readlines()]

for i in range(len(ranges)):
    left, right = ranges[i]
    left = [int(x) for x in left.split("-")]
    right = [int(x) for x in right.split("-")]
    ranges[i] = (left, right)

p1, p2 = 0, 0

for r in ranges:
    left, right = r
    large = max([left, right], key=lambda k: (k[1] - k[0], k[1]))
    small = min([left, right], key=lambda k: (k[1] - k[0], k[1]))


    if small[0] >= large[0] and small[1] <= large[1]:
        p1 += 1

    if not (left[1] < right[0] or left[0] > right[1]):
        p2 += 1
    

print("Part 1:", p1)
print("Part 2:", p2)












