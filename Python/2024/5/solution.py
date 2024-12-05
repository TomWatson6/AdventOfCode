from collections import defaultdict

input = open("input.txt").read().strip()

follows = defaultdict(list)

def parse_input(input: str) -> list[list[int]]:
    global follows

    chunks = input.replace("\r", "").split("\n\n")
    lines = chunks[0].splitlines()

    for line in chunks[0].splitlines():
        left, right = [int(x) for x in line.split("|")]
        follows[left].append(right)

    updates = []

    for line in chunks[1].splitlines():
        nums = [int(x) for x in line.split(",")]
        updates.append(nums)

    return updates

def validate(update: list[int]) -> bool:
    valid = True

    for i, item in enumerate(update):
        if item not in follows:
            continue

        valid = valid and all(update.index(f) > i if f in update else True for f in follows[item])

    if valid:
        return True

    return False

def order(update: list[int]) -> list[int]:
    while not validate(update):
        i = 0
        while i < len(update) - 1:
            left = update[i]
            right = update[i + 1]
            check = follows[right]
            if left in check:
                update[i], update[i + 1] = update[i + 1], update[i]
                break

            i += 1

    return update

def part1(input: str) -> int:
    updates = parse_input(input)

    mids = []

    for update in updates:
        if validate(update):
            mids.append(update[len(update) // 2])

    return sum(mids)

def part2(input: str) -> int:
    updates = parse_input(input)

    mids = []
    invalid = []

    for update in updates:
        valid = validate(update)
        if not valid:
            invalid.append(update)

    for update in invalid:
        fixed = order(update)
        mids.append(fixed[len(fixed) // 2])

    return sum(mids)

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















