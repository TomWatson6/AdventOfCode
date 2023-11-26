
with open("simple_input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

M = {}
p2 = 0

for line in lines:
    M[line.split(" ")[0]] = 0

for line in lines:
    base, instr, val, _, cond, op, lim = line.split(" ")

    expression = f"{M[cond]} {op} {lim}"
    outcome = eval(expression)

    if outcome:
        if instr == "inc":
            M[base] += int(val)
        else:
            M[base] -= int(val)

    p2 = max(max(M.items(), key=lambda t: t[1])[1], p2)

p1 = max(M.items(), key=lambda t: t[1])[1]

print("Part 1:", p1)
print("Part 2:", p2)














