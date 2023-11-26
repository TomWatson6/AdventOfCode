
def process(num):
    next = ""
    last = num[0]
    sections = []
    section = ""

    for i, c in enumerate(num):
        if c != last or i == len(num) - 1:
            sections.append(section)
            section = ""
            if i == len(num) - 1:
                sections += c
                sections.append(section)
        section += c
        last = c

    sections = [s for s in sections if s != ""]

    # print(sections)
    for s in sections:
        next += str(len(s)) + s[0]

    return next

number = ""

with open("input.txt") as f:
    number = f.read().strip()

for i in range(50):
    if i == 40:
        print("Part 1:", len(number))
    number = process(number)

print("Part 2:", len(number))
