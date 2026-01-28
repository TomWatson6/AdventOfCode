
input = open("input.txt").read().strip()

def parse(input: str):
    return [int(x.strip('+')) for x in input.splitlines()]

def part1(input: str) -> int:
    numbers = parse(input)
    return sum(numbers)

def part2(input: str) -> int:
    numbers = parse(input)
    i = 0
    seen = set()
    curr = 0

    while True:
        if curr in seen:
            break
        seen.add(curr)
        curr += numbers[i]
        i = (i + 1) % len(numbers)

    return curr

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















