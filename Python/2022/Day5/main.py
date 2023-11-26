

def get_input(file_name):
    with open(file_name) as f:
        left, right = [x.split("\n") for x in f.read().split("\n\n")]

    left.pop()
    rows = []

    for l in left:
        row = []
        for a in range(1, len(l), 4):
            row.append(l[a])
        rows.append(row)

    stacks = []

    for x in range(len(rows[0])):
        stack = []
        for y in range(len(rows) - 1, -1, -1):
            stack.append(rows[y][x])

        stacks.append([s for s in stack if s != " "])

    return stacks, right

stacks, instructions = get_input("input.txt")

for ins in instructions:
    split = ins.split(" ")
    quant, before, after = int(split[1]), int(split[3]), int(split[5])

    for _ in range(quant):
        stacks[after - 1].append(stacks[before - 1].pop())

output = ""

for s in stacks:
    output += s[-1]

print("Part 1:", output)

stacks, instructions = get_input("input.txt")

for ins in instructions:
    split = ins.split(" ")
    quant, before, after = int(split[1]), int(split[3]), int(split[5])

    to_move = []

    for _ in range(quant):
        to_move.append(stacks[before - 1].pop())

    to_move = to_move[::-1]

    [stacks[after - 1].append(x) for x in to_move]

output = ""

for s in stacks:
    output += s[-1]

print("Part 2:", output)
