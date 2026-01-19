from collections import Counter

input = open("input.txt").read().strip()

def parse(input: str):
    ranges = input.split(',')
    ranges = [[int(y) for y in x.split('-')] for x in ranges]
    return ranges

def is_invalid(number, p2):
    pattern = str(number)

    if pattern[0] == '0':
        return True

    if len(pattern) % 2 != 0 and not p2:
        return False

    left, right = pattern[:len(pattern) // 2], pattern[len(pattern) // 2:]

    if left == right:
        return True

    if p2:
        for l in range(1, len(pattern) // 2 + 1):
            counts = Counter()
            wrong = False

            for i in range(0, len(pattern), l):
                if i + l > len(pattern):
                    wrong = True
                    break

                part = pattern[i:i + l]

                if part.startswith('0'):
                    wrong = True
                    break

                counts[part] += 1

            if not wrong:
                if len(counts) == 1:
                    return True

    return False

def part1(input: str) -> int:
    ranges = parse(input)
    invalid = []

    for low, high in ranges:
        for number in range(low, high + 1):
            if is_invalid(number, False):
                invalid.append(number)
    
    return sum(invalid)

def part2(input: str) -> int:
    ranges = parse(input)
    invalid = []

    for low, high in ranges:
        for number in range(low, high + 1):
            if is_invalid(number, True):
                invalid.append(number)
    
    return sum(invalid)

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















