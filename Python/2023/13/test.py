
with open(0) as f:
    grids = [[list(t) for t in x.strip().split("\n")] for x in f.read().split("\n\n")]

def reflections(grid):
    horiz = []
    vert = []

    for r in range(1, len(grid) - 1):
        top = tuple([tuple(grid[x][c] for x in range(r, -1, -1)) for c in range(len(grid[r]))])
        bottom = tuple([tuple(grid[x][c] for x in range(r + 1, 2 * r + 1)) for c in range(len(grid[r]))])




















