import sys

sys.setrecursionlimit(int(1e9))

with open(0) as f:
    blocks = [x.strip() for x in f.read().split("\n\n")]

rules = [x.strip() for x in blocks[0].split("\n")]
parts = [x.strip() for x in blocks[1].split("\n")]

R = {}

for rule in rules:
    name, rule = rule.split("{")
    rule = rule.strip("}")
    rs = rule.split(",")
    R[name] = [r.split(":") for r in rs]

U = 4001

def search(rules, lx, ux, lm, um, la, ua, ls, us):
    rule = rules[0]

    if len(rules) == 1:
        x = max(0, ux - lx - 1)
        m = max(0, um - lm - 1)
        a = max(0, ua - la - 1)
        s = max(0, us - ls - 1)

        if rule[0] == 'A':
            return x * m * a * s
        elif rule[0] == 'R':
            return 0
        else:
            return search(R[rule[0]], lx, ux, lm, um, la, ua, ls, us)

    rest = rules[1:]

    con = rule[0]
    var = con[0]
    sign = con[1]
    dest = rule[1]
    val = int(con[2:])

    if var == 'x':
        if sign == '>':
            return search([[dest]], val, ux, lm, um, la, ua, ls, us) + search(rest, lx, val + 1, lm, um, la, ua, ls, us)
        else:
            return search([[dest]], lx, val, lm, um, la, ua, ls, us) + search(rest, val - 1, ux, lm, um, la, ua, ls, us)
    elif var == 'm':
        if sign == '>':
            return search([[dest]], lx, ux, val, um, la, ua, ls, us) + search(rest, lx, ux, lm, val + 1, la, ua, ls, us)
        else:
            return search([[dest]], lx, ux, lm, val, la, ua, ls, us) + search(rest, lx, ux, val - 1, um, la, ua, ls, us)
    elif var == 'a':
        if sign == '>':
            return search([[dest]], lx, ux, lm, um, val, ua, ls, us) + search(rest, lx, ux, lm, um, la, val + 1, ls, us)
        else:
            return search([[dest]], lx, ux, lm, um, la, val, ls, us) + search(rest, lx, ux, lm, um, val - 1, ua, ls, us)
    elif var == 's':
        if sign == '>':
            return search([[dest]], lx, ux, lm, um, la, ua, val, us) + search(rest, lx, ux, lm, um, la, ua, ls, val + 1)
        else:
            return search([[dest]], lx, ux, lm, um, la, ua, ls, val) + search(rest, lx, ux, lm, um, la, ua, val - 1, us)

ACC = []
REJ = []

def is_valid(A):
    rules = R["in"]
    n = None

    while True:
        done = False
        for rule in rules:
            # print(rule)
            if len(rule) == 1:
                if rule[0] == 'A':
                    return True
                    done = True
                elif rule[0] == 'R':
                    return False
                    done = True
                else:
                    n = rule[0]
                break

            if eval(str(A[rule[0][0]]) + rule[0][1:]):
                if rule[1] == 'A':
                    return True
                    done = True
                elif rule[1] == 'R':
                    return False
                    done = True
                else:
                    n = rule[1]
                break

        if done:
            break
        rules = R[n]

    return False

for part in parts:
    part = part[1:-1].split(",")
    A = {}
    for p in part:
        name, val = p.split("=")
        A[name] = int(val)

    if is_valid(A):
        ACC.append(A)
    else:
        REJ.append(A)

total = 0

for a in ACC:
    for k, v in a.items():
        total += v

print("Part 1:", total)
print("Part 2:", search(R["in"], 0, U, 0, U, 0, U, 0, U))






















