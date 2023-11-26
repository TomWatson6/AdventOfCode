from collections import defaultdict

with open("input.txt") as f:
    input = f.read().strip()

width = 25
height = 6
layers = len(input) // (width * height)

outcomes = {}

at = lambda l, h, w: l * width * height + h * width + w

for l in range(layers):
    totals = defaultdict(int)

    for h in range(height):
        for w in range(width):
            totals[int(input[at(l, h, w)])] += 1
            

    outcomes[totals[0]] = totals[1] * totals[2]

fewest = min(outcomes.items(), key=lambda k: k[0])[1]

print("Part 1:", fewest)
print("Part 2:")

final = ""

for h in range(height):
    for w in range(width):
        for l in range(layers):
            if input[at(l, h, w)] == "0":
                final += "0"
                break
            elif input[at(l, h, w)] == "1":
                final += "1"
                break

for h in range(height):
    o = ""
    for w in range(width):
        if final[at(0, h, w)] == "1":
            o += "#"
        else:
            o += " "
    print(o)


            



















