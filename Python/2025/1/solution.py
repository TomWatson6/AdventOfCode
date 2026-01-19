
input = open("input.txt").read().strip()

def parse(input: str):
    return input.splitlines()

def part1(input: str) -> int:
    lines = parse(input)

    curr = 50
    total = 0

    for line in lines:
        dir, mag = line[:1], int(line[1:])

        if dir == 'L':
            curr = (curr - mag) % 100
        elif dir == 'R':
            curr = (curr + mag) % 100
        else:
            exit(-1)

        if curr == 0:
            total += 1

    return total

def part2(input: str) -> int:
    lines = parse(input)

    curr = 50
    total = 0

    for line in lines:
        dir, mag = line[:1], int(line[1:])

        if dir == 'L':
            for m in range(mag):
                curr -= 1
                curr = curr % 100
                if curr == 0:
                    total += 1
        elif dir == 'R':
            for m in range(mag):
                curr += 1
                curr = curr % 100
                if curr == 0:
                    total += 1
        else:
            exit(-1)

    return total

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















