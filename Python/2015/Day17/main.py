
litres = 150

with open("input.txt") as f:
    input = [(i, int(x)) for i, x in enumerate(f.readlines())]

DP = {}
OUTPUT = {}

def calculate(curr, numbers):
    if (curr, tuple(numbers)) in DP:
        return DP[(curr, tuple(numbers))]

    total = 0
    if curr == litres:
        OUTPUT[tuple(sorted([i for i in input if i not in numbers], key=lambda i: i[0]))] = True
        return 1
    if curr > litres:
        return 0
    for n in numbers:
        total += calculate(curr + n[1], [t for t in numbers if t != n])

    DP[(curr, tuple(numbers))] = total

    return total

calculate(0, input)
print("Part 1: {}".format(len(OUTPUT)))

smallest = min(OUTPUT.items(), key=lambda kv: len(kv[0]))
smallest = len(smallest[0])
print("Part 2: {}".format(len([k for k in OUTPUT.keys() if len(k) == smallest])))






