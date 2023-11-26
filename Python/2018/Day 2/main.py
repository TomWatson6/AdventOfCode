

f = open("input.txt")
boxes = [x.strip() for x in f.readlines()]
f.close()

two = 0
three = 0

for box in boxes:
    counts = dict()
    for letter in box:
        if counts.get(letter):
            counts[letter] += 1
        else:
            counts[letter] = 1

    for count in counts:
        if counts[count] == 2:
            two += 1
            break

    for count in counts:
        if counts[count] == 3:
            three += 1
            break

print("Part 1:", two * three)

characters = []
found = False

for x in range(len(boxes) - 1):
    for y in range(1, len(boxes)):
        if boxes[x] == boxes[y]:
            continue
        diff = 0
        characters = []
        for z in range(len(boxes[x])):
            if boxes[y][z] != boxes[x][z]:
                diff += 1
            else:
                characters.append(boxes[x][z])
        if diff == 1:
            found = True
            break
    if found:
        break

print("Part 2:", ''.join(characters))