from functools import cache

input = open("input.txt").read().strip()

def parse(input: str):
    return input

@cache
def is_safe(first_row, r, c):
    if c < 0 or c >= len(first_row):
        return True

    if r == 0:
        return first_row[c] == '.'

    left = is_safe(first_row, r - 1, c - 1)
    centre = is_safe(first_row, r - 1, c)
    right = is_safe(first_row, r - 1, c + 1)

    if not left and not centre and right:
        return False
    
    if not centre and not right and left:
        return False
    
    if not left and centre and right:
        return False
    
    if not right and centre and left:
        return False

    return True

def part1(input: str) -> int:
    first_row = parse(input)
    safe = 0

    for r in range(40):
        for c in range(len(first_row)):
            safe += is_safe(first_row, r, c)

    return safe

def part2(input: str) -> int:
    first_row = parse(input)
    safe = 0

    for r in range(400_000):
        for c in range(len(first_row)):
            safe += is_safe(first_row, r, c)

    return safe

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















