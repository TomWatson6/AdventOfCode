import re
from collections import defaultdict, deque
from copy import deepcopy
import functools

def get_blueprint(values):
    id = values[0]
    robots = {
            0: 1,
            1: 0,
            2: 0,
            3: 0,
    }

    max_spend = {
            0: 0,
            1: 0,
            2: 0,
    }

    costs = {}
    costs[0] = [(0, values[1])] # Ore Robots
    costs[1] = [(0, values[2])] # Clay Robots
    costs[2] = [(0, values[3]), (1, values[4])] # Obsidian Robots
    costs[3] = [(0, values[5]), (2, values[6])] # Geode Robots

    max_spend[0] = max(values[1], values[2], values[3], values[5])
    max_spend[1] = values[4]
    max_spend[2] = values[6]

    return id, max_spend, robots, costs

def get_quality(robots, costs):
    materials = defaultdict(lambda: 0)
    print(costs)

    for _ in range(24):
        print(robots)
        # print(materials)
        for k, v in robots.items():
            materials[k] += v

        for k, v in sorted(list(costs.items()))[::-1]:
            can_afford = True
            for c in v:
                if materials[c[0]] < c[1]:
                    can_afford = False
                    break

            if can_afford:
                for c in v:
                    materials[c[0]] -= c[1]

                robots[k] += 1

    print(robots)

    return id * robots[3]

def add_robot(robots, r):
    new_robots = deepcopy(robots)
    new_robots[r] += 1
    return new_robots

def deduct(materials, costs, r):
    new_materials = deepcopy(materials)
    for k, v in costs[r]:
        new_materials[k] -= v

    return new_materials

def affordable(r, costs, materials):
    for k, v in costs[r]:
        if materials[k] < v:
            return False

    return True

def at_max_spend(max_spend, materials):
    for k, v in max_spend.items():
        if materials[k] < v:
            return False

    return True

DP = {}
best = {}
best_geodes = 0

def search(robots, costs, materials, max_spend, time):
    global best, best_geodes
    # DFS
    if time == 0:
        if materials[3] > best_geodes:
            best_geodes = materials[3]
            best = materials
        return materials[3]

    key = (tuple(robots), tuple(materials), time)
    if key in DP:
        return DP[key]

    # Increase the amount of materials based on the number of robots currently working
    for k, v in robots.items():
        materials[k] += v

    BEST = []

    # Consider all actions based on materials we have, including "do nothing" and decrement time action
    for r in robots.keys():
        if affordable(r, costs, materials):
            new_robots = add_robot(robots, r)
            new_materials = deduct(materials, costs, r)
            outcome = search(new_robots, costs, new_materials, max_spend, time - 1)
            # DP[(tuple(new_robots), tuple(costs), tuple(new_materials), time - 1)] = outcome
            BEST.append(outcome)

    if not at_max_spend(max_spend, materials):
        outcome = search(deepcopy(robots), costs, deepcopy(materials), max_spend, time - 1)
        BEST.append(outcome)
        # DP[(tuple(robots), tuple(costs), tuple(materials), time - 1)] = outcome

    final = max(BEST)
    DP[key] = final
    return final

with open("simple_input.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    values = [list(map(int, re.findall("\d+", x))) for x in lines]

C = {}

for v in values:
    id, max_spend, robots, costs = get_blueprint(v)
    print(id, max_spend, robots, costs)
    materials = defaultdict(lambda: 0)

    C[id] = search(robots, costs, materials, max_spend, 24)
    print(best_geodes, best)
    best = {}
    best_geodes = 0

print(C)













