from collections import defaultdict, deque

input = open("input.txt").read()

def pretty_print(grid):
    r_low = min(r for r, c in grid.keys())
    r_high = max(r for r, c in grid.keys())
    c_low = min(c for r, c in grid.keys())
    c_high = max(c for r, c in grid.keys())

    for r in range(r_low, r_high + 1):
        row = ""

        for c in range(c_low, c_high + 1):
            if (r, c) in grid:
                row += grid[(r, c)]
            else:
                row += ' '

        print(row)

    print()

R = 0
C = 0

def parse(input: str):
    global R, C
    grid = {}

    for r, row in enumerate(input.splitlines()):
        for c, ch in enumerate(row):
            grid[(r, c)] = ch
            R = r
            C = c

    return grid

def find_portals(grid):
    portals = defaultdict(lambda: set())

    for (r, c), v in grid.items():
        if v not in '#. ':
            letters = [(r, c)]
            # Find other char
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                rr = r + dr
                cc = c + dc
                if (rr, cc) in grid and grid[(rr, cc)] not in '#. ':
                    letters.append((rr, cc))
                    break

            surrounding = []

            for a in range(min(r for r, c in letters) - 1, max(r for r, c in letters) + 2):
                for b in range(min(c for r, c in letters) - 1, max(c for r, c in letters) + 2):
                    surrounding.append((a, b))

            loc = [(a, b) for a, b in surrounding if (a, b) in grid and grid[(a, b)] == '.'][0]
            letters = sorted(letters)

            portals["".join(grid[(a, b)] for a, b in letters)].add(loc)

    assert all(len(p) == 2 for p in portals)

    return portals

def convert_portals(portals):
    converted = {}

    for a, b in [p for p in portals.values() if len(p) == 2]:
        converted[a] = b
        converted[b] = a

    return converted

def bfs(grid, portals, start, dest):
    queue = deque([(start, 0)])
    seen = set()

    while queue:
        (r, c), d = queue.popleft()

        if (r, c) == dest:
            return d

        if (r, c) in seen:
            continue

        seen.add((r, c))

        if (r, c) in portals:
            queue.append((portals[(r, c)], d + 1))

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rr = r + dr
            cc = c + dc

            if (rr, cc) in grid and grid[(rr, cc)] == '.':
                queue.append(((rr, cc), d + 1))

    return 0

def bfs2(grid, portals, start, dest):
    queue = deque([(start, 0, 0)])
    seen = set()

    while queue:
        (r, c), d, l = queue.popleft()

        if (r, c) == dest and l == 0:
            return d

        if (r, c, l) in seen:
            continue

        seen.add((r, c, l))

        if (r, c) in portals:
            # If outer portal
            if r == 2 or r == R - 2 or c == 2 or c == C - 2:
                if l > 0:
                    queue.append((portals[(r, c)], d + 1, l - 1))
            else:
                queue.append((portals[(r, c)], d + 1, l + 1))


        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rr = r + dr
            cc = c + dc

            if (rr, cc) in grid and grid[(rr, cc)] == '.':
                queue.append(((rr, cc), d + 1, l))

    return 0

def part1(input: str) -> int:
    grid = parse(input)

    portals = find_portals(grid)
    start = list(portals["AA"])[0]
    dest = list(portals["ZZ"])[0]

    portals = convert_portals(portals)

    return bfs(grid, portals, start, dest)

def part2(input: str) -> int:
    grid = parse(input)

    portals = find_portals(grid)
    start = list(portals["AA"])[0]
    dest = list(portals["ZZ"])[0]

    portals = convert_portals(portals)

    return bfs2(grid, portals, start, dest)

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















