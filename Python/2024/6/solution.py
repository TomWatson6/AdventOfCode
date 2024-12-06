from copy import deepcopy

input = open("input.txt").read().strip()

def parse_grid(input: str) -> tuple[dict[tuple[int, int], chr], tuple[int, int]]:
    lines = input.splitlines()
    grid = {}
    guard = (0, 0)

    for r, row in enumerate(lines):
        for c, ch in enumerate(row):
            grid[(r, c)] = ch
            if ch in ['^', 'v', '>', '<']:
                guard = (r, c)

    return grid, guard

dirs = [
    (-1, 0), # ^
    (0, 1),  # >
    (1, 0),  # v
    (0, -1), # <
]

def patrol(grid: dict[tuple[int, int], chr], pos: tuple[int, int])-> tuple[set[tuple[int, int]], bool]:
    dir = (0, 0)
    curr = 0
    visited = set()

    match grid[pos]:
        case '^':
            dir = dirs[0]
        case '>':
            dir = dirs[1]
            curr = 1
        case 'v':
            dir = dirs[2]
            curr = 2
        case '<':
            dir = dirs[3]
            curr = 3

    while pos in grid:
        if (pos, dir) in visited:
            return set(), True
        visited.add((pos, dir))
        new_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if new_pos not in grid:
            break
        if grid[new_pos] == '#':
            curr += 1
            dir = dirs[curr % len(dirs)]
            new_pos = pos
        pos = new_pos

    return set(v for v, d in visited), False

def part1(input: str) -> int:
    grid, guard = parse_grid(input)
    visited, _ = patrol(grid, guard)

    return len(visited)

def part2(input: str) -> int:
    grid, guard = parse_grid(input)
    loops = 0

    visited, _ = patrol(grid, guard)

    for v in visited:
        if v == guard:
            continue
        new_grid = deepcopy(grid)
        new_grid[v] = '#'
        _, looping = patrol(new_grid, guard)
        if looping:
            loops += 1

    return loops

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















