
input = open("input.txt").read().strip()

def parse(input: str):
    return [int(x) for x in input.splitlines()]

def fuel(num):
    return num // 3 - 2

def fuel2(num):
    output = num // 3 - 2

    return output + fuel2(output) if output > 0 else 0

def part1(input: str) -> int:
    numbers = parse(input)

    return sum(fuel(num) for num in numbers)

def part2(input: str) -> int:
    numbers = parse(input)

    return sum(fuel2(num) for num in numbers)

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















