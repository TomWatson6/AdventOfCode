
with open(0) as f:
    grid = [list(x.strip()) for x in f.readlines()]

cached = grid[:]
R = len(grid)
C = len(grid[0])
SEEN = {}
assert R == C

def score(grid):
    score = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'O':
                score += len(grid) - r

    return score

def print_grid(grid):
    for r in range(R):
        out = ""
        for c in range(C):
            out += grid[r][c]
        print(out)

    print()

def tilt(grid):
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '#' or grid[r][c] == 'O':
                continue
            t = r

            while t < R:
                if grid[t][c] in ['O', '#']:
                    if grid[t][c] == '#':
                        break

                    grid[r][c] = 'O'
                    grid[t][c] = '.'
                    break

                t += 1

def rotate(grid):
    new_grid = []
    for c in range(C):
        new_grid.append([grid[r][c] for r in range(R - 1, -1, -1)])

    return new_grid


def cycle(grid):
    for _ in range(4):
        tilt(grid)
        grid = rotate(grid)

    return grid

tilt(grid)
print("Part 1:", score(grid))

grid = cached[:]

ITERS = 1000000000
cycled = False
i = 0

while i < ITERS:
    grid = cycle(grid)
    t = tuple(["".join(c) for c in grid])

    if t in SEEN and not cycled:
        cycle_length = i - SEEN[t]
        rem_cycles = ITERS - i - 1
        num_cycles = rem_cycles // cycle_length
        i += num_cycles * cycle_length
        cycled = True

    SEEN[t] = i
    i += 1

print("Part 2:", score(grid))





















