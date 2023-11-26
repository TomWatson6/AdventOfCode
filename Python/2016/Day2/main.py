
moves = {
    'U': [0, -1],
    'D': [0, 1],
    'L': [-1, 0],
    'R': [1, 0]
}

def read_numpad(file_name):
    with open(file_name) as f:
        input = [[y.strip() for y in x.split(" ")] for x in f.readlines() if x != ""]

    numpad = {}

    for i, row in enumerate(input):
        for j, col in enumerate(row):
            if col != "":
                numpad[(j, i)] = col

    return numpad

numpad = read_numpad("numpad1.txt")

def read_instructions(file_name):
    with open(file_name) as f:
        input = [x.strip() for x in f.readlines()]

    return [[y for y in x] for x in input]

def get_next(pos, move):
    next = (pos[0] + moves[move][0], pos[1] + moves[move][1])
    if numpad.get(next) != None:
        return next
    else:
        return pos


instructions = read_instructions("input.txt")
pos = (1, 1)
sequence = ""

for ins in instructions:
    for move in ins:
        pos = get_next(pos, move)

    sequence += numpad[pos]

print("Part 1: {}".format(sequence))

numpad = read_numpad("numpad2.txt")

pos = (0, 2)
sequence = ""

for ins in instructions:
    for move in ins:
        pos = get_next(pos, move)

    sequence += numpad[pos]

print("Part 2: {}".format(sequence))


