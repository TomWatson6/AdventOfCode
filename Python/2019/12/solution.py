from math import lcm

input = open("input.txt").read().strip()

def parse(input: str):
    moons = []

    for x, y, z in [line[1:-1].split(", ") for line in input.splitlines()]:
        x = int(x[2:])
        y = int(y[2:])
        z = int(z[2:])

        moons.append((x, y, z, 0, 0, 0))

    return moons

def step(moons):
    new_moons = []

    for m1 in moons:
        dx = 0
        dy = 0
        dz = 0

        for m2 in [m for m in moons if m != m1]:
            dx += 1 if m2[0] > m1[0] else 0 if m2[0] == m1[0] else -1
            dy += 1 if m2[1] > m1[1] else 0 if m2[1] == m1[1] else -1
            dz += 1 if m2[2] > m1[2] else 0 if m2[2] == m1[2] else -1

        new_moons.append((m1[0], m1[1], m1[2], m1[3] + dx, m1[4] + dy, m1[5] + dz))

    for i in range(len(new_moons)):
        m = new_moons[i]
        new_moons[i] = (m[0] + m[3], m[1] + m[4], m[2] + m[5], m[3], m[4], m[5])

    return new_moons

def potential_energy(moons):
    total = 0

    for m in moons:
        total += (abs(m[0]) + abs(m[1]) + abs(m[2])) * (abs(m[3]) + abs(m[4]) + abs(m[5]))

    return total

def part1(input: str) -> int:
    moons = parse(input)

    for _ in range(1000):
        moons = step(moons)

    return potential_energy(moons)

def part2(input: str) -> int:
    moons = parse(input)
    moons_copy = list(moons)

    M = []
    M.append([x[0] for x in moons])
    M.append([x[1] for x in moons])
    M.append([x[2] for x in moons])

    cycles = []
    
    for i in range(3):
        count = 1
        moons = list(moons_copy)

        while any(M[i][j] != moons[j][i] for j in range(len(moons))) or count == 1:
            moons = step(moons)
            count += 1

        cycles.append(count)

    return lcm(*cycles)

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















