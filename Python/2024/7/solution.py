
input = open("input.txt").read().strip()

def parse_input(input: str) -> list[tuple[int, list[int]]]:
    lines = input.splitlines()
    outputs = []

    for test, right in [x.split(": ") for x in lines]:
        test = int(test)
        right = [int(x) for x in right.split(' ')]
        outputs.append((test, right))

    return outputs

def solve(outcome: int, leftover: list[int], p2: bool) -> int:
    assert len(leftover) >= 2
    if sum(leftover) > outcome:
        return 0

    left = leftover.pop(0)
    right = leftover.pop(0)

    ops = ["add", "mult", "concat"] if p2 else ["add", "mult"]

    for op in ops:
        output = 0
        match op:
            case "add":
                output = left + right
            case "mult":
                output = left * right
            case "concat":
                output = int(str(left) + str(right))
        if output == outcome and len(leftover) == 0:
            return outcome
        elif len(leftover) > 0:
            new_leftover = [output] + leftover
            output = solve(outcome, new_leftover, p2)
            if output != 0:
                return output

    return 0

def part1(input: str) -> int:
    tests = parse_input(input)
    total = 0

    for test, nums in tests:
        total += solve(test, nums, False)

    return total

def part2(input: str) -> int:
    tests = parse_input(input)
    total = 0

    for test, nums in tests:
        total += solve(test, nums, True)

    return total

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















