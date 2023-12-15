
def hash(s):
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val %= 256

    return val

with open(0) as file:
    strings = file.read().strip().split(",")

total = 0
power = 0
boxes = [[] for _ in range(256)]

for s in strings:
    if '-' in s:
        label, focal_length = s.split('-')
        i = hash(label)
        boxes[i] = [l for l in boxes[i] if l[0] != label]

    elif '=' in s:
        label, focal_length = s.split('=')
        i = hash(label)
        for x in range(len(boxes[i])):
            if boxes[i][x][0] == label:
                boxes[i][x] = (label, focal_length)
                break
        else:
            boxes[i].append((label, focal_length))
    else:
        assert False, s

    total += hash(s)

print("Part 1:", total)

for i, box in enumerate(boxes):
    for j, lens in enumerate(box):
        power += (i + 1) * (j + 1) * int(lens[1])

print("Part 2:", power)



















