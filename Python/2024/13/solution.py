import sympy as sym

input = open("input.txt").read().strip()
extra = 10_000_000_000_000

def parse_input(input: str) -> list[tuple[list[int], list[int], list[int]]]:
    chunks = input.split("\n\n")
    prizes = []

    for chunk in chunks:
        lines = chunk.splitlines()
        a = [3] + [int(x[1:]) for x in lines[0].split(": ")[1].split(", ")]
        b = [1] + [int(x[1:]) for x in lines[1].split(": ")[1].split(", ")]
        p = [int(x[2:]) for x in lines[2].split(": ")[1].split(", ")]
        prizes.append((a, b, p))

    return prizes

def part1(input: str) -> int:
    prizes = parse_input(input)
    total = 0

    for a, b, p in prizes:
        x, y = sym.symbols('x,y')
        eq1 = sym.Eq(a[1] * x + b[1] * y, p[0])
        eq2 = sym.Eq(a[2] * x + b[2] * y, p[1])
        result = sym.solve([eq1, eq2], (x, y))
        if len(result) == 0:
            continue
        if result[x] % 1 == 0 and result[y] % 1 == 0 and result[x] > 0 and result[y] > 0:
            total += result[x] * 3 + result[y]

    return total

def part2(input: str) -> int:
    prizes = parse_input(input)
    total = 0

    for a, b, p in prizes:
        x, y = sym.symbols('x,y')
        eq1 = sym.Eq(a[1] * x + b[1] * y, p[0] + extra)
        eq2 = sym.Eq(a[2] * x + b[2] * y, p[1] + extra)
        result = sym.solve([eq1, eq2], (x, y))
        if len(result) == 0:
            continue
        if result[x] % 1 == 0 and result[y] % 1 == 0 and result[x] > 0 and result[y] > 0:
            total += result[x] * 3 + result[y]

    return total

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















