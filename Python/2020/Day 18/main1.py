
def evaluate(expr):
    output = 0

    expr = expr.split(" ")
    if len(expr) == 1:
        return eval(expr)

    while len(expr) != 1:
        a = expr.pop(0)
        op = expr.pop(0)
        b = expr.pop(0)
        output = eval(f"{a}{op}{b}")
        expr = [output] + expr

    return output

def evaluate2(expr):
    output = 0

    expr = expr.split(" * ")
    if len(expr) == 1:
        return eval(expr[0])

    for i in range(len(expr)):
        expr[i] = eval(expr[i])

    expr = " * ".join([str(x) for x in expr])
    return eval(expr)


def solve(expr, p2):
    final = ""
    depth = 0

    for i in range(len(expr)):
        if expr[i] == '(':
            if depth == 0:
                start = i + 1
            depth += 1
        if expr[i] == ')':
            depth -= 1
            if depth == 0:
                final += str(solve(expr[start:i], p2))
                continue
        if depth == 0:
            final += expr[i]

    if not p2:
        return evaluate(final)
    return evaluate2(final)

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

total = 0
total2 = 0

for line in lines:
    total += solve(line, False)
    total2 += solve(line, True)

print(f"Part 1: {total}")
print(f"Part 2: {total2}")
























