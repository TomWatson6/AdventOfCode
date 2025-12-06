
input = open("input.txt").read().strip()

def parse(input: str):
    lines = input.splitlines()
    numbers, symbols = lines[:-1], lines[-1]
    numbers = [[int(x) for x in n.split(" ") if x != ""] for n in numbers]
    symbols = [x for x in symbols.split(" ") if x != ""]

    return numbers, symbols

def parse2(input: str):
    lines = input.splitlines()
    lines[-1] += "  "
    return lines

def part1(input: str) -> int:
    numbers, symbols = parse(input)
    total = 0
    
    for i in range(len(numbers[0])):
        nums = []
        for j in range(len(numbers)):
            nums.append(numbers[j][i])
        total += eval(symbols[i].join([str(n) for n in nums]))

    return total

def part2(input: str) -> int:
    lines = parse2(input)
    i = 0
    symbol = "+"
    curr = ""
    total = 0

    while i < len(lines[0]):
        addition = ""

        for j in range(len(lines)):
            addition += lines[j][i]

        if addition.strip() == '':
            curr = curr[:-1]
            total += eval(curr)
            curr = ""
            i += 1
            continue

        if addition[-1] in ["+", "*"]:
            symbol = addition[-1]
            addition = addition[:-1]

        addition = addition.strip()
        curr += addition
        curr += symbol

        i += 1

    total += eval(curr[:-1])

    return total

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















