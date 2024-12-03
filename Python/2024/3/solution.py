from collections import defaultdict
import re

input = open("input.txt").read().strip()

def part1(input: str) -> int:
    mults = [list(map(int, x.split(","))) for x in list(re.findall(r"mul\((-?\d+,-?\d+)\)", input))]
    total = 0

    for left, right in mults:
        total += left * right

    return total

def part2(input: str) -> int:
    mults = [[x for x in l if x != ''][0] for l in list(re.findall(r"(do\(\))|(don\'t\(\))|mul\((-?\d+,-?\d+)\)", input))]
    enabled = True
    total = 0

    for match in mults:
        if match == "don't()":
            enabled = False
            continue
        if match == "do()":
            enabled = True
            continue
        if enabled:
            left, right = [int(x) for x in match.split(",")]
            total += left * right

    return total

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















