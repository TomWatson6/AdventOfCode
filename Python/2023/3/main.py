import re

with open(0) as f:
    lines = [x.strip() for x in f.readlines()]

total = 0
blocks_coord = []
blocks = []

def get_block_coord(i, j, t):
    block_coord = []

    for y in range(i - 1, i + 2):
        for x in range(j - 1, j + t + 1):
            if y >= 0 and y < len(lines) and x >= 0 and x < len(lines[0]):
                block_coord.append((y, x))

    return block_coord

def get_block(i, j, t):
    block = []

    for y in range(i - 1, i + 2):
        for x in range(j - 1, j + t + 1):
            if y >= 0 and y < len(lines) and x >= 0 and x < len(lines[0]):
                block.append(lines[y][x])

    return block

for i, r in enumerate(lines):
    S = set()
    for j, c in enumerate(r):
        if j in S:
            continue
        S.add(j)
        if c.isnumeric():
            num = ""
            t = 0
            while lines[i][j + t].isnumeric():
                num += lines[i][j + t]
                t += 1
                if j + t >= len(lines[i]):
                    break
            [S.add(j + x) for x in range(t)]
            blocks_coord.append((int(num), get_block_coord(i, j, t)))
            blocks.append((int(num), get_block(i, j, t)))

total = 0

for block in blocks:
    if any(b != "." and not b.isnumeric() for b in block[1]):
        total += block[0]

print("Part 1:", total)

total = 0

for i in range(len(blocks_coord) - 1):
    for j in range(i + 1, len(blocks_coord)):
        inter = set(blocks_coord[i][1]).intersection(set(blocks_coord[j][1]))
        if len(inter) > 0:
            if any([lines[b[0]][b[1]] == "*" for b in inter]):
                total += blocks_coord[i][0] * blocks_coord[j][0]

print("Part 2:", total)



















