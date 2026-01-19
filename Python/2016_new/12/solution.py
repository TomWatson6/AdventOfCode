from collections import defaultdict

input = open("input.txt").read().strip()

def parse(input: str):
    return input.splitlines()

def process(instructions, p2):
    ptr = 0
    R = defaultdict(lambda: 0)

    if p2:
        R['c'] = 1

    while 0 <= ptr < len(instructions):
        opcode, *params = instructions[ptr].split()

        match opcode:
            case "cpy":
                if params[0].isalpha():
                    R[params[1]] = R[params[0]]
                else:
                    R[params[1]] = int(params[0])
            case "inc":
                R[params[0]] += 1
            case "dec":
                R[params[0]] -= 1
            case "jnz":
                check = 0
                if params[0].isalpha():
                    check = R[params[0]]
                else:
                    check = int(params[0])

                if check != 0:
                    val = 0
                    if params[1].isalpha():
                        val = R[params[1]]
                    else:
                        val = int(params[1])

                    ptr += val
                    continue

        ptr += 1

    return R['a']

def part1(input: str) -> int:
    instructions = parse(input)

    return process(instructions, False)

def part2(input: str) -> int:
    instructions = parse(input)

    return process(instructions, True)

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















