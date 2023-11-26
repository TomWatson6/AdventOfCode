import re

def hash(x, y, z, vx, vy, vz):
    return str(x) + "," + str(y) + "," + str(z) + "," + str(vx) + "," + str(vy) + "," + str(vz)

with open("input.txt") as f:
    lines = [[int(x) for x in re.findall(r"(?<=[xyz]=)([-]?\d+)", line.strip())] for line in f.readlines()]

# Pos / Vel
M = [[[x[0], x[1], x[2]], [0, 0, 0]] for x in lines]
CM = M[:]

def apply_gravity(curr):
    for m in [a for a in M if a[0] != curr[0]]:
        for i in range(3):
            if curr[0][i] < m[0][i]:
                curr[1][i] += 1
            elif curr[0][i] > m[0][i]:
                curr[1][i] -= 1

    return curr

def apply_velocity(curr):
    for i in range(3):
        curr[0][i] += curr[1][i]

    return curr

def step():
    for m in M:
        m = apply_gravity(m)

    for m in M:
        m = apply_velocity(m)

def energy():
    return sum([sum([abs(x) for x in m[0]]) * sum([abs(x) for x in m[1]]) for m in M])

# Optimisation for part 2
def lcm(a, b):
    return a * b // gcd(a, b)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm3(a, b, c):
    return lcm(lcm(a, b), c)

def find_cycle(M, i):
    start = tuple([tuple([x[0][i], x[1][i]]) for x in M])
    DP = {}
    j = 0

    while True:
        step()
        t = tuple([tuple([x[0][i], x[1][i]]) for x in M])

        if t == start:
            return j + 1

        if t in DP:
            return j - DP[t]

        DP[t] = j
        j += 1

def find_total_cycle(M):
    cycles = [find_cycle(M, i) for i in range(3)]
    return lcm3(*cycles)

DP = {}

for _ in range(1000):
    step()

print("Part 1:", energy())

M = CM[:]
output = find_total_cycle(M)
print("Part 2:", output)

   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   