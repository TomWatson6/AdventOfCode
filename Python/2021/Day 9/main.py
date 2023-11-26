

def get_pits(grid):
    collection = []
    pits = []

    ## Locate the centre of the pits
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if y == len(grid) - 1 or int(grid[y][x]) < int(grid[y + 1][x]):
                if y == 0 or int(grid[y][x]) < int(grid[y - 1][x]):
                    if x == len(grid[0]) - 1 or int(grid[y][x]) < int(grid[y][x + 1]):
                        if x == 0 or int(grid[y][x]) < int(grid[y][x - 1]):
                            collection.append([y, x])

    ## For each pit, find surrounding parts that need to be checked, and at them to a finitely expanding list.
    ## The expansion will stop once the pits edges have been found (9 has been found around the edges)
    for c in collection:
        to_check = [c]
        curr = 0

        while curr != len(to_check):
            r, c = to_check[curr]
            if r != len(grid) - 1:
                if int(grid[r][c]) < int(grid[r + 1][c]):
                    if int(grid[r + 1][c]) != 9:
                        to_check.append([r + 1, c])
            if r != 0:
                if int(grid[r][c]) < int(grid[r - 1][c]):
                    if int(grid[r - 1][c]) != 9:
                        to_check.append([r - 1, c])
            if c != len(grid[0]) - 1:
                if int(grid[r][c]) < int(grid[r][c + 1]):
                    if int(grid[r][c + 1]) != 9:
                        to_check.append([r, c + 1])
            if c != 0:
                if int(grid[r][c]) < int(grid[r][c - 1]):
                    if int(grid[r][c - 1]) != 9:
                        to_check.append([r, c - 1])
            curr += 1
        stripped_check = []
        [stripped_check.append(x) for x in to_check if x not in stripped_check]
        pits.append(len(stripped_check))

    return pits

def p1(output):
    print("Part 1:", output)

def p2(output):
    print("Part 2:", output)

with open("input.txt") as f:
    grid = [x.strip() for x in f.readlines()]

grid = [[y for y in x] for x in grid]

total = 0

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if y == len(grid) - 1 or int(grid[y][x]) < int(grid[y + 1][x]):
            if y == 0 or int(grid[y][x]) < int(grid[y - 1][x]):
                if x == len(grid[0]) - 1 or int(grid[y][x]) < int(grid[y][x + 1]):
                    if x == 0 or int(grid[y][x]) < int(grid[y][x - 1]):
                        total += 1 + int(grid[y][x])

p1(total)

pits = get_pits(grid)

pits.sort()

largest = 1

for x in pits[-3:]:
    largest *= x

p2(largest)