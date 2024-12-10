from collections import deque

input = open("input.txt").read().strip()

def parse_grid(input: str) -> dict[tuple[int, int], int]:
    grid = {}

    for r, row in enumerate([x.strip() for x in input.splitlines()]):
        for c, ch in enumerate(row):
            grid[(r, c)] = int(ch)

    return grid

def find_trailheads(grid: dict[tuple[int, int], int], p2: bool) -> int:
    total = 0
    queue = deque()

    for k, v in grid.items():
        if v == 0:
            queue.append((k, set()))

    while queue:
        curr, seen = queue.popleft()
        r, c = curr

        if curr in seen:
            continue

        seen.add(curr)

        if grid[curr] == 9:
            total += 1
            continue

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rr = r + dr
            cc = c + dc

            if (rr, cc) not in grid:
                continue

            if grid[(rr, cc)] == grid[curr] + 1:
                if p2:
                    queue.append(((rr, cc), set(seen)))
                else:
                    queue.append(((rr, cc), seen))

    return total

def part1(input: str) -> int:
    grid = parse_grid(input)
    trailheads = find_trailheads(grid, False)
    return trailheads

def part2(input: str) -> int:
    grid = parse_grid(input)
    trailheads = find_trailheads(grid, True)
    return trailheads

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















