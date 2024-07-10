from collections import defaultdict

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

instructions = []

for line in lines:
    parts = [x.strip(",") for x in line.split()]
    instructions.append(parts)

def run(a):
    R = defaultdict(int)
    R['a'] = a
    i = 0

    while i < len(instructions):
        cmd, *rest = instructions[i]

        if cmd == "hlf":
            R[rest[0]] //= 2
        elif cmd == "tpl":
            R[rest[0]] *= 3
        elif cmd == "inc":
            R[rest[0]] += 1
        elif cmd == "jmp":
            i += int(rest[0])
            continue
        elif cmd == "jie":
            if R[rest[0]] % 2 == 0:
                i += int(rest[1])
                continue
        elif cmd == "jio":
            if R[rest[0]] == 1:
                i += int(rest[1])
                continue

        i += 1

    return R['b']

print("Part 1:", run(0))
print("Part 2:", run(1))





















