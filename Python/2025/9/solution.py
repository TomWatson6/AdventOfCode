from collections import deque

input = open("input.txt").read().strip()

def parse(input: str):
    return [list(map(int, num.split(","))) for num in input.splitlines()]

def rect_area(a, b):
    width = abs(a[1] - b[1]) + 1
    height = abs(a[0] - b[0]) + 1

    return width * height

def part1(input: str) -> int:
    coords = parse(input)
    largest = 0

    for i in range(len(coords) - 1):
        for j in range(i + 1, len(coords)):
            largest = max(largest, rect_area(coords[i], coords[j]))

    return largest

grid = []
psa = []
xs = []
ys = []

def valid(x1, y1, x2, y2):
    cx1, cx2 = sorted([xs.index(x1) * 2, xs.index(x2) * 2])
    cy1, cy2 = sorted([ys.index(y1) * 2, ys.index(y2) * 2])

    left = psa[cx1 - 1][cy2] if cx1 > 0 else 0
    top = psa[cx2][cy1 - 1] if cy1 > 0 else 0
    topleft = psa[cx1 - 1][cy1 - 1] if cx1 > 0 < cy1 else 0

    count = psa[cx2][cy2] - left - top + topleft

    return count == (cx2 - cx1 + 1) * (cy2 - cy1 + 1)

def part2(input: str) -> int:
    global grid, psa, xs, ys
    points = parse(input)

    xs = sorted({x for x, y in points})
    ys = sorted({y for x, y in points})

    grid = [[0] * (len(ys) * 2 - 1) for _ in range(len(xs) * 2 - 1)]

    for (x1, y1), (x2, y2) in zip(points, points[1:] + points[:1]):
        cx1, cx2 = sorted([xs.index(x1) * 2, xs.index(x2) * 2])
        cy1, cy2 = sorted([ys.index(y1) * 2, ys.index(y2) * 2])

        for cx in range(cx1, cx2 + 1):
            for cy in range(cy1, cy2 + 1):
                grid[cx][cy] = 1

    outside = {(-1, -1)}
    queue = deque(outside)

    while queue:
        x, y = queue.popleft()

        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if nx < -1 or nx > len(grid) or ny < -1 or ny > len(grid[0]):
                continue

            if 0 <= nx < len(grid) and 0 <= ny < len(grid) and grid[nx][ny] == 1:
                continue

            if (nx, ny) in outside:
                continue

            outside.add((nx, ny))
            queue.append((nx, ny))

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (x, y) not in outside:
                grid[x][y] = 1

    psa = [[0] * len(row) for row in grid]

    for x in range(len(psa)):
        for y in range(len(psa[0])):
            left = psa[x - 1][y] if x > 0 else 0
            top = psa[x][y - 1] if y > 0 else 0
            topleft = psa[x - 1][y - 1] if x > 0 < y else 0
            psa[x][y] = left + top - topleft + grid[x][y]

    return max([(abs(x1 - x2) + 1) * (abs(y1 - y2) + 1) for i, (x1, y1) in enumerate(points) for x2, y2 in points[:i] if valid(x1, y1, x2, y2)])

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















