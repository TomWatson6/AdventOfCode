from collections import Counter

input = open("input.txt").read().strip()

def parse(input: str):
    return input.splitlines()

def part1(input: str) -> int:
    boxes = parse(input)
    twos = 0
    threes = 0

    for box in boxes:
        c = Counter([b for b in box])

        if any(v == 2 for v in c.values()):
            twos += 1

        if any(v == 3 for v in c.values()):
            threes += 1

    return twos * threes

def part2(input: str) -> int:
    boxes = parse(input)

    for a in range(len(boxes) - 1):
        for b in range(a + 1, len(boxes)):
            left, right = boxes[a], boxes[b]

            if len(left) != len(right):
                continue

            count = 0
            chars = ""

            for ch in range(len(left)):
                if left[ch] != right[ch]:
                    count += 1
                else:
                    chars += left[ch]

            if count == 1:
                return chars

    return "Boxes not found"

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















