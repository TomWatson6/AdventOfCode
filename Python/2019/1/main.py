
def cost(x):
    return x // 3 - 2

def cost2(x):
    c = x // 3 - 2
    if c > 0:
        return c + cost2(c)
    return 0

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    print("Part 1:", sum(cost(int(x.strip())) for x in lines))
    print("Part 2:", sum(cost2(int(x.strip())) for x in lines))



















