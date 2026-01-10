
input = open("input.txt").read().strip()

def parse(input: str):
    return [int(x) for x in list(input.strip())]

pattern = [0, 1, 0, -1]
DP = {}

def get_ranges(N, count):
    if count in DP:
        return DP[count]

    pos_ranges = []
    neg_ranges = []

    for i in range(0, N, count * 4):
        lower = i + count - 1
        upper = i + count * 2 - 2
        pos_ranges.append((lower, upper))
        lower = i + count * 3 - 1
        upper = i + count * 4 - 2
        neg_ranges.append((lower, upper))

    DP[count] = (pos_ranges, neg_ranges)
    return pos_ranges, neg_ranges

def fft(numbers):
    totals = []

    for i, n in enumerate(numbers):
        if i == 0:
            totals.append(n)
            continue

        totals.append(n + totals[i - 1])

    new_numbers = []

    for count in range(1, len(numbers) + 1):
        pos_ranges, neg_ranges = get_ranges(len(numbers), count)
        new_number = 0

        for lower, upper in pos_ranges:
            if 0 <= lower - 1 < len(totals) and 0 <= upper < len(totals):
                new_number += totals[upper] - totals[lower - 1]
            elif 0 <= lower - 1 < len(totals):
                new_number += totals[-1] - totals[lower - 1]
            elif 0 <= upper < len(totals):
                new_number += totals[upper]

        for lower, upper in neg_ranges:
            if 0 <= lower - 1 < len(totals) and 0 <= upper < len(totals):
                new_number -= totals[upper] - totals[lower - 1]
            elif 0 <= lower - 1 < len(totals):
                new_number -= totals[-1] - totals[lower - 1]
            elif 0 <= upper < len(totals):
                new_number -= totals[upper]

        new_numbers.append(int(str(new_number)[-1]))

    return new_numbers

def part1(input: str) -> int:
    numbers = parse(input)

    for _ in range(4 if len(numbers) == 8 else 100):
        numbers = fft(numbers)

    return "".join([str(x) for x in numbers[:8]])

def part2(input: str) -> int:
    numbers = parse(input)
    offset = int("".join(str(n) for n in numbers[:7]))
    numbers *= 10000

    for i in range(100):
        numbers = fft(numbers)

    return "".join([str(x) for x in numbers[offset:offset + 8]])

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















