from collections import defaultdict

with open(0) as f:
    instructions = [x.strip() for x in f.readlines()]


R = defaultdict(int)
i = 0

def get(x):
    if x.isdigit():
        return int(x)

    return R[x]

def process():
    global R, i
    while i < len(instructions):
        parts = instructions[i].split()

        if parts[0] == "cpy":
            R[parts[2]] = get(parts[1])
        elif parts[0] == "inc":
            R[parts[1]] += 1
        elif parts[0] == "dec":
            R[parts[1]] -= 1
        elif parts[0] == "jnz":
            x = get(parts[1])
            if x != 0:
                i += int(parts[2])
                continue

        i += 1

process()

print("Part 1:", R['a'])

R = defaultdict(int)
R['c'] = 1
i = 0

process()

print("Part 2:", R['a'])
















