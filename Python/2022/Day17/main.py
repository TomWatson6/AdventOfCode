

FLOOR = 0
high = 0
DIST_FROM_HIGH = 4
obj = 0

DIR = {
    '<': (-1, 0),
    '>': (1, 0),
    '': (0, 1),
}

def read_rocks():
    R = []

    with open("rocks.txt") as f:
        rocks = [x.strip() for x in f.read().split("\n\n")]
        rocks = [[list(y) for y in x.split("\n")] for x in rocks]

    for rock in rocks:
        entry = set()
        for r in range(len(rock)):
            for c in range(len(rock[0])):
                if rock[r][c] == '#':
                    entry.add((c, r))

        R.append(entry)

    return R

def get_start(rock):
    r = set()
    YS = max(rock, key=lambda k: k[1])[1]

    for c in rock:
        r.add((c[0] + 3, c[1] - high - DIST_FROM_HIGH - YS))

    return r

def move(grid, rock, input):
    dir = DIR[input]

    MX = min(rock, key=lambda k: k[0])[0]
    SX = max(rock, key=lambda k: k[0])[0]
    SY = max(rock, key=lambda k: k[1])[1]

    # Stop moving through floor
    if input == '' and SY == FLOOR - 1:
        return rock, False
    
    # Stop moving through left wall
    if MX == 1 and input == '<':
        return rock, False

    # Stop moving through right wall
    if SX == 7 and input == '>':
        return rock, False

    new_rock = set()

    for r in rock:
        new_rock.add((r[0] + dir[0], r[1] + dir[1]))

    # Stop moving into another fallen piece
    if len(grid.intersection(new_rock)) > 0 and input == '':
        return rock, False
    elif len(grid.intersection(new_rock)) > 0 and input != '':
        return rock, True
    else:
        return new_rock, True

grid = set()

def print_grid():
    low_y = min(grid, key=lambda k: k[1])[1]
    high_y = max(grid, key=lambda k: k[1])[1]
    for y in range(low_y, high_y + 1):
        for x in range(0, 9):
            if x == 0 or x == 8:
                print("|", end="")
            elif (x, y) in grid:
                print("#", end="")
            else:
                print(".", end="")

        print()


with open("input.txt") as f:
    instructions = list(f.read())

rocks = read_rocks()
print(rocks)
print(instructions)

curr = None
count = 0
i = 0
#limit = 1000000000000
limit = 2022

while count < limit:
    m = instructions[i%len(instructions)]
    if curr is None:
        curr = get_start(rocks[obj % len(rocks)])
    # print(m)

    # print(curr)

    # Side move
    curr, moved = move(grid, curr, m)

    # Down move
    curr, moved = move(grid, curr, '')

    if not moved:
        top = min(curr, key=lambda k: k[1])[1]
        bottom = max(curr, key=lambda k: k[1])[1]

        for c in curr:
            grid.add(c)
        
        count += 1

        # high += bottom - top + 1
        high = -min(grid, key=lambda k: k[1])[1]
        obj += 1
        curr = None
        # print(count, high, obj)
        # print_grid()

    i += 1



print(grid)

low_x = min(grid, key=lambda k: k[0])[0]
high_x = max(grid, key=lambda k: k[0])[0]
low_y = min(grid, key=lambda k: k[1])[1]
high_y = max(grid, key=lambda k: k[1])[1]

print_grid()

x = high_x - low_x + 1
y = high_y - low_y + 1

print(y)







