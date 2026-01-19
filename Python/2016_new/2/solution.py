
input = open("input.txt").read().strip()

def parse(input: str):
    return input.splitlines()

numpad = """123
456
789""".splitlines()

numpad2 = """  1  
 234 
56789
 ABC 
  D  """.split("\n")

def part1(input: str) -> int:
    lines = parse(input)
    digits = ""
    r = 1
    c = 1

    for line in lines:
        for ch in line:
            match ch:
                case 'L':
                    c = max(c - 1, 0)
                case 'R':
                    c = min(c + 1, 2)
                case 'U':
                    r = max(r - 1, 0)
                case 'D':
                    r = min(r + 1, 2)

        digits += numpad[r][c]

    return int(digits)

def part2(input: str) -> int:
    lines = parse(input)
    digits = ""
    r = 2
    c = 0

    def check(r, c):
        return 0 <= r < len(numpad2) and 0 <= c < len(numpad2[0]) and numpad2[r][c] != ' '

    for line in lines:
        for ch in line:
            match ch:
                case 'L':
                    if check(r, c - 1):
                        c -= 1
                case 'R':
                    if check(r, c + 1):
                        c += 1
                case 'U':
                    if check(r - 1, c):
                        r -= 1
                case 'D':
                    if check(r + 1, c):
                        r += 1

        digits += numpad2[r][c]

    return digits

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















