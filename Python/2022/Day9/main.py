
with open("input.txt") as f:
    lines = [x.strip().split(" ") for x in f.readlines()]

lines = [(x[0], int(x[1])) for x in lines]

head = (0, 0)
tail = [(0, 0) for _ in range(9)]

MOVE = {
    "U": (0, -1),
    "L": (-1, 0),
    "R": (1, 0),
    "D": (0, 1),
}

def print_grid(vis):
    for y in range(-25, 15, 1):
        for x in range(-20, 25, 1):
            if vis.get((x, y)) is not None:
                print("#", end="")
            else:
                print(".", end="")
        print()

def trail(head, tail):
    dx = abs(head[0] - tail[0])
    dy = abs(head[1] - tail[1])
    if not (dx <= 2 and dy <= 2):
        assert False
    if dx == 2 and dy == 2:
        if head[0] > tail[0] and head[1] > tail[1]:
            tail = (head[0] - 1, head[1] - 1)
        elif head[0] > tail[0] and head[1] < tail[1]:
            tail = (head[0] - 1, head[1] + 1)
        elif head[0] < tail[0] and head[1] > tail[1]:
            tail = (head[0] + 1, head[1] - 1)
        else:
            tail = (head[0] + 1, head[1] + 1)
        # tail = (tail[0] - ((head[0] - tail[0]) // 2), tail[1] - ((head[1] - tail[1]) // 2))
        return tail

    if head[0] - tail[0] > 1:
        tail = (head[0] - 1, head[1])
    if tail[0] - head[0] > 1:
        tail = (head[0] + 1, head[1])
    if head[1] - tail[1] > 1:
        tail = (head[0], head[1] - 1)
    if tail[1] - head[1] > 1:
        tail = (head[0], head[1] + 1)

    return tail

visited = {
    (0, 0): True
}

for line in lines:
    for i in range(line[1]):
        head = (head[0] + MOVE[line[0]][0], head[1] + MOVE[line[0]][1])
        tail[0] = trail(head, tail[0])
        for j in range(len(tail)-1):
            tail[j + 1] = trail(tail[j], tail[j + 1])

            visited[tail[-1]] = True

print(len(visited))








