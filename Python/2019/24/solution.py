from collections import defaultdict

input = open("input.txt").read().strip()

def evolve(grid):
    new_grid = []

    for r in range(len(grid)):
        row = []

        for c in range(len(grid[0])):
            total = 0

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                rr = r + dr
                cc = c + dc

                if 0 <= rr < len(grid) and 0 <= cc < len(grid[0]) and grid[rr][cc] == '#':
                    total += 1

            if grid[r][c] == '.' and total in [1, 2]:
                row.append('#')
            elif grid[r][c] == '#' and total != 1:
                row.append('.')
            else:
                row.append(grid[r][c])

        new_grid.append(row)

    return new_grid

low = 0
high = 0

def evolve2(grids):
    global low, high
    checks = [i for i in range(low, high + 1)]
    new_checks = set()

    new_grids = defaultdict(lambda: [list('.' * 5) for _ in range(5)])
    check = 0

    while check < len(checks):
        i = checks[check]
        exclusions = set()

        if i in new_checks and i == max(new_checks):
            # Outer addition
            high = i
            exclusions = set([(r, c) for r in range(5) for c in range(5) if r == 0 or r == 4 or c == 0 or c == 4])

        if i in new_checks and i == min(new_checks):
            # Inner addition
            low = i
            exclusions = set([(r, c) for r in range(5) for c in range(5) if r != 0 and r != 4 and c != 0 and c != 4])

        for r in range(5):
            for c in range(5):
                if r == c == 2:
                    # ? in centre of grid
                    continue

                if (r, c) in exclusions:
                    continue

                adjacents = []

                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    rr = r + dr
                    cc = c + dc

                    if rr == cc == 2:
                        if i - 1 not in grids and i - 1 not in new_checks:
                            new_checks.add(i - 1)
                            checks.append(i - 1)

                        if (dr, dc) == (-1, 0):
                            adjacents += grids[i - 1][-1]
                        elif (dr, dc) == (1, 0):
                            adjacents += grids[i - 1][0]
                        elif (dr, dc) == (0, -1):
                            adjacents += list(zip(*grids[i - 1]))[-1]
                        else:
                            adjacents += list(zip(*grids[i - 1]))[0]

                    if rr >= len(grids[i]) or rr < 0 or cc >= len(grids[i][0]) or cc < 0:
                        if i + 1 not in grids and i + 1 not in new_checks:
                            new_checks.add(i + 1)
                            checks.append(i + 1)

                        if rr >= len(grids[i]):
                            # Bottom
                            adjacents.append(grids[i + 1][3][2])
                        elif rr < 0:
                            # Top
                            adjacents.append(grids[i + 1][1][2])
                        elif cc >= len(grids[i][0]):
                            # Right
                            adjacents.append(grids[i + 1][2][3])
                        else:
                            # Left
                            adjacents.append(grids[i + 1][2][1])

                    if 0 <= rr < len(grids[i]) and 0 <= cc < len(grids[i][0]) and not rr == cc == 2:
                        adjacents.append(grids[i][rr][cc])

                adj = len([a for a in adjacents if a == '#'])

                if grids[i][r][c] == '#' and adj != 1:
                    new_grids[i][r][c] = '.'
                elif grids[i][r][c] == '.'and adj in [1, 2]:
                    new_grids[i][r][c] = '#'
                else:
                    new_grids[i][r][c] = grids[i][r][c]

        check += 1

    return new_grids

def parse(input: str):
    return [list(x) for x in input.splitlines()]

def part1(input: str) -> int:
    grid = parse(input)

    states = set()
    states.add("".join("".join(c) for c in r) for r in grid)
    count = 0
    state = ""

    while True:
        count += 1
        grid = evolve(grid)
        state = "".join(["".join(c for c in r) for r in grid])
        if state in states:
            break

        states.add(state)

    total = 0

    for i, ch in enumerate(state):
        if ch == '#':
            total += 2 ** i

    return total

def part2(input: str) -> int:
    grid = parse(input)
    grids = defaultdict(lambda: [list('.' * 5) for _ in range(5)])
    grids[0] = grid

    for i in range(200):
        grids = evolve2(grids)

    total = 0

    for grid in grids.values():
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '#':
                    total += 1

    return total

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















