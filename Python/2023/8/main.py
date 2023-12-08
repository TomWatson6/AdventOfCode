
with open(0) as f:
    lines = [x.strip() for x in f.readlines()]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

D = {}
DP = {}

I = [x for x in lines[0]]

for line in lines[2:]:
    start, finish = line.split(" = ")
    left, right = [x.strip("(").strip(")") for x in finish.split(", ")]
    D[start] = (left, right)

pos = "AAA"
count = 0

while True:
    i = I[count % len(I)]
    if i == 'L':
        pos = D[pos][0]
    elif i == 'R':
        pos = D[pos][1]
    else:
        assert False, i

    count += 1

    if pos == 'ZZZ':
        break

print("Part 1:", count)

count = 0
steps = 0
starts = [d for d in D.keys() if d[-1] == 'A']
positions = [d for d in D.keys() if d[-1] == 'A']
inc = 1
M = {}

for x in range(len(positions)):
    count = 0
    S = {}

    while True:
        i = I[count % len(I)]
        if i == 'L':
            positions[x] = D[positions[x]][0]
        elif i == 'R':
            positions[x] = D[positions[x]][1]
        else:
            assert False, i

        count += inc

        if positions[x][-1] == 'Z' and positions[x] in S:
            M[starts[x]] = (count, lcm(inc, count - S[positions[x]]))
            break

        S[positions[x]] = count

mult = 1

for m in M.values():
    mult = lcm(mult, m[1])

print("Part 2:", mult)


















