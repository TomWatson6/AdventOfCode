import re

def get_ranges(scanners, exc, is_row):
    ranges = []
    
    for s, b in scanners.items():
        m = abs(b[0] - s[0]) + abs(b[1] - s[1])
        d = 0
        if is_row:
            d = abs(s[1] - exc)
        else:
            d = abs(s[0] - exc)
        if d >= m:
            continue
        disp = (m - d)
        lower = 0
        upper = 0
        if is_row:
            lower = s[0] - disp
            upper = s[0] + disp
        else:
            lower = s[1] - disp
            upper = s[1] + disp

        if is_row:
            if b[0] == lower:
                lower += 1
            if b[0] == upper:
                upper -= 1
        else:
            if b[1] == lower:
                lower += 1
            if b[1] == upper:
                upper -= 1

        ranges.append((lower, upper))

    return ranges

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) // div
    y = det(d, ydiff) // div
    return x, y

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

scanners = {}

for line in lines:
    x1, y1, x2, y2 = [int(x.strip("x=").strip("y=")) for x in re.findall(".{1}\=\-?\d+", line)]
    scanners[(x1, y1)] = (x2, y2)

exc_row = 2000000
total = 0

ranges = get_ranges(scanners, exc_row, True)

S = set()

for r in ranges:
    for i in range(r[0], r[1] + 1):
        S.add(i)

print("Part 1:", len(S))

high = 4000000

lines = []

for s, b in scanners.items():
    dx = abs(s[0] - b[0])
    dy = abs(s[1] - b[1])
    m = dx + dy
    points = [(s[0] - m, s[1]), (s[0], s[1] - m), (s[0] + m, s[1]), (s[0], s[1] + m)]
    for i in range(len(points)):
        lines.append((points[i], points[(i+1)%len(points)]))

I = set()

for i in range(len(lines) - 1):
    for j in range(1, len(lines)):
        I.add(line_intersection(lines[i], lines[j]))

I = [x for x in I if x is not None]
I = [x for x in I if 0 <= x[0] <= high]
I = [x for x in I if 0 <= x[1] <= high]

I = sorted(I, key=lambda i: (i[0], i[1]))

S = set()

I = sorted(I, key=lambda k: k[0])

for i in range(len(I) - 1):
    for j in range(1, len(I)):
        if I[i][1] == I[j][1]:
            if I[j][0] - I[i][0] > 2:
                break
            elif I[j][0] - I[i][0] == 2:
                x = (I[j][0] + I[i][0]) // 2
                y = I[i][1]
                points = []
                for point in I:
                    if point == (x, y - 1) or point == (x, y + 1):
                        points.append(point)

                if len(points) == 2:
                    S.add(((I[i][0] + I[j][0]) // 2, (points[0][1] + points[1][1]) // 2))

S_ = set()

for pos in S:
    for s, b in scanners.items():
        dx = abs(s[0] - b[0])
        dy = abs(s[1] - b[1])
        m = dx + dy
        dx0 = abs(s[0] - pos[0])
        dy0 = abs(s[1] - pos[1])
        m0 = dx0 + dy0
        if m0 > m:
            S_.add(pos)

S = S_

x, y = list(S)[0]
print("Part 2:", x * 4000000 + y)
