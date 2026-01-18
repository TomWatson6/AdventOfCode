from copy import deepcopy

input = open("input.txt").read().strip()

W = 50
H = 6


def parse(input: str):
    return input.splitlines()

def pretty_print(grid):
    r_low = min(grid.keys(), key = lambda k: k[0])[0]
    r_high = max(grid.keys(), key = lambda k: k[0])[0]
    c_low = min(grid.keys(), key = lambda k: k[1])[1]
    c_high = max(grid.keys(), key = lambda k: k[1])[1]

    for r in range(r_low, r_high + 1):
        row = ""
        for c in range(c_low, c_high + 1):
            row += grid[(r, c)]
        print(row)
    print()

grid = {(r, c): ' ' for r in range(H) for c in range(W)}

def part1(input: str) -> int:
    global grid
    lines = parse(input)

    for line in lines:
        if line.startswith("rect"):
            width, height = list(map(int, line.split()[1].split('x')))

            for r in range(height):
                for c in range(width):
                    grid[(r, c)] = '#'
        else:
            new_grid = deepcopy(grid)
            left, right = line.split('=')
            val, amt = list(map(int, right.split(" by ")))

            if left[-1] == 'x':
                for i in range(H):
                    new_grid[((i + amt) % H, val)] = grid[(i, val)]
            else:
                for i in range(W):
                    new_grid[(val, (i + amt) % W)] = grid[(val, i)]

            grid = new_grid

    return sum(v == '#' for v in grid.values())

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:")
    pretty_print(grid)















