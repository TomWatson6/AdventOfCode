from collections import deque, defaultdict as dd

input = open("input.txt").read().strip()

def parse(input: str):
    lines = input.splitlines()
    orbits = {}

    for left, right in [x.split(')') for x in lines]:
        orbits[right] = left

    return orbits

def checksum(orbits):
    total = 0

    for orbit in orbits.keys():
        while orbit in orbits:
            total += 1
            orbit = orbits[orbit]

    return total

def transfers(orbits, a, b):
    a_orbits = {}
    i = 0

    while a in orbits:
        a_orbits[orbits[a]] = i
        i += 1
        a = orbits[a]

    b_orbits = {}
    i = 0

    while b in orbits:
        b_orbits[orbits[b]] = i
        i += 1
        b = orbits[b]

    for a in a_orbits.keys():
        if a in b_orbits:
            return a_orbits[a] + b_orbits[a]

    return 0

def part1(input: str) -> int:
    orbits = parse(input)

    return checksum(orbits)

def part2(input: str) -> int:
    orbits = parse(input)

    return transfers(orbits, "YOU", "SAN")

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















