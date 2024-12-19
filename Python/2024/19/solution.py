
input = open("input.txt").read().strip()

def parse_input(input):
    patterns, towels = input.split("\n\n")
    patterns = set(patterns.split(", "))
    towels = towels.splitlines()

    return patterns, towels

DP = {}

def find(towel, patterns):
    curr_valid = False

    if towel in patterns:
        curr_valid = True

    if towel in DP:
        return DP[towel]

    outcomes = []

    for i in range(1, len(towel)):
        section = towel[:i]
        if section in patterns:
            outcomes.append(find(towel[i:], patterns))

    if len(outcomes) == 0:
        DP[towel] = curr_valid
        return curr_valid

    DP[towel] = curr_valid + sum(outcomes)

    return curr_valid + sum(outcomes)

def part1(input: str) -> int:
    patterns, towels = parse_input(input)
    total = 0

    for towel in towels:
        total += find(towel, patterns) > 0

    return total

def part2(input: str) -> int:
    patterns, towels = parse_input(input)
    total = 0

    for towel in towels:
        outcome = find(towel, patterns)
        total += outcome

    return total

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















