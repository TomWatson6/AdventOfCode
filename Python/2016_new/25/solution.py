from collections import defaultdict

input = open("input.txt").read().strip()

outputs = []

def process(instructions, input_code):
    global outputs
    ptr = 0
    R = defaultdict(lambda: 0)
    R['a'] = input_code
    count = 0

    while 0 <= ptr < len(instructions):
        opcode, *params = instructions[ptr].split()
        count += 1

        if count % 100_000 == 0:
            return

        match opcode:
            case "out":
                if params[0].isalpha():
                    outputs.append(R[params[0]])
                else:
                    outputs.append(int(params[0]))
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
    global outputs
    instructions = parse(input)
    i = 0

    while True:
        process(instructions, i)
        if all(abs(a - b) == 1 for a, b in zip(outputs, outputs[1:])):
            break
        outputs = []
        i += 1

    return i

def part2(input: str) -> int:
    return 0

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















