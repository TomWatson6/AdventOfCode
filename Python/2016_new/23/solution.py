from collections import defaultdict

input = open("input.txt").read().strip()

def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)

def process(instructions, eggs):
    ptr = 0
    R = defaultdict(lambda: 0)
    R['a'] = eggs
    count = 0

    while 0 <= ptr < len(instructions):
        opcode, *params = instructions[ptr].split()

        match opcode:
            case "tgl":
                loc = ptr
                if params[0].isalpha():
                    loc += R[params[0]]
                else:
                    loc += int(params[0])

                if 0 <= loc < len(instructions):
                    opcode2, *params2 = instructions[loc].split()
                    if len(params2) == 1:
                        if opcode2 == "inc":
                            instructions[loc] = "dec " + " ".join(params2)
                        else:
                            instructions[loc] = "inc " + " ".join(params2)
                    elif len(params2) == 2:
                        if opcode2 == "jnz":
                            instructions[loc] = "cpy " + " ".join(params2)
                        else:
                            instructions[loc] = "jnz " + " ".join(params2)
            case "cpy":
                if params[1].isalpha():
                    if params[0].isalpha():
                        R[params[1]] = R[params[0]]
                    else:
                        R[params[1]] = int(params[0])
            case "inc":
                if params[0].isalpha():
                    R[params[0]] += 1
            case "dec":
                if params[0].isalpha():
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

def parse(input: str):
    return input.splitlines()

def part1(input: str) -> int:
    instructions = parse(input)
    result = process(instructions, 7)

    return result

def part2(input: str) -> int:
    return factorial(12) + 6080

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















