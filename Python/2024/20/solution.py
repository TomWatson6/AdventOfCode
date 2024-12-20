from collections import deque

input = open("input.txt").read().strip()

def parse_input(input):
    lines = input.splitlines()
    grid = {}
    start = (0, 0)
    dest = (0, 0)

    for r in range(len(lines)):
        for c in range(len(lines[0])):
            grid[(r, c)] = lines[r][c]
            if lines[r][c] == 'S':
                start = (r, c)
            if lines[r][c] == 'E':
                dest = (r, c)

    return grid, start, dest

D = {}

def find(grid, start, dest):
    queue = deque([(start, 0)])
    seen = set()

    while queue:
        (r, c), depth = queue.popleft()

        if (r, c) in seen:
            continue

        seen.add((r, c))

        if (r, c) not in D:
            D[(r, c)] = depth

        if (r, c) == dest:
            return depth

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rr = r + dr
            cc = c + dc

            if (rr, cc) in grid and grid[(rr, cc)] in ['.', 'E']:
                queue.append(((rr, cc), depth + 1))

    return 0

def find_with_cheating(grid, start, dest, to_beat, cheat_low, cheat_high):
    queue = deque([(start, 0)]) # Loc, Depth
    seen = set()
    outcomes = []

    while queue:
        (r, c), depth = queue.popleft()

        if (r, c) in seen:
            continue

        seen.add((r, c))

        if (r, c) == dest and depth < to_beat:
            outcomes.append(to_beat - depth)
            continue

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rr = r + dr
            cc = c + dc

            if (rr, cc) not in grid or grid[(rr, cc)] == '#':
                continue

            queue.append(((rr, cc), depth + 1))

        goals = [d for d in D.items() if cheat_low <= man_dist((r, c), d[0]) <= cheat_high and d[0] not in seen]
        if len(goals) > 0:
            for goal, leftover in goals:
                dist = man_dist((r, c), goal)
                total = depth + dist + leftover
                if total < to_beat:
                    outcomes.append(to_beat - total)

    return outcomes

def man_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def invert_distances(to_beat):
    for k, v in D.items():
        D[k] = to_beat - v

def part1(input: str) -> int:
    grid, start, dest = parse_input(input)
    to_beat = find(grid, start, dest)
    invert_distances(to_beat)
    outcomes = find_with_cheating(grid, start, dest, to_beat, 0, 2)

    return len([o for o in outcomes if o >= 100])

def part2(input: str) -> int:
    grid, start, dest = parse_input(input)
    to_beat = find(grid, start, dest)
    outcomes = find_with_cheating(grid, start, dest, to_beat, 0, 20)

    return len([o for o in outcomes if o >= 100])

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















