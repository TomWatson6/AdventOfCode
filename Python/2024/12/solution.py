from collections import defaultdict, deque

input = open("input.txt").read().strip()

def parse_input(input: str) -> dict[tuple[int, int], chr]:
    grid = {}

    for r, row in enumerate(input.splitlines()):
        for c, ch in enumerate(row):
            grid[(r, c)] = ch

    return grid

def outside(coord: tuple[int, int], checks: list[tuple[int, int]], anti_checks: list[tuple[int, int]], grid: dict[tuple[int, int], chr],
            region: list[tuple[int, int]]) -> bool:
    r, c = coord
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == dc == 0:
                continue
            rr = r + dr
            cc = c + dc
            different = (rr, cc) not in grid or grid[(rr, cc)] != grid[coord] or (grid[(rr, cc)] == grid[coord] and (rr, cc) not in region)

            if not different and (rr, cc) in checks:
                return False
            if different and (rr, cc) in anti_checks:
                return False

    return True


def get_sides(coords: list[tuple[int, int]], grid: dict[tuple[int, int], chr]) -> int:
    sides = 0

    for coord in coords:
        r, c = coord

        # Top-Right outside corner
        if outside(coord, [(r - 1, c), (r, c + 1)], [], grid, coords):
            sides += 1
        # Bottom-Right outside corner
        if outside(coord, [(r, c + 1), (r + 1, c)], [], grid, coords):
            sides += 1
        # Bottom-Left outside corner
        if outside(coord, [(r + 1, c), (r, c - 1)], [], grid, coords):
            sides += 1
        # Top-Left outside corner
        if outside(coord, [(r, c - 1), (r - 1, c)], [], grid, coords):
            sides += 1
        # Top-Right inside corner
        if outside(coord, [(r - 1, c + 1)], [(r - 1, c), (r, c + 1)], grid, coords):
            sides += 1
        # Bottom-Right inside corner
        if outside(coord, [(r + 1, c + 1)], [(r, c + 1), (r + 1, c)], grid, coords):
            sides += 1
        # Bottom-Left inside corner
        if outside(coord, [(r + 1, c - 1)], [(r + 1, c), (r, c - 1)], grid, coords):
            sides += 1
        # Top-Left inside corner
        if outside(coord, [(r - 1, c - 1)], [(r, c - 1), (r - 1, c)], grid, coords):
            sides += 1

    return sides

def get_perimeter(coord: tuple[int, int], grid: dict[tuple[int, int], chr]) -> int:
    total = 0
    r, c = coord

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        rr = r + dr
        cc = c + dc

        if (rr, cc) not in grid:
            total += 1
            continue

        if grid[(rr, cc)] != grid[coord]:
            total += 1

    return total

def locate_regions(grid: dict[tuple[int, int], chr]):
    regions = {}
    seen = set()

    for coord in grid.keys():
        region = set()
        queue = deque([(coord, 1, get_perimeter(coord, grid))])
        perimeter = 0
        area = 0

        while queue:
            (r, c), a, p = queue.popleft()

            if (r, c) in seen:
                continue
            seen.add((r, c))
            region.add((r, c))

            perimeter += p
            area += a

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                rr = r + dr
                cc = c + dc

                if (rr, cc) in grid and grid[(rr, cc)] == grid[coord]:
                    queue.append(((rr, cc), 1, get_perimeter((rr, cc), grid)))

        if area == perimeter == 0:
            continue

        regions[tuple(region)] = area * perimeter

    return regions

def part1(input: str) -> int:
    grid = parse_input(input)

    regions = locate_regions(grid)

    return sum(regions.values())

def part2(input: str) -> int:
    grid = parse_input(input)

    regions = locate_regions(grid)
    total = 0

    for region in regions.keys():
        total += len(region) * get_sides(list(region), grid)

    return total

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















