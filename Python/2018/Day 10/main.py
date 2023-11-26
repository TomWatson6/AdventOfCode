import re

def has_correct_height(grid):
    Y = min(x[1] for x in grid)
    YS = max(x[1] for x in grid)
    # 9 was found from observing height every iteration until it reached it's smallest, 9
    # slightly brute force, but works
    return YS - Y == 9

def progress(grid):
    new_grid = set()

    for v in grid:
        new_grid.add((v[0] + v[2], v[1] + v[3], v[2], v[3]))

    return new_grid

with open("input.txt") as f:
    input = [tuple([int(a) for a in x]) for x in [list(re.findall("(\-?\d+)", line.strip())) for line in f.readlines()]]

grid = set()

for pos_x, pos_y, vel_x, vel_y in input:
    grid.add((pos_x, pos_y, vel_x, vel_y))

time = 0
smallest = int(1e9)

while not has_correct_height(grid):
    new_grid = progress(grid)
    assert new_grid != grid
    grid = new_grid
    time += 1

points = [(x, y) for x, y, vx, vy in grid]

X = min(t[0] for t in grid)
XS = max(t[0] for t in grid)
Y = min(t[1] for t in grid)
YS = max(t[1] for t in grid)

print("Part 1:")
for y in range(Y, YS + 1):
    for x in range(X, XS + 1):
        if (x, y) in points:
            print("#", end="")
        else:
            print(" ", end="")
    print()

assert len(grid) == len(input)
print("Part 2:", time)





















