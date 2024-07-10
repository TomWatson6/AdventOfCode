import re

with open("input.txt") as f:
    json = f.read().strip()

numbers = re.findall(r"(-?\d+)", json)

print("Part 1:", sum([int(x) for x in numbers]))

index = 0

while True:
    try:
        index = json.index("red", index)
    except:
        break

    left = index
    right = index
    depth = 0
    while json[left] not in ["{", "["] or depth <= 0:
        left -= 1
        if json[left] in ["}", "]"]:
            depth -= 1
        if json[left] in ["{", "["]:
            depth += 1

    depth = 0
    while json[right] not in ["}", "]"] or depth <= 0:
        right += 1
        if json[right] in ["}", "]"]:
            depth += 1
        if json[right] in ["{", "["]:
            depth -= 1

    if json[left] == "{":
        print("Removing:", json[left:right])
        json = json[:left] + json[right + 1:]
        index = left
        continue

    index += 3

numbers = re.findall(r"(-?\d+)", json)

print("Part 2:", sum([int(x) for x in numbers]))




















