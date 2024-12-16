from collections import deque

input = open("input.txt").read().strip()

def parse_grid(input):
    lines = input.splitlines()
    R = len(lines)
    C = len(lines[0])
    start = (0, 0)
    dest = (0, 0)

    for r in range(R):
        for c in range(C):
            if lines[r][c] == 'S':
                start = (r, c)
            if lines[r][c] == 'E':
                dest = (r, c)

    return lines, start, dest

def find(start, dest, grid, p2):
    queue = deque([(start, (0, 1), 0, 0, set([start]))])
    seen = set()
    found_at = {}
    paths = set()
    best = None

    while queue:
        curr, dir, steps, rem_time, path = queue.popleft()
        r, c = curr
        rem_time -= 1

        if rem_time > 0:
            queue.append((curr, dir, steps + 1, rem_time, path))
            continue

        if (curr, dir) in seen:
            if not p2:
                continue
            if (curr, dir) in found_at and found_at[(curr, dir)] != steps:
                continue

        seen.add((curr, dir))
        found_at[(curr, dir)] = steps

        if curr == dest:
            if best is None:
                best = steps
            if steps == best:
                paths |= path
            if steps > best:
                return best, paths

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rr = r + dr
            cc = c + dc

            if 0 <= rr < len(grid) and 0 <= cc < len(grid[0]) and grid[rr][cc] in ['.', 'E']:
                if (dr, dc) == dir:
                    queue.append(((rr, cc), dir, steps + 1, 1, path | set([(rr, cc)])))
                else:
                    queue.append(((r, c), (dr, dc), steps + 1, 1000, path))

    return 0, set()

def part1(input: str) -> int:
    grid, start, dest = parse_grid(input)

    steps, _ = find(start, dest, grid, False)

    return steps

def part2(input: str) -> int:
    grid, start, dest = parse_grid(input)

    _, paths = find(start, dest, grid, True)

    return len(paths)

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















