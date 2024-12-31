from collections import Counter

input = open("input.txt").read().strip()

def parse_input(input):
    keys = []
    locks = []

    blocks = input.split("\n\n")

    for block in blocks:
        lines = block.splitlines()

        if lines[0][0] == '#':
            key = {}
            for r, row in enumerate(lines):
                for c, ch in enumerate(row):
                    key[(r, c)] = ch
            keys.append(key)
        else:
            lock = {}
            for r, row in enumerate(lines):
                for c, ch in enumerate(row):
                    lock[(r, c)] = ch

            locks.append(lock)

    return keys, locks

def fit(key, lock):
    key_cols = Counter([k[1] for k, v in key.items() if v == '#'])
    lock_cols = Counter(k[1] for k, v in lock.items() if v == '#')
    totals = []

    for k, v in key_cols.items():
        totals.append(v + lock_cols[k])

    return all(x <= 7 for x in totals)

def part1(input: str) -> int:
    keys, locks = parse_input(input)
    total = 0

    for key in keys:
        for lock in locks:
            if fit(key, lock):
                total += 1

    return total

def part2(input: str) -> int:
    return 0

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















