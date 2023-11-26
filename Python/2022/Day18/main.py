
def adjacents(grid, cube):
    A = []

    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                if x == 0 and y == 0 and z == 0:
                    continue
                if abs(x) + abs(y) + abs(z) > 1:
                    continue
                a = (cube[0] + x, cube[1] + y, cube[2] + z)
                if a in grid:
                    A.append(a)

    return A

def water_adj(grid, water, cube):
    A = []

    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                if x == 0 and y == 0 and z == 0:
                    continue
                if abs(x) + abs(y) + abs(z) > 1:
                    continue
                a = (cube[0] + x, cube[1] + y, cube[2] + z)
                if cube in grid and a in water:
                    A.append(a)

    return A

def empty_adj(grid, water, cube):
    A = []

    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                if x == 0 and y == 0 and z == 0:
                    continue
                if abs(x) + abs(y) + abs(z) > 1:
                    continue
                a = (cube[0] + x, cube[1] + y, cube[2] + z)
                if a not in water and a not in grid:
                    A.append(a)

    return A

with open("input.txt") as f:
    cubes = [list(map(int, x.strip().split(","))) for x in f.readlines()]

grid = set()

for c in cubes:
    grid.add(tuple(c))

total = 0

for c in cubes:
    total += 6 - len(adjacents(grid, c))

print("Part 1:", total)

x_low = min(cubes, key=lambda k: k[0])[0] - 1
x_high = max(cubes, key=lambda k: k[0])[0] + 1
y_low = min(cubes, key=lambda k: k[1])[1] - 1
y_high = max(cubes, key=lambda k: k[1])[1] + 1
z_low = min(cubes, key=lambda k: k[2])[2] - 1
z_high = max(cubes, key=lambda k: k[2])[2] + 1

water = set()

# From (X, Y) plane scan inwards
for x in range(x_low, x_high + 1):
    for y in range(y_low, y_high + 1):
        for z in range(z_low, z_high + 1):
            if (x, y, z) not in grid:
                water.add((x, y, z))
            else:
                break
        for z in range(z_high, z_low - 1, -1):
            if (x, y, z) not in grid:
                water.add((x, y, z))
            else:
                break

# From (X, Z) plane scan inwards
for x in range(x_low, x_high + 1):
    for z in range(z_low, z_high + 1):
        for y in range(y_low, y_high + 1):
            if (x, y, z) not in grid:
                water.add((x, y, z))
            else:
                break
        for y in range(y_high, y_low - 1, -1):
            if (x, y, z) not in grid:
                water.add((x, y, z))
            else:
                break

# From (Y, Z) plane scan inwards
for y in range(y_low, y_high + 1):
    for z in range(z_low, z_high + 1):
        for x in range(x_low, x_high + 1):
            if (x, y, z) not in grid:
                water.add((x, y, z))
            else:
                break

        for x in range(x_high, x_low - 1, -1):
            if (x, y, z) not in grid:
                water.add((x, y, z))
            else:
                break

total = 0

wx_low = min(cubes, key=lambda k: k[0])[0] - 1
wx_high = max(cubes, key=lambda k: k[0])[0] + 1
wy_low = min(cubes, key=lambda k: k[1])[1] - 1
wy_high = max(cubes, key=lambda k: k[1])[1] + 1
wz_low = min(cubes, key=lambda k: k[2])[2] - 1
wz_high = max(cubes, key=lambda k: k[2])[2] + 1

# Expand the water on the outside to fill all the cracks
def expand_water(grid, water):
    for x in range(wx_low + 1, wx_high):
        for y in range(wy_low + 1, wy_high):
            for z in range(wz_low + 1, wz_high):
                adj = []
                if (x, y, z) in water:
                    adj = empty_adj(grid, water, (x, y, z))
                for a in adj:
                    water.add(a)

for _ in range(10):
    expand_water(grid, water)

for x in range(wx_low, wx_high + 1):
    for y in range(wy_low, wy_high + 1):
        for z in range(wz_low, wz_high + 1):
            total += len(water_adj(grid, water, (x, y, z)))

print("Part 2:", total)

def print_slice():
    for z in range(wz_low, wz_high + 1):
        for x in range(wx_low, wx_high + 1):
            for y in range(wy_low, wy_high + 1):
                if (x, y, z) in water:
                    print("W", end="")
                elif (x, y, z) in grid:
                    print("#", end="")
                else:
                    print(" ", end="")
            print()
        print()
        print()





