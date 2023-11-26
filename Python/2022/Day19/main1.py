import re

def get_blueprint(values):
    id = values[0]
    robots = [1, 0, 0, 0]
    max_spend = [0, 0, 0]

    costs = [(), (), (), ()]
    costs[0] = [(values[1], 0)] # Ore Robots
    costs[1] = [(values[2], 0)] # Clay Robots
    costs[2] = [(values[3], 0), (values[4], 1)] # Obsidian Robots
    costs[3] = [(values[5], 0), (values[6], 2)] # Geode Robots

    max_spend[0] = max(values[1], values[2], values[3], values[5])
    max_spend[1] = values[4]
    max_spend[2] = values[6]

    return id, max_spend, robots, costs

def dfs(bp, maxspend, cache, time, bots, amt):
    if time == 0:
        return amt[3]

    key = tuple([time, *bots, *amt])
    if key in cache:
        return cache[key]

    maxval = amt[3] + bots[3] * time

    for btype, recipe in enumerate(bp):
        if btype != 3 and bots[btype] >= maxspend[btype]:
            continue

        wait = 0
        for ramt, rtype in recipe:
            if bots[rtype] == 0:
                break
            wait = max(wait, -(-(ramt - amt[rtype]) // bots[rtype]))
        else:
            remtime = time - wait - 1
            if remtime <= 0:
                continue
            bots_ = bots[:]
            amt_ = [x + y * (wait + 1) for x, y in zip(amt, bots)]
            for ramt, rtype in recipe:
                amt_[rtype] -= ramt
            bots_[btype] += 1
            for i in range(3):
                amt_[i] = min(amt_[i], maxspend[i] * remtime)

            maxval = max(maxval, dfs(bp, maxspend, cache, remtime, bots_, amt_))


    cache[key] = maxval
    return maxval

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    values = [list(map(int, re.findall("\d+", x))) for x in lines]

total = 0

for i, v in enumerate(values):
    id, max_spend, robots, costs = get_blueprint(v)
    v = dfs(costs, max_spend, {}, 24, robots, [0, 0, 0, 0])
    total += (i + 1) * v

print(f"Part 1: {total}")

total = 1

for v in values[:3]:
    id, max_spend, robots, costs = get_blueprint(v)
    v = dfs(costs, max_spend, {}, 32, robots, [0, 0, 0, 0])
    total *= v

print(f"Part 2: {total}")


















































