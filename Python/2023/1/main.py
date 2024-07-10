import re

with open(0) as f:
    lines = [x.strip() for x in f.readlines()]

C = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def convert(i):
    if i in C:
        return C[i]

    return i

total = 0

def replace_nums(s, p2):
    if p2:
        for num, digit in C.items():
            s = s.replace(num, f"{num[0]}{digit}{num[-1]}")

    return s

for line in lines:
    line = replace_nums(line, False)
    matches = re.findall(r"\d", line)
    total += int(matches[0] + matches[-1])

print("Part 1:", total)

total = 0

for line in lines:
    line = replace_nums(line, True)
    matches = re.findall(r"\d", line)
    total += int(matches[0] + matches[-1])

print("Part 2:", total)
















