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
    to_add = int(str(digits[0]) + str(digits[-1]))
    total += to_add

print("Part 1:", total)
total = 0

for line in [re.findall(r"(?=(\d|" + "|".join(C) + "))", line) for line in lines]:
    digits = []

    for r in line:
        if r in C:
            digits.append(C.index(r) + 1)
        else:
            digits.append(int(r))

    to_add = int(str(digits[0]) + str(digits[-1]))
    total += to_add

print("Part 2:", total)












