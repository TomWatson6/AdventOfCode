import re

lower = 48
upper = 57
dash = 45
regex = """\{+[0-9A-Za-z:\-",]*(?<!\[):"red"(?!\])[0-9A-Za-z:\-",]*\}+"""
regex2 = """\{+[0-9A-Za-z:\-",\[\]]*(?<=(\[.*\])*):"red"(?=(\[.*\])*)[0-9A-Za-z:\-",\[\]]*\}+"""

def count_numbers(s):
    numbers = []
    current = ""

    for c in s:
        ch = ord(c)
        if (ch >= lower and ch <= upper) or ch == dash:
            current += c
        else:
            numbers.append(current)
            current = ""

    return sum([int(n) for n in numbers if n != ""])

def remove_red(s):
    occurences = re.findall(regex, s)
    while len(occurences) > 0:
        for o in occurences:
            s = s.replace(str(o), "")
        occurences = re.findall(regex, s)

    # occurences = re.findall(regex2, s)
    # while len(occurences) > 0:
    #     for o in occurences:
    #         s = s.replace(str(o), "")
    #     occurences = re.findall(regex2, s)

    # with open("output.txt", "w") as f:
    #     f.write(s)

    return s

with open("input.txt") as f:
    input = f.read().strip()

p1 = count_numbers(input)

print("Part 1:", p1)

input = remove_red(input)

with open("input2.txt") as f:
    input2 = f.read().strip()

p2 = count_numbers(input2)

print("Part 2:", p2)

