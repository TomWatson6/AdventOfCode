from collections import defaultdict
from copy import deepcopy

with open(0) as f:
    instructions = [x.strip() for x in f.readlines()]

instructions = [i.split() for i in instructions]

def run(a):
    def get(x):
        try:
            x = int(x)
            return x
        except:
            return R[x]

    R = defaultdict(int)
    H = []
    R['a'] = a
    mul = 0
    i = 0
    J = defaultdict(lambda: int(1e9))
    count = 0

    while i < len(instructions):
        cmd, x, y = instructions[i]

        if cmd == "set":
            R[x] = get(y)
        elif cmd == "sub":
            R[x] -= get(y)
        elif cmd == "mul":
            R[x] *= get(y)
            mul += 1
        elif cmd == "jnz":
            if get(x) != 0:
                i += get(y)
                continue
        else:
            assert False, (cmd, x, y)

        if x == 'h':
            H.append(R['h'])

        count += 1
        i += 1

    return mul if a == 0 else R['h']

print("Part 1:", run(0))
print("Part 2:", run(1))























