from collections import defaultdict, deque

with open(0) as f:
    lines = [x.strip() for x in f.readlines()]

R = defaultdict(int)
sound = -1
i = 0

def get(val):
    if val.strip("-").isdigit():
        return int(val)
    return R[val]

while i < len(lines):
    line = lines[i]
    cmd, *rest = line.split()

    match cmd:
        case "snd":
            reg = rest[0]
            sound = R[reg]
        case "set":
            reg, val = rest
            R[reg] = get(val)
        case "add":
            reg, val = rest
            R[reg] += get(val)
        case "mul":
            reg, val = rest
            R[reg] *= get(val)
        case "mod":
            reg, val = rest
            R[reg] %= get(val)
        case "rcv":
            reg = rest[0]
            if R[reg] != 0:
                assert sound != -1
                print("Part 1:", sound)
                break
        case "jgz":
            reg, val = rest
            if R[reg] > 0:
                i = (i + get(val)) % len(lines)
                continue

    i += 1

R = [defaultdict(int), defaultdict(int)]
R[1]['p'] = 1

p = 0 # Program being run currently
i = [0, 0]
sent = [deque(), deque()]
count = 0

def get2(val):
    if val.strip("-").isdigit():
        return int(val)
    return R[p][val]

while True:
    line = lines[i[p]]
    cmd, *rest = line.split()

    match cmd:
        case "snd":
            reg = rest[0]
            if p == 1:
                count += 1
            sent[not p].append(get2(reg))
        case "set":
            reg, val = rest
            R[p][reg] = get2(val)
        case "add":
            reg, val = rest
            R[p][reg] += get2(val)
        case "mul":
            reg, val = rest
            R[p][reg] *= get2(val)
        case "mod":
            reg, val = rest
            R[p][reg] %= get2(val)
        case "rcv":
            reg = rest[0]
            if len(sent[p]) > 0:
                R[p][reg] = sent[p].popleft()
            elif len(sent[p]) == len(sent[not p]) == 0:
                break
            else:
                p = not p
                continue
        case "jgz":
            reg, val = rest
            if get2(reg) > 0:
                i[p] = (i[p] + get2(val)) % len(lines)
                continue
    i[p] += 1

print("Part 2:", count)



















