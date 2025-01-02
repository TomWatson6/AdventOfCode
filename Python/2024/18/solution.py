from collections import deque

input = open("input.txt").read().strip()

def parse_input(input, dim, num_bytes):
    lines = input.splitlines()
    nums = [(int(x), int(y)) for x, y in [t.split(",") for t in lines]][:num_bytes]
    grid = {}

    for y in range(dim + 1):
        for x in range(dim + 1):
            if (x, y) in nums:
                grid[(x, y)] = '#'
            else:
                grid[(x, y)] = '.'

    return grid

def find(grid, start, dest, dim):
    queue = deque([(start, 0)])
    seen = set()

    while queue:
        curr, depth = queue.popleft()
        x, y = curr

        if curr in seen:
            continue

        seen.add(curr)

        if curr == dest:
            return depth

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            xx = x + dx
            yy = y + dy

            if (xx, yy) in grid and grid[(xx, yy)] != '#':
                queue.append(((xx, yy), depth + 1))

    return 0

def print_grid(grid, dim):
    for y in range(dim + 1):
        for x in range(dim + 1):
            print(grid[(x, y)], end='')
        print()

def part1(input: str, dim: int, num_bytes: int) -> int:
    grid = parse_input(input, dim, num_bytes)
    dist = find(grid, (0, 0), (dim, dim), dim)
    return dist

def part2(input: str, dim: int) -> int:
    i = 0
    lines = input.splitlines()
    low = 0
    high = len(lines)
    mid = 0

    # while i < len(lines):
    while low < high:
        mid = (low + high) // 2
        if abs(high - low) <= 1:
            return lines[low]
        grid = parse_input(input, dim, mid)
        dist = find(grid, (0, 0), (dim, dim), dim)

        if dist == 0:
            high = mid
        else:
            low = mid

        # if dist == 0:
        #     return lines[i - 1]

        # i += 1

    return lines[mid]

if __name__ == "__main__":
    print("Part 1:", part1(input, 70, 1024))
    print("Part 2:", part2(input, 70))















