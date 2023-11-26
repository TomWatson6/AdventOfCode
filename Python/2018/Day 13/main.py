
LEFT = {
    '^': '<',
    '<': 'v',
    'v': '>',
    '>': '^',
}

RIGHT = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^',
}

NEXT = {
    '^': lambda r, c: (r - 1, c),
    '>': lambda r, c: (r, c + 1),
    'v': lambda r, c: (r + 1, c),
    '<': lambda r, c: (r, c - 1),
}

# /
# v => right
# ^ => right
# < => left
# > => left

# \
# v => left
# ^ => left
# < => right
# > => right

TURN = {
    0: lambda x: LEFT[x],
    1: lambda x: x,
    2: lambda x: RIGHT[x],
}

with open("input.txt") as f:
    grid = [list(x.strip("\n")) for x in f.readlines()]

carts = []

for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val in ['^', 'v', '<', '>']:
            carts.append(((r, c), val, 0))
            grid[r][c] = '-' if val in ['<', '>'] else '|'

def print_grid(grid, carts):
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            cart = [x[1] for x in carts if x[0] == (r, c)]
            if len(cart) == 1:
                print(cart[0], end="")
                continue

            print(val, end="")
        print()
    print()

collision = (0, 0)
p1 = False

while True:
    carts = sorted(carts, key=lambda x: (x[0], x[1]))
    loc_collisions = []

    for i in range(len(carts)):
        if carts[i][0] in loc_collisions:
            continue

        n = NEXT[carts[i][1]](carts[i][0][0], carts[i][0][1])

        carts[i] = (n, carts[i][1], carts[i][2])
        val = grid[carts[i][0][0]][carts[i][0][1]]

        if carts[i][0] in [x[0] for x in [t for t in carts if t != carts[i]]]:
            collision = (carts[i][0][1], carts[i][0][0])
            if not p1:
                print(f"Part 1: {collision[0]},{collision[1]}")
                p1 = True

            loc_collisions.append(carts[i][0])
            continue

        if val == '\\':
            if carts[i][1] in ['<', '>']:
                carts[i] = (carts[i][0], RIGHT[carts[i][1]], carts[i][2])
            else:
                carts[i] = (carts[i][0], LEFT[carts[i][1]], carts[i][2])

        elif val == '/':
            if carts[i][1] in ['<', '>']:
                carts[i] = (carts[i][0], LEFT[carts[i][1]], carts[i][2])
            else:
                carts[i] = (carts[i][0], RIGHT[carts[i][1]], carts[i][2])

        elif val == '+':
            carts[i] = (carts[i][0], TURN[carts[i][2] % 3](carts[i][1]), carts[i][2] + 1)

    if len(loc_collisions) > 0:
        for loc in loc_collisions:
            carts = [x for x in carts if x[0] != loc]

            if len(carts) == 1:
                print(f"Part 2: {carts[0][0][1]},{carts[0][0][0]}")
                exit(0)



























