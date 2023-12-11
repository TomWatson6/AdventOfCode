
with open(0) as f:
    grid = [x.strip() for x in f.readlines()]

R = len(grid)
C = len(grid[0])

empty_rows = []
empty_cols = []

for i, r in enumerate(grid):
    if all(c == '.' for c in r):
        empty_rows.append(i)

cols = []

for i in range(len(grid[0])):
    col = []
    for j in range(len(grid)):
        col.append(grid[j][i])
    cols.append(col)

empty_cols = [i for i, c in enumerate(cols) if all(a == '.' for a in c)]

galaxies = []

for i, row in enumerate(grid):
    for j, ch in enumerate(row):
        if ch == '#':
            galaxies.append((i, j))

def solve(p2):
    distances = 0
    age = 1000000 if p2 else 2

    # To work with test input
    if p2 and len(grid) < 20:
        age = 10

    for i in range(len(galaxies) - 1):
        for j in range(i, len(galaxies)):
            a = galaxies[i]
            b = galaxies[j]

            dr = len([t for t in empty_rows if a[0] < t < b[0] or b[0] < t < a[0]])
            dc = len([t for t in empty_cols if a[1] < t < b[1] or b[1] < t < a[1]])

            distances += abs(a[0] - b[0]) + (dr * (age - 1)) + abs(a[1] - b[1]) + (dc * (age - 1))

    return distances

print("Part 1:", solve(False))
print("Part 2:", solve(True))

















