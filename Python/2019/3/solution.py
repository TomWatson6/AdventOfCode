
input = open("input.txt").read().strip()

def man_dist(a):
    return abs(a[0]) + abs(a[1])

def parse(input: str):
    return [x.split(',') for x in input.splitlines()]

def visited(wire):
    curr = (0, 0)
    V = {}
    V[0] = curr
    steps = 0

    for w in wire:
        dir_, mag = w[0], int(w[1:])

        for m in range(mag):
            match dir_:
                case 'U': curr = (curr[0], curr[1] - 1)
                case 'D': curr = (curr[0], curr[1] + 1)
                case 'L': curr = (curr[0] - 1, curr[1])
                case 'R': curr = (curr[0] + 1, curr[1])

            steps += 1

            V[steps] = curr

    return V

def part1(input: str) -> int:
    wires = parse(input)

    A = set(visited(wires[0]).values())
    B = set(visited(wires[1]).values())
    
    col = A & B

    return min(man_dist(c) for c in col if c != (0, 0))

def part2(input: str) -> int:
    wires = parse(input)

    AV = {b: a for a, b in visited(wires[0]).items()}
    BV = {b: a for a, b in visited(wires[1]).items()}

    A = set(AV.keys())
    B = set(BV.keys())

    col = A & B

    return min(AV[c] + BV[c] for c in col if c != (0, 0))

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















