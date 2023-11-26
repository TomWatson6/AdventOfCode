
from collections import defaultdict
import gc

class Cube:
    def __init__(self, x_low, x_high, y_low, y_high, z_low, z_high, on):
        self.x_low = x_low
        self.x_high = x_high
        self.y_low = y_low
        self.y_high = y_high
        self.z_low = z_low
        self.z_high = z_high
        self.on = on

def p1(output):
    print("Part 1:", output)

def p2(output):
    print("Part 2:", output)

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

intersections = dict()
cubes = []

for line in lines:
    left, right = line.split(" ")
    x, y, z = [t.strip("x=").strip("y=").strip("z=") for t in right.split(",")]
    x_low, x_high = [int(t) for t in x.split("..")]
    y_low, y_high = [int(t) for t in y.split("..")]
    z_low, z_high = [int(t) for t in z.split("..")]
    cubes.append(Cube(x_low, x_high + 1, y_low, y_high + 1, z_low, z_high + 1, left == "on"))

X = []
Y = []
Z = []

for cube in cubes:
    X.append(cube.x_low)
    X.append(cube.x_high)
    Y.append(cube.y_low)
    Y.append(cube.y_high)
    Z.append(cube.z_low)
    Z.append(cube.z_high)

X.sort()
Y.sort()
Z.sort()
XS = len(X)
YS = len(Y)
ZS = len(Z)
XI = dict()
YI = dict()
ZI = dict()

for i in range(len(X)):
    XI[X[i]] = i

for i in range(len(Y)):
    YI[Y[i]] = i 

for i in range(len(Z)):
    ZI[Z[i]] = i

grid = dict()

for x, cube in enumerate(cubes):
    print("Starting instruction:", x)
    x0 = XI[cube.x_low]
    x1 = XI[cube.x_high]
    y0 = YI[cube.y_low]
    y1 = YI[cube.y_high]
    z0 = ZI[cube.z_low]
    z1 = ZI[cube.z_high]

    for x in range(x0, x1):
        for y in range(y0, y1):
            for z in range(z0, z1):
                if cube.on:
                    grid[(x, y, z)] = True
                elif grid.get((x, y, z)):
                    grid[(x, y, z)] = False
                    # del grid[(x, y, z)]
                    # gc.collect()
                grid[(x, y, z)] = cube.on

total = 0

for x in range(0, XS - 1):
    for y in range(0, YS - 1):
        for z in range(0, ZS - 1):
            add = 1 if grid.get((x, y, z)) == True else 0
            total += add * (X[x + 1] - X[x]) * (Y[y + 1] - Y[y]) * (Z[z + 1] - Z[z])

p2(total)
