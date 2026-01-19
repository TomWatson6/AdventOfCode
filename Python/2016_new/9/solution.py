
input = open("input.txt").read().strip()

def parse(input: str):
    return input

def decompress(s, p2):
    if '(' not in s:
        return len(s)

    total = 0

    while '(' in s:
        total += s.find('(')

        s = s[s.find('('):]
        marker = s[1:s.find(')')].split('x')
        s = s[s.find(')') + 1:]

        if p2:
            total += decompress(s[:int(marker[0])], p2) * int(marker[1])
        else:
            total += len(s[:int(marker[0])]) * int(marker[1])

        s = s[int(marker[0]):]

    total += len(s)

    return total

def part1(input: str) -> int:
    data = parse(input)

    return decompress(data, False)

def part2(input: str) -> int:
    data = parse(input)

    return decompress(data, True)

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















