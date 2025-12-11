from collections import deque
from functools import cache

input = open("input.txt").read().strip()

def parse(input: str):
    lines = input.splitlines()
    lines = [l.split(": ") for l in lines]
    lines = {l[0]: l[1].split() for l in lines}

    return lines

def find(node):
    queue = deque([node])
    total = 0

    while queue:
        curr = queue.popleft()

        if curr == "out":
            total += 1
            continue

        if curr in wires:
            for wire in wires[curr]:
                queue.append(wire)

    return total

wires = {}

@cache
def find2(node, seen_dac, seen_fft):
    if node == "out":
        return 1 if seen_dac and seen_fft else 0

    total = 0

    for dest in wires[node]:
        new_seen_dac = seen_dac or dest == "dac"
        new_seen_fft = seen_fft or dest == "fft"
        total += find2(dest, new_seen_dac, new_seen_fft)

    return total

def part1(input: str) -> int:
    global wires
    wires = parse(input)

    paths = find("you")

    return paths

def part2(input: str) -> int:
    global wires
    wires = parse(input)

    total = find2("svr", False, False)

    return total

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















