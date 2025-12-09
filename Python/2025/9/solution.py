
input = open("input.txt").read().strip()

def parse(input: str):
    return [list(map(int, num.split(","))) for num in input.splitlines()]

def rect_area(a, b):
    width = abs(a[1] - b[1]) + 1
    height = abs(a[0] - b[0]) + 1

    return width * height

def part1(input: str) -> int:
    coords = parse(input)
    largest = 0

    for i in range(len(coords) - 1):
        for j in range(i + 1, len(coords)):
            largest = max(largest, rect_area(coords[i], coords[j]))

    return largest

def part2(input: str) -> int:
    return 0

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















