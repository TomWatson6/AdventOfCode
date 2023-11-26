def p1(output):
    print("Part 1:", output)

def p2(output):
    print("Part 2:", output)

f = open("input.txt")
lines = [x.strip("\n").split(" ") for x in f.readlines()]
f.close()

x = 0
y = 0

for line in lines:
    if line[0] == "forward":
        x += int(line[1])
    elif line[0] == "down":
        y += int(line[1])
    else:
        y -= int(line[1])

p1(str(x * y))

x = 0
y = 0
aim = 0

for line in lines:
    if line[0] == "down":
        aim += int(line[1])
    elif line[0] == "up":
        aim -= int(line[1])
    else:
        x += int(line[1])
        y += (aim * int(line[1]))

p2(str(x * y))