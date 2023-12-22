from collections import defaultdict

with open(0) as f:
    lines = [x.strip() for x in f.readlines()]

bricks = []

for start, end in [line.split("~") for line in lines]:
    start = list(map(int, start.split(",")))
    end = list(map(int, end.split(",")))
    assert all(a <= b for a, b in zip(start, end))

    brick = set()

    for x in range(start[0], end[0] + 1):
        for y in range(start[1], end[1] + 1):
            for z in range(start[2], end[2] + 1):
                brick.add((x, y, z))

    bricks.append(brick)

bricks = sorted(bricks, key=lambda b: min(a[2] for a in b))

def fall(bricks):
    placed = {}
    changed = 0
    for i in range(len(bricks)):
        change = False
        while len(placed) != len(bricks):
            new_brick = set()
            floored = False

            for b in bricks[i]:
                x, y, z = b
                if z - 1 < 1:
                    floored = True
                    break
                new_brick.add((x, y, z - 1))

            if floored:
                break

            intersecting = False

            for b in range(len(bricks)):
                if i == b:
                    continue
                if len(bricks[b] & new_brick) != 0:
                    intersecting = True
                    break

            if not intersecting:
                bricks[i] = new_brick
                change = True
            else:
                placed[i] = True
                break
        if change:
            changed += 1

    return bricks, changed

bricks, _ = fall(bricks)

safe = 0
supports = {}

for i, b in enumerate(bricks):
    supported_by = set()

    for x, y, z in b:
        for j, b2 in enumerate([t for t in bricks if t != b]):
            if any(x2 == x and y2 == y and z2 + 1 == z for x2, y2, z2 in b2):
                supported_by.add(j)

    supports[i] = supported_by

excluded = set()

for k, v in supports.items():
    if len(v) == 1:
        excluded.add(list(v)[0])

print("Part 1:", len(bricks) - len(excluded))

total = 0

for i, b in enumerate(bricks):
    if i not in excluded:
        continue

    altered = [b for j, b in enumerate(bricks) if j != i]
    altered_after, changed = fall(altered)
    total += changed

print("Part 2:", total)

























