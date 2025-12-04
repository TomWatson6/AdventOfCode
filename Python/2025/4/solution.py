
input = open("input.txt").read().strip()

def parse(input: str):
    grid = input.splitlines()
    grid = [[char for char in s] for s in grid]

    return grid

def get_adjacents(grid, coord):
    adj = []
    r, c = coord

    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == dc == 0:
                continue

            rr = r + dr
            cc = c + dc

            if 0 <= rr < len(grid) and 0 <= cc < len(grid[0]):
                adj.append((rr, cc))

    return adj

def part1(input: str) -> int:
    grid = parse(input)
    total = 0

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col != '@':
                continue

            adj = get_adjacents(grid, (r, c))
            if sum(grid[r][c] == '@' for (r, c) in adj) < 4:
                total += 1

    return total

def part2(input: str) -> int:
    grid = parse(input)
    total = 0
    r = 0
    c = 0

    while r < len(grid):
        if grid[r][c] == '@':
            adj = get_adjacents(grid, (r, c))
            if sum(grid[r][c] == '@' for (r, c) in adj) < 4:
                total += 1
                grid[r][c] = '.'
                r = 0
                c = 0
                continue

        if c == len(grid[0]) - 1:
            c = 0
            r += 1
        else:
            c += 1

    return total

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















