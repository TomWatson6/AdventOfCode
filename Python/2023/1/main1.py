import re

C = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

total = 0

for line in lines:
    digits = []

    for c in line:
        if c.isnumeric():
            digits.append(c)
    total += int(digits[0] + digits[-1])

print("Part 1:", total)

total = 0

for line in [re.findall(r"(?=(\d|" + "|".join(C) + "))", line) for line in lines]:
    digits = []

    for r in line:
        if r in C:
            digits.append(C.index(r) + 1)
        else:
            digits.append(int(r))

    total += int(str(digits[0]) + str(digits[-1]))

print("Part 2:", total)












