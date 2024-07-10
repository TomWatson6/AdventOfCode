
with open(0) as f:
    n = int(f.read().strip())

ITERS = 2017
ITERS2 = 50000000

def solve():
    pos = 0
    total = 1

    for i in range(1, ITERS2 + 1):
        pos = (pos + n) % total
        pos += 1
        if pos == 1:
            ans = i
        total += 1

    return ans

LL = {0: 0}
curr = 0

for i in range(ITERS):
    for _ in range(n):
        curr = LL[curr]

    LL[i + 1] = LL[curr]
    LL[curr] = i + 1
    curr = LL[curr]

    if i % 100000 == 0:
        print(i)

print("Part 1:", LL[2017])
print("Part 2:", solve())






















