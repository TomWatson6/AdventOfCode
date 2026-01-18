
input = open("input.txt").read().strip()

def parse(input: str):
    return [list(map(int, x.split())) for x in input.splitlines()]

def part1(input: str) -> int:
    lines = parse(input)
    total = 0

    for line in lines:
        for a, b, c in list(zip(line, line[1:] + [line[0]], [line[2]] + line[:2])):
            if a + b <= c:
                break
        else:
            total += 1

    return total

def part2(input: str) -> int:
    lines = parse(input)
    total = 0

    for i in range(0, len(lines), 3):
        for a, b, c in list(zip(lines[i], lines[i + 1], lines[i + 2])):
            if any([a + b <= c, b + c <= a, c + a <= b]):
                continue

            total += 1

    return total

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















