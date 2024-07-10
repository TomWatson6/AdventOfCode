from copy import deepcopy as dc

with open(0) as f:
    a = f.read().strip()

def expand(a):
    b = dc(a)
    b = b[::-1]
    b = "".join(["1" if x == "0" else "0" for x in b])
    return a + "0" + b

DP = {}

def crunch(a):
    if a in DP:
        return DP[a]

    if len(a) % 2 == 1:
        return a

    left = crunch(a[:len(a) // 2])
    right = crunch(a[len(a) // 2:])

    a = left + right
    output = ""

    for i in range(0, len(a), 2):
        x = a[i]
        y = a[i + 1]

        if x == y:
            output += "1"
        else:
            output += "0"

    DP[a] = output

    return output

def solve(a, disk_size):
    while len(a) < disk_size:
        a = expand(a)

    a = a[:disk_size]
    a = crunch(a)

    return a

print("Part 1:", solve(a, 272))
print("Part 2:", solve(a, 35651584))








