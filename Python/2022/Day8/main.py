

def print_grid(V, lines):
    R = max(V, key=lambda k: k[0])[0]
    C = max(V, key=lambda k: k[1])[1]

    for r in range(R + 1):
        for c in range(C + 1):
            if (r, c) in V:
                print(lines[r][c], end="")
            else:
                print(".", end="")
        print()
    print()

with open("simple_input.txt") as f:
    lines = [list(x.strip()) for x in f.readlines()]

lines = [[int(x) for x in line] for line in lines]

V = set()

left = set()
right = set()

for i, line in enumerate(lines):
    l = []
    for j, tree in enumerate(line):
        if len(l) == 0:
            l.append((i, j))
            continue
        r, c = l[-1]
        if lines[r][c] <= tree:
            l.append((i, j))

    r_ = []
    for j, tree in enumerate(line[::-1]):
        if len(r_) == 0:
            r_.append((i, j))
            continue
        r, c = r_[-1]
        if lines[r][c] <= tree:
            r_.append((i, j))

    for a in l:
        left.add(a)

    for a in r_:
        right.add(a)

top = set()
bottom = set()

for i in range(len(lines[0])):
    t = []
    for j in range(len(lines)):
        if len(t) == 0:
            t.append((i, j))
            continue
        r, c = t[-1]
        if lines[r][c] <= lines[i][j]:
            t.append((i, j))

    for a in t:
        top.add(a)

for i in range(len(lines[0]) - 1, -1, -1):
    b = []
    for j in range(len(lines)):
        if len(b) == 0:
            b.append((i, j))
            continue
        r, c = t[-1]
        if lines[r][c] <= lines[i][j]:
            b.append((i, j))

    for a in b:
        bottom.add(a)

V = left.union(right).union(top).union(bottom)

print(len(left), len(right), len(top), len(bottom), sum([len(left), len(right), len(top), len(bottom)]))
print(len(V))

print()
print_grid(V, lines)
















