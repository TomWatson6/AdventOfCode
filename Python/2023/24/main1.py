import numpy as np

def get_intersect(a1, a2, b1, b2):
    s = np.vstack([a1,a2,b1,b2])        # s for stacked
    h = np.hstack((s, np.ones((4, 1)))) # h for homogeneous
    l1 = np.cross(h[0], h[1])           # get first line
    l2 = np.cross(h[2], h[3])           # get second line
    x, y, z = np.cross(l1, l2)          # point of intersection
    if z == 0:                          # lines are parallel
        return (float('inf'), float('inf'))
    return (x/z, y/z)

with open(0) as f:
    lines = [x.strip() for x in f.readlines()]

# lines = """0, 0, 0 @ 1, 1, 0
# 1, 1, 0 @ 1, 0, 0"""

# lines = [x.strip() for x in lines.split("\n")]

stones = []

for line in lines:
    px, py, pz, _, vx, vy, vz = [x.strip(",") for x in line.split(" ") if x != ""]
    stones.append((int(px), int(py), int(pz), int(vx), int(vy), int(vz)))

T = 1000000000000000 if len(lines) > 10 else 200

lines = []

for stone in stones:
    lines.append(((stone[0], stone[1]), (stone[0] + T * stone[3], stone[1] + T * stone[4])))

def sign(a):
    return (a > 0) - (a < 0)

inters = 0

lower = 200000000000000 if len(lines) > 10 else 7
upper = 400000000000000 if len(lines) > 10 else 27

for i in range(len(lines) - 1):
    for j in range(i + 1, len(lines)):
        l1, l2 = lines[i], lines[j]
        intersection = get_intersect(l1[0], l1[1], l2[0], l2[1])
        if intersection != (float('inf'), float('inf')):
            x, y = intersection
            if lower <= x <= upper and lower <= y <= upper:
                si = sign(l1[1][0] - l1[0][0])
                if si == 1 and (x < l1[0][0] or x > l1[1][0]):
                    continue
                if si == -1 and (x > l1[0][0] or x < l1[1][0]):
                    continue
                si = sign(l1[1][1] - l1[0][1])
                if si == 1 and (y < l1[0][1] or y > l1[1][1]):
                    continue
                if si == -1 and (y > l1[0][1] or y < l1[1][1]):
                    continue

                si = sign(l2[1][0] - l2[0][0])
                if si == 1 and (x < l2[0][0] or x > l2[1][0]):
                    continue
                if si == -1 and (x > l2[0][0] or x < l2[1][0]):
                    continue
                si = sign(l2[1][1] - l2[0][1])
                if si == 1 and (y < l2[0][1] or y > l2[1][1]):
                    continue
                if si == -1 and (y > l2[0][1] or y < l2[1][1]):
                    continue


                inters += 1

print(inters)

X = [(x[0], x[3]) for x in stones]
Y = [(x[1], x[4]) for x in stones]
Z = [(x[2], x[5]) for x in stones]

XP = []
YP = []
ZP = []

for i in range(len(X) - 1):
    for j in range(i + 1, len(X)):
        p, x1 = X[i]
        q, x2 = X[j]

        if p == q or x1 == x2:
            intersection = 0
            XP.append((intersection, p + x1 * intersection))
            # XP.append((p, x1, q, x2, intersection))
            continue

        intersection = (q - p) / (x1 - x2)
        XP.append((intersection, p + x1 * intersection))
        # XP.append(p + x1 * intersection)
        # XP.append((p, x1, q, x2, intersection))

        p, y1 = Y[i]
        q, y2 = Y[j]

        if p == q or y1 == y2:
            intersection = 0
            YP.append(intersection)
            continue

        intersection = (q - p) / (y1 - y2)
        YP.append(intersection)

        p, z1 = Z[i]
        q, z2 = Z[j]

        if p == q or z1 == z2:
            intersection = 0
            ZP.append(intersection)
            continue

        intersection = (q - p) / (z1 - z2)
        ZP.append(intersection)

XP = sorted(XP)
YP = sorted(YP)
ZP = sorted(ZP)

# print(XP)
# print(YP)
# print(ZP)



















