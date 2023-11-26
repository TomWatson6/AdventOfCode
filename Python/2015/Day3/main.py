
with open("input.txt") as f:
    directions = [x for x in f.read().strip()]

curr = [0, 0]
visited = {
    (0, 0): True
}

for dir in directions:
    if dir == "<":
        curr[0] -= 1
    elif dir == ">":
        curr[0] += 1
    elif dir == "^":
        curr[1] -= 1
    elif dir == "v":
        curr[1] += 1
    else:
        exit(-1)

    visited[tuple(curr)] = True

print("Part 1:", len(visited.keys()))

curr = [
    [0, 0],
    [0, 0]
]
santa = 0
visited = {
    (0, 0): True
}

for dir in directions:
    who = santa % 2
    if dir == "<":
        curr[who][0] -= 1
    elif dir == ">":
        curr[who][0] += 1
    elif dir == "^":
        curr[who][1] -= 1
    elif dir == "v":
        curr[who][1] += 1
    else:
        exit(-1)

    visited[tuple(curr[who])] = True
    santa += 1

print("Part 2:", len(visited.keys()))