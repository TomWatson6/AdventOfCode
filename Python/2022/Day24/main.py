from collections import defaultdict, deque
from copy import deepcopy

with open("input.txt") as f:
    input = [list(x.strip()) for x in f.readlines()]

D = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1),
}

grid = set()
start = (0, 0)
end = (0, 0)
W = defaultdict(lambda: [])
WS = []
R = len(input) - 1
C = len(input[0]) - 1

for r, row in enumerate(input):
    for c, val in enumerate(row):
        if r == 0 and val == '.':
            start = (r, c)
        if r == len(input) - 1 and val == '.':
            end = (r, c)
        if val == '#':
            grid.add((r, c))
        elif val in ['^', 'v', '<', '>']:
            W[(r, c)].append(val)

WS.append(W)

def evolve(winds):
    W_ = defaultdict(lambda: [])
    for k, v in winds.items():
        while v:
            w = v.pop()

            r = k[0] + D[w][0]
            r = 1 if r >= R else r
            r = R - 1 if r < 1 else r

            c = k[1] + D[w][1]
            c = 1 if c >= C else c
            c = C - 1 if c < 1 else c

            pos = (r, c)
            W_[pos].append(w)

    return W_

for i in range(R * C):
    WS.append(deepcopy(evolve(WS[i])))

for x in range(10):
    print(WS[x])

def print_grid():
    for r in range(R + 1):
        for c in range(C + 1):
            if (r, c) in W:
                if len(W[(r, c)]) > 1:
                    print(len(W[(r, c)]), end="")
                else:
                    print(W[(r, c)][0], end="")
            else:
                if (r, c) in grid:
                    print("#", end="")
                else:
                    print(".", end="")
        print()
    print()

def reconstruct_path(r, c, d, CF):
    path = [(r, c)]

    while (r, c) != start:
        r, c, d = CF[(r, c, d)]
        path.append((r, c))

    return path[::-1]

def search(start, end, starting_depth):
    moves = 0
    Q = deque()
    Q.append((start, starting_depth))
    S = set()
    # print(start, end)
    CF = {}

    while Q:
        (r, c), d = Q.popleft()

        if (r, c, d) in S:
            continue
        S.add((r, c, d))

        if d + 1 > moves:
            moves = d + 1
            # print(moves, r, c)

        if (r, c) == end:
            # print(reconstruct_path(r, c, d, CF))
            return d - starting_depth

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]:
            rr = r + dr
            cc = c + dc

            if 0 <= rr <= R and 0 <= cc <= C and (rr, cc) not in grid and len(WS[d + 1][(rr, cc)]) == 0: 
                Q.append(((rr, cc), d + 1))
                CF[(rr, cc, d + 1)] = (r, c, d)

total = 0
d = search(start, end, total)
print(d)
total += d
d = search(end, start, total)
print(d)
total += d
d = search(start, end, total)
print(d)
total += d
print("Part 2:", total)



# for _ in range(30):
#     print_grid()
#     W = evolve(W)










