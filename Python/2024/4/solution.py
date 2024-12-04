

input = open("input.txt").read().strip()

def parse_grid(input: str) -> dict[tuple[int, int], chr]:
    lines = input.splitlines()
    grid = {}

    for r, row in enumerate(lines):
        for c, ch in enumerate(row):
            grid[(r, c)] = ch

    return grid

def find(word: str, grid: dict[tuple[int, int], chr]) -> int:
    count = 0

    for (r, c), ch in grid.items():
        if ch == word[0]:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    check = word[0]
                    if dr == dc == 0:
                        continue
                    for i in range(1, len(word)):
                        rr = r + dr * i
                        cc = c + dc * i
                        if (rr, cc) in grid:
                            check += grid[(rr, cc)]
                        else:
                            break

                    if check == word:
                        count += 1

    return count

def find2(word: str, grid: dict[tuple[int, int], chr]) -> int:
    assert len(word) == 3

    count = 0

    for (r, c), ch in grid.items():
        if ch == word[1] and all(x in grid for x in [(r - 1, c + 1), (r + 1, c + 1), (r + 1, c - 1), (r - 1, c - 1)]):
            w1 = "".join(grid[(r - 1, c - 1)] + grid[(r, c)] + grid[(r + 1, c + 1)])
            w2 = "".join(grid[(r - 1, c + 1)] + grid[(r, c)] + grid[(r + 1, c - 1)])

            if word in [w1, w1[::-1]] and word in [w2, w2[::-1]]:
                count += 1

    return count



def part1(input: str) -> int:
    grid = parse_grid(input)
    count = find("XMAS", grid)

    return count

def part2(input: str) -> int:
    grid = parse_grid(input)
    count = find2("MAS", grid)

    return count

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















