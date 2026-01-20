
input = open("input.txt").read().strip()

def parse(input: str):
    lines = input.splitlines()
    blacklist = [(int(a), int(b)) for a, b in [line.split('-') for line in lines]]
    return blacklist

def combine(a, b):
    lower1, upper1 = a
    lower2, upper2 = b

    if lower1 <= lower2 <= upper2 <= upper1:
        return [a]

    if lower2 <= lower1 <= upper1 <= upper2:
        return [b]

    if lower1 <= lower2 <= upper1 <= upper2:
        return [(lower1, upper2)]

    if lower2 <= lower1 <= upper2 <= upper1:
        return [(lower2, upper1)]

    return [a, b]


def part1(input: str) -> int:
    blacklist = parse(input)
    blacklist = sorted(blacklist)

    for a, b in list(zip(blacklist, blacklist[1:])):
        if len(combine(a, b)) == 2 and a[1] != b[0] - 1:
            return a[1] + 1

    return 0

def part2(input: str) -> int:
    blacklist = parse(input)
    blacklist = sorted(blacklist)
    while True:
        changed = False
        for i in range(len(blacklist) - 1):
            combination = combine(blacklist[i], blacklist[i + 1])
            if len(combination) == 1:
                blacklist = blacklist[:i] + combination + blacklist[i + 2:]
                changed = True
                break

        if not changed:
            break
            
    largest = 4294967295
    total = sum(b - a + 1 for a, b in blacklist)

    return largest - total + 1

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















