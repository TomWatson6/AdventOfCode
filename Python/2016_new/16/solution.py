from functools import cache

input = open("input.txt").read().strip()

def parse(input: str):
    return input

def generate(a):
    b = str(a)
    b = b[::-1]
    b = "".join(['1' if x == '0' else '0' for x in b])
    return a + '0' + b

@cache
def checksum(binary):
    if len(binary) == 2:
        return '1' if binary[0] == binary[1] else '0'

    if (len(binary) // 2) % 2 == 0:
        return checksum(binary[:len(binary) // 2]) + checksum(binary[len(binary) // 2:])

    return checksum(binary[:len(binary) // 2 - 1]) + checksum(binary[len(binary) // 2 - 1:])

def part1(input: str) -> int:
    a = parse(input)
    length = 272

    while True:
        a = generate(a)
        if len(a) >= length:
            break

    a = a[:length]
    check = a

    while len(check) % 2 == 0:
        check = checksum(check)

    return check

def part2(input: str) -> int:
    a = parse(input)
    length = 35651584

    while True:
        a = generate(a)
        if len(a) >= length:
            break

    a = a[:length]
    check = a

    while len(check) % 2 == 0:
        check = checksum(check)

    return check

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















