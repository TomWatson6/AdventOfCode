import re

input = open("input.txt").read().strip()

def parse(input: str):
    lines = input.splitlines()
    return lines

def configure_bots(lines):
    bots = {}

    for line in lines:
        if line.startswith("value"):
            val, bot = list(re.findall(r"\d+|bot \d+", line))
            val = int(val)
            if bot in bots:
                lower, upper = bots[bot]
                if val < lower:
                    lower = val
                elif val > upper:
                    upper = val
                else:
                    assert False, (lower, upper, val)
            else:
                bots[bot] = (val, val)

        elif line.startswith("bot"):
            origin, low_bot, high_bot = list(re.findall(r"bot \d+|output \d+", line))
            lower, upper = bots[origin]

            if low_bot in bots:
                lo, hi = bots[low_bot]
                bots[low_bot] = (lower, hi)
            else:
                bots[low_bot] = (lo, lower)

            if high_bot in bots:
                lo, hi = bots[high_bot]
                bots[high_bot] = (lo, upper)
            else:
                bots[high_bot] = (upper, upper)

    return bots

def part1(input: str) -> int:
    lines = parse(input)

    bots = configure_bots(lines)
    print(bots)

    return 0

def part2(input: str) -> int:
    return 0

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















