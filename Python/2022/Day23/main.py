from collections import defaultdict

with open("input.txt") as f:
    input = [list(x.strip()) for x in f.readlines()]

grid = set()

for r, row in enumerate(input):
    for c, val in enumerate(row):
        if val == '#':
            grid.add((r, c))

def get_adjacents(coord):
    adj = []

    r, c = coord

    for rr in range(-1, 2):
        for cc in range(-1, 2):
            if rr == 0 and cc == 0:
                continue
            adj.append((r + rr, c + cc))

    return adj

funcs = {
    0: lambda k, adj: all([x not in grid for x in adj if x[0] < k[0]]),
    1: lambda k, adj: all([x not in grid for x in adj if x[0] > k[0]]),
    2: lambda k, adj: all([x not in grid for x in adj if x[1] < k[1]]),
    3: lambda k, adj: all([x not in grid for x in adj if x[1] > k[1]]),
}

outcomes = {
    0: lambda k: (k[0] - 1, k[1]),
    1: lambda k: (k[0] + 1, k[1]),
    2: lambda k: (k[0], k[1] - 1),
    3: lambda k: (k[0], k[1] + 1),
}

func_pointer = 0

def evolve():
    global func_pointer
    M = defaultdict(lambda: [])
    for k in grid:
        adj = get_adjacents(k)
        if any([x in grid for x in adj]):
            index = lambda i: (func_pointer + i) % len(funcs)

            if funcs[index(0)](k, adj):
                M[outcomes[index(0)](k)].append(k)
            elif funcs[index(1)](k, adj):
                M[outcomes[index(1)](k)].append(k)
            elif funcs[index(2)](k, adj):
                M[outcomes[index(2)](k)].append(k)
            elif funcs[index(3)](k, adj):
                M[outcomes[index(3)](k)].append(k)

    new_grid = set()

    for k, v in M.items():
        if len(v) > 1:
            continue

        new_grid.add(k)
        grid.remove(v[0])

    new_grid = new_grid.union(grid)

    func_pointer += 1
    
    return new_grid, len(M) == 0

def count_empty():
    count = 0

    YM = min([x[0] for x in grid])
    XM = min([x[1] for x in grid])
    YS = max([x[0] for x in grid])
    XS = max([x[1] for x in grid])

    for r in range(YM, YS + 1):
        for c in range(XM, XS + 1):
            if (r, c) in grid:
                count += 1

    return (YS - YM + 1) * (XS - XM + 1) - count

def print_grid():
    YM = min([x[0] for x in grid])
    XM = min([x[1] for x in grid])
    YS = max([x[0] for x in grid])
    XS = max([x[1] for x in grid])

    for r in range(YM, YS + 1):
        for c in range(XM, XS + 1):
            if (r, c) in grid:
                print('#', end="")
            else:
                print("X", end="")
        print()

    print()

same = False
i = 0

while not same:
    grid, same = evolve()
    if same:
        print("Part 2:", i + 1)
        break
    if i == 9:
        print("Part 1:", count_empty())
    i += 1








