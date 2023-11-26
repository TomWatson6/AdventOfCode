

with open("input.txt") as f:
    input = [x.strip(",") for x in f.read().split(" ") if x != ""]

pos = [0, 0]
dir = 0
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for x in input:
    if x[0] == 'L':
        dir -= 1
    else:
        dir += 1

    mag = int(x[1:])
    d = dirs[dir % len(dirs)]

    pos[0] += d[0] * mag
    pos[1] += d[1] * mag

print("Part 1: {}".format(abs(pos[0]) + abs(pos[1])))

pos = [0, 0]
dir = 0
visited = {(0, 0): True}
found = False

for x in input:
    if x[0] == 'L':
        dir -= 1
    else:
        dir += 1

    mag = int(x[1:])
    d = dirs[dir % len(dirs)]

    for _ in range(mag):
        pos[0] += d[0]
        pos[1] += d[1]
        if visited.get(tuple(pos)):
            found = True
            break
        else:
            visited[tuple(pos)] = True

    if found:
        break

print("Part 2: {}".format(abs(pos[0]) + abs(pos[1])))
