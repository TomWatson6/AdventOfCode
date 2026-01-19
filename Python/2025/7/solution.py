from collections import deque, defaultdict

input = open("input.txt").read().strip()

R = 0
C = 0
start = (0, 0)

def parse(input: str):
    global R, C, start

    grid = [list(x) for x in input.splitlines()]
    start = (0, 0)

    for r in range(len(grid)):
        R = r

        for c in range(len(grid[0])):
            C = c

            if grid[r][c] == 'S':
                start = (r, c)

    return grid

def emit(grid):
    r, c = start
    queue = deque([(r, c)])
    seen = set()
    positions = set()

    while queue:
        r, c = queue.popleft()

        if r == R:
            continue

        if (r, c) in seen:
            continue

        seen.add((r, c))

        if grid[r][c] == '^':
            positions.add((r, c))

            if c > 0:
                queue.append((r, c - 1))
            if c < C - 1:
                queue.append((r, c + 1))

            continue

        queue.append((r + 1, c))

    return len(positions)

DP = {}

def emit2(grid, curr):
    if curr in DP:
        return DP[curr]

    r, c = curr

    if c < 0 or c > C:
        return 0

    while grid[r][c] != '^' and r < R:
        r += 1

    if r == R:
        return 1

    left = emit2(grid, (r, c - 1))
    DP[(r, c - 1)] = left

    right = emit2(grid, (r, c + 1))
    DP[(r, c + 1)] = right

    return left + right

def part1(input: str) -> int:
    grid = parse(input)

    total = emit(grid)

    return total

def part2(input: str) -> int:
    grid = parse(input)

    total = emit2(grid, start)

    return total

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















