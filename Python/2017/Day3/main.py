
with open("input.txt") as f:
    number = int(f.read().strip())

D = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]

M = {(0, 0): 1}

pos = (0, 0)
dir = 0
visited = set()
visited.add(pos)

def next(pos, dir):
    global D
    return (pos[0] + D[dir % len(D)][0], pos[1] + D[dir % len(D)][1])

def get_adj_sum(pos):
    global D
    total = 0

    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == y:
                continue
            coord = (pos[0] + x, pos[1] + y)
            if coord in M:
                total += M[coord]

    return total

p2_solved = False
p2 = 0

for _ in range(number - 1):
    pos = next(pos, dir)
    M[pos] = get_adj_sum(pos)
    if M[pos] > number and not p2_solved:
        p2 = M[pos]
        p2_solved = True
    visited.add(pos)
    if next(pos, dir + 1) not in visited:
        dir += 1

print("Part 1:", abs(pos[0]) + abs(pos[1]))
print("Part 2:", p2)


















