
input = open("input.txt").read().strip()

def parse(input: str):
    lines = input.splitlines()
    batteries = [[int(x) for x in b] for b in lines]
    return batteries

def largest(battery: str, count: int):
    biggest = ""
    c = 0

    for i in range(count - 1, -1, -1):
        segment = battery[c:len(battery) - i]
        l = max([int(x) for x in segment])
        ind = segment.index(str(l))
        biggest += segment[ind]
        c += ind + 1

    return int(biggest)

def part1(input: str) -> int:
    batteries = parse(input)
    biggest = [largest("".join([str(b) for b in battery]), 2) for battery in batteries]

    return sum(biggest)

def part2(input: str) -> int:
    batteries = parse(input)
    biggest = [largest("".join([str(b) for b in battery]), 12) for battery in batteries]

    return sum(biggest)

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















