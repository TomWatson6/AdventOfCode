import re

DIR = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]

ARROW = {
    (1, 0): '>',
    (0, 1): 'v',
    (-1, 0): '<',
    (0, -1): '^',
}


with open("input.txt") as f:
    input = f.read().split("\n\n")

grid = {}
found = False
pos = (0, 0)
facing = 0
dir = lambda: DIR[facing % len(DIR)]
XS, YS = 0, 0

# print(input[0].split("\n"))

for i, r in enumerate(input[0].split("\n")):
    # print(r)
    for j, c in enumerate(r):
        if not found and c == '.':
            found = True
            pos = (j, i)
        if i + 1 > YS:
            YS = i + 1
        if j + 1 > XS:
            XS = j + 1

        grid[(j, i)] = c

# print(grid)

for y in range(YS):
    for x in range(XS):
        if grid.get((x, y)) is None:
            grid[(x, y)] = ' '

def move_forward():
    global pos
    dx = abs(dir()[0])
    inc_pos = None
    if dx > 0:
        inc_pos = lambda p: (((p[0] + dir()[0]) % XS, p[1] + dir()[1]))
    else:
        inc_pos = lambda p: ((p[0] + dir()[0], (p[1] + dir()[1]) % YS))

    new_pos = inc_pos(pos)
    
    while grid[new_pos] not in ['#', '.']:
        new_pos = inc_pos(new_pos)

    if grid[new_pos] == '#':
        return False

    pos = new_pos

    return True

def move_forward2():
    global pos
    inc_pos = None
    new_pos = (pos[0] + dir()[0], pos[1] + dir()[1])
    if grid.get(new_pos) is None or grid.get(new_pos) == ' ':
        # Figure out where it needs to go from here
        # If top of front
        if 50 <= new_pos[0] < 100 and new_pos[1] < 0:
            pass
        # If left of front
        elif 0 <= new_pos[1] < 50 and new_pos[0] < 50:
            facing += 2 # From left to upside down right
            new_pos = (0, 100 + (49 - pos[1]))
            pass
        # If top of right
        elif 100 <= new_pos[0] < 150 and new_pos[1] < 0:
            pass
        # If right of right
        elif new_pos[0] >= 150:
            pass
        # If bottom of right
        elif 100 <= new_pos[0] < 150 and new_pos[1] >= 50:
            pass
        # If left of bottom
        elif new_pos[0] < 50 and 50 <= new_pos[1] < 100:
            pass
        # If right of bottom
        elif new_pos[0] >= 100 and 50 <= new_pos[1] < 100:
            pass
        # If right of back
        elif new_pos[0] >= 100 and 100 <= new_pos[1] < 150:
            pass
        # If bottom of back
        elif 50 <= new_pos[0] < 100 and new_pos[1] >= 150:
            pass
        # If top of left
        elif 0 <= new_pos[0] < 50 and new_pos[1] < 100:
            pass
        # If left of left
        elif new_pos[0] < 0 and 100 <= new_pos[1] < 150:
            pass
        # If left of top
        elif new_pos[0] < 0 and 150 <= new_pos[1] < 200:
            pass
        # If right of top
        elif new_pos[0] >= 50 and 150 <= new_pos[1] < 200:
            pass
        # If bottom of top
        elif 0 <= new_pos[0] < 50 and new_pos[1] >= 200:
            pass
        else:
            assert False
        

    if grid[new_pos] == '#':
        return False

    pos = new_pos

    return True


directions = list(re.findall("\d+|L|R", input[1]))
visited = {}

def print_grid():
    for y in range(YS):
        for x in range(XS):
            if (x, y) in visited:
                print(visited[(x, y)], end = "")
            else:
                print(grid[(x, y)], end = "")
        print()

# with open("output.txt", 'r+') as f:
# f.write(f"{(pos[1], pos[0])}\n")
for d in directions:
    if d == 'L':
        facing -= 1
    elif d == 'R':
        facing += 1
    else:
        mag = int(d)
        for _ in range(mag):
            visited[pos] = ARROW[dir()]
            if not move_forward():
                # print("HIT A WALL AT:", pos)
                break
        # f.write(f"{(pos[1], pos[0])}\n")

    # print(d, pos, dir())

visited[pos] = ARROW[dir()]
# print_grid()
# print(directions)

r = pos[1] + 1
c = pos[0] + 1
f = facing % len(DIR)
# print(facing)
# print(directions[:40])
print_grid()
print(r, c, f)

# print(directions)
print(r*1000 + c*4 + f)













