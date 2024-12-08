from collections import defaultdict

input = open("input.txt").read().strip()

def parse_input(input: str) -> dict[tuple[int, int], chr]:
    grid = {}

    for r, row in enumerate([x.strip() for x in input.splitlines()]):
        for c, ch in enumerate(row):
            grid[(r, c)] = ch

    return grid

def get_antennas(grid: dict[tuple[int, int], chr]) -> dict[chr, list[tuple[int, int]]]:
    antennas = defaultdict(list)

    for k, v in grid.items():
        if v != '.':
            antennas[v].append(k)

    return antennas

def get_antinodes(grid: dict[tuple[int, int], chr], coords: list[tuple[int, int]]) -> set[tuple[int, int]]:
    antinodes = set()

    for i in range(len(coords) - 1):
        for j in range(i + 1, len(coords)):
            left, right = coords[i], coords[j]
            before = (left[0] + left[0] - right[0], left[1] + left[1] - right[1])
            after = (right[0] + right[0] - left[0], right[1] + right[1] - left[1])
            if before in grid:
                antinodes.add(before)
            if after in grid:
                antinodes.add(after)

    return antinodes

def get_antinodes2(grid: dict[tuple[int, int], chr], coords: list[tuple[int, int]]) -> set[tuple[int, int]]:
    antinodes = set()

    for i in range(len(coords) - 1):
        for j in range(i + 1, len(coords)):
            left, right = coords[i], coords[j]
            antinodes.add(left)
            antinodes.add(right)
            curr = left
            prev = right
            while curr in grid:
                _curr = (curr[0], curr[1])
                curr = (curr[0] + curr[0] - prev[0], curr[1] + curr[1] - prev[1])
                prev = _curr
                if curr in grid:
                    antinodes.add(curr)

            curr = right
            prev = left
            while curr in grid:
                _curr = (curr[0], curr[1])
                curr = (curr[0] + curr[0] - prev[0], curr[1] + curr[1] - prev[1])
                prev = _curr
                if curr in grid:
                    antinodes.add(curr)

    return antinodes

def part1(input: str) -> int:
    grid = parse_input(input)
    antennas = get_antennas(grid)
    antinodes = set()

    for v in antennas.values():
        antinodes = antinodes.union(get_antinodes(grid, v))

    return len(antinodes)

def part2(input: str) -> int:
    grid = parse_input(input)
    antennas = get_antennas(grid)
    antinodes = set()

    for v in antennas.values():
        antinodes = antinodes.union(get_antinodes2(grid, v))

    return len(antinodes)

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















