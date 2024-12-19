
input = open("input.txt").read().strip()

def parse_input(input):
    patterns, towels = input.split("\n\n")
    patterns = set(patterns.split(", "))
    towels = towels.splitlines()

    return patterns, towels

DP = {}

def find(pattern, patterns):
    curr_valid = False

    if pattern in patterns:
        curr_valid = True

    if pattern in DP:
        return DP[pattern]

    outcomes = []

    for i in range(1, len(pattern)):
        section = pattern[:i]
        if section in patterns:
            outcomes.append(find(pattern[i:], patterns))

    if len(outcomes) == 0:
        DP[pattern] = curr_valid + 0
        return curr_valid + 0

    DP[pattern] = curr_valid + sum(outcomes)

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















