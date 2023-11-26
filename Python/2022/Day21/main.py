

with open("input.txt") as f:
    lines = [x.strip().split(": ") for x in f.readlines()]

M = {}

for line in lines:
    M[line[0]] = line[1]
    
def resolve(exp):
    parts = exp.split(" ")
    if len(parts) == 1:
        return int(parts[0])

    assert len(parts) == 3

    left = resolve(M[parts[0]])
    right = resolve(M[parts[2]])

    return eval(f"{left} {parts[1]} {right}")

print("Part 1:", int(resolve(M["root"])))

parts = M["root"].split(" ")
M["root"] = f"{parts[0]} - {parts[2]}"

low = 0
high = int(1e20)
result = int(1e20)

while result != 0:
    i = (high + low) // 2
    M["humn"] = str(i)
    result = resolve(M["root"])
    if result > 0:
        low = i + 1
    elif result < 0:
        high = i - 1
    else:
        print("Part 2:", i)
        break




