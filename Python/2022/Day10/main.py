
with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

X = 1
T = 0

S = []

G = [['.' for _ in range(40)] for _ in range(6)]

def get_grid():
    output = ""

    for r in G:
        for c in r:
            output += c
        output += "\n"

    return output

def attempt_draw():
    t = T % 40
    row = T // 40
    if t in [X - 1, X, X + 1]:
        G[row][t] = '#'

def check_signals():
    if T in [20, 60, 100, 140, 180, 220]:
        S.append(X * T)

for line in lines:
    parts = line.split(" ")
    attempt_draw()
    if len(parts) > 1:
        op, val = parts[0], int(parts[1])
        T += 1
        check_signals()
        attempt_draw()
        T += 1
        check_signals()
        X += val
        continue
    T += 1
    check_signals()
    
print(f"Part 1: {sum(S)}")
print(f"Part 2:\n{get_grid()}")


























