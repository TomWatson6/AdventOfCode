import sympy

# class Hailstone:
#     def __init__(self, sx, sy, sz, vx, vy, vz):
#         self.sx = sx
#         self.sy = sy
#         self.sz = sz
#         self.vx = vx
#         self.vy = vy
#         self.vz = vz

#         self.a = vy
#         self.b = -vx
#         self.c = vy * sx - vx * sy

#     def __repr__(self):
#         return "Hailstone{" + f"a={self.a}, b={self.b}, c={self.c}" + "}"

with open(0) as f:
    lines = [x.strip() for x in f.readlines()]

hailstones = []

for line in lines:
    line = line.replace("@", ",")
    line = tuple(map(int, line.split(", ")))
    hailstones.append(line)

xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

total = 0
lower = 7 if len(lines) < 10 else 200000000000000
upper = 24 if len(lines) < 10 else 400000000000000

equations = []

for i, (sx, sy, sz, vx, vy, vz) in enumerate(hailstones):
    equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
    equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
    if i < 2:
        continue
    answers = [soln for soln in sympy.solve(equations) if all(x % 1 == 0 for x in soln.values())]
    if len(answers) == 1:
        break

answer = answers[0]
print(answer[xr] + answer[yr] + answer[zr])

# for i, hs1 in enumerate(hailstones):
#     for hs2 in hailstones[:i]:
#         px, py = sympy.symbols("px py")
#         answers = sympy.solve([vy * (px - sx) - vx * (py - sy) for sx, sy, _, vx, vy, _ in [hs1, hs2]])
#         if answers == []:
#             continue
#         x, y = answers[px], answers[py]
#         if lower <= x <= upper and lower <= y <= upper:
#             if all((x - sx) * vx >= 0 and (y - sy) * vy >= 0 for sx, sy, _, vx, vy, _ in [hs1, hs2]):
#                 total += 1

# for i, hs1 in enumerate(hailstones):
#     for hs2 in hailstones[:i]:
#         a1, b1, c1 = hs1.a, hs1.b, hs1.c
#         a2, b2, c2 = hs2.a, hs2.b, hs2.c

#         if a1 * b2 == b1 * a2:
#             continue

#         x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
#         y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)

#         if lower <= x <= upper >= y >= lower:
#             if all((x - hs.sx) * hs.vx >= 0 and (y - hs.sy) * hs.vy >= 0 for hs in (hs1, hs2)):
#                 total += 1

# print(total)
















