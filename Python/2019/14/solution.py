from math import ceil
from collections import defaultdict, deque

input = open("input.txt").read().strip()

recipes = {}
output_counts = {}

def parse(input: str):
    global recipes, output_counts

    for ingreds, output in [x.split(" => ") for x in input.splitlines()]:
        ingreds = [(b, int(a)) for a, b in [x.split() for x in ingreds.split(", ")]]
        count, output = output.split()
        recipes[output] = ingreds
        output_counts[output] = int(count)

    return recipes, output_counts

def bfs(product, count):
    required = defaultdict(lambda: 0)
    amounts = defaultdict(lambda: 0)

    queue = deque([(product, count)])

    while queue:
        ingred, amount = queue.popleft()

        required[ingred] += amount

        if ingred == "ORE":
            continue

        n = ceil((required[ingred] - amounts[ingred]) / output_counts[ingred])
        amounts[ingred] += output_counts[ingred] * n

        for p, c in recipes[ingred]:
            queue.append((p, n * c))

    return required["ORE"]

def part1(input: str) -> int:
    recipes, output_counts = parse(input)

    required = bfs("FUEL", 1)

    return required

def part2(input: str) -> int:
    recipes, output_counts = parse(input)

    low = 0
    high = 1_000_000_000_000
    target = 1_000_000_000_000

    while low <= high:
        mid = low + ((high - low) // 2)
        req = bfs("FUEL", mid)
        if req < target:
            low = mid + 1
        elif req > target:
            high = mid - 1
        else:
            return mid

    return mid - 1 if bfs("FUEL", mid) > target else mid

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















