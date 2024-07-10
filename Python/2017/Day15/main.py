from collections import deque

with open(0) as f:
    A, B = [int(x.strip().split()[-1]) for x in f.readlines()]

fa, fb = 16807, 48271
div = 2147483647

def update():
    global A, B
    A *= fa
    B *= fb

    A %= div
    B %= div

def match():
    global A, B

    if bin(A)[-16:] == bin(B)[-16:]:
        return True

    return False

def stack():
    global A, B

    if A % 4 == 0:
        sa.append(A)

    if B % 8 == 0:
        sb.append(B)

provided = 0

def match2():
    global sa, sb, provided

    if len(sa) > 0 and len(sb) > 0:
        output = bin(sa[0])[-16:] == bin(sb[0])[-16:]
        sa.popleft()
        sb.popleft()
        provided += 1
        return output

    return False

total = 0
total2 = 0

sa = deque()
sb = deque()

ITERS = 40000000
t = 0

for i in range(ITERS):
    update()
    total += match()

    if provided < 5000000:
        stack()
        total2 += match2()


print("Part 1:", total)
print("Part 2:", total2)























