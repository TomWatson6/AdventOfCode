

def init_fuel_costs(max):
    fuel_costs = dict()
    total = 0
    for x in range(max + 1):
        total += x
        fuel_costs[x] = total
    return fuel_costs

def p1(output):
    print("Part 1:", output)

def p2(output):
    print("Part 2:", output)

with open("input.txt") as f:
    subs = [int(x) for x in f.read().split(",")]

smallest = 99999999

for x in range(min(subs), max(subs) + 1, 1):
    total = 0

    for sub in subs:
        fuel = abs(sub - x)
        total += fuel

    if total < smallest:
        smallest = total

p1(smallest)

smallest = 99999999
fuel_costs = init_fuel_costs(max(subs) - min(subs))

for x in range(min(subs), max(subs) + 1, 1):
    total = 0

    for sub in subs:
        distance = abs(sub - x)
        fuel = fuel_costs[distance]
        total += fuel

    if total < smallest:
        smallest = total

p2(smallest)