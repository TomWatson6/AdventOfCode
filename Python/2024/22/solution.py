from collections import defaultdict

input = open("input.txt").read().strip()

def parse_input(input):
    return [int(x) for x in input.splitlines()]

def mix(a, b):
    return a ^ b

def prune(a):
    return a % 16777216

def evolve(num):
    val = num * 64
    num = mix(num, val)
    num = prune(num)

    val = num // 32
    num = mix(num, val)
    num = prune(num)

    val = num * 2048
    num = mix(num, val)
    num = prune(num)

    return num

memo = defaultdict(int)

def find(prices, changes, a, b, c, d):
    bests = {}

    if len(memo) == 0:
        for price in prices.keys():
            vals = prices[price]
            diffs = changes[price]

            for i in range(3, len(vals)):
                change = (diffs[i - 3], diffs[i - 2], diffs[i - 1], diffs[i])
                if (price, *change) not in memo:
                    memo[(price, *change)] = vals[i]
                if change == (a, b, c, d):
                    if price not in bests:
                        bests[price] = vals[i]
                        break
    else:
        for price in prices.keys():
            bests[price] = memo[(price, a, b, c, d)]

    return bests

def part1(input: str) -> int:
    nums = parse_input(input)
    total = 0

    for num in nums:
        for _ in range(2000):
            num = evolve(num)

        total += num

    return total

def part2(input: str) -> int:
    nums = parse_input(input)
    prices = defaultdict(list)
    changes = defaultdict(list)

    for num in nums:
        n_ = int(num)
        prev = None
        for i in range(2000):
            prev = int(num)
            num = evolve(num)
            price = int(str(num)[-1])
            prices[n_].append(price)
            if i == 0:
                changes[n_].append(price - int(str(n_)[-1]))
            else:
                changes[n_].append(price - int(str(prev)[-1]))

    highest = 0

    for a in range(-9, 10):
        for b in range(-9, 10):
            for c in range(-9, 10):
                for d in range(-9, 10):
                    if abs(a + b + c + d) > 3:
                        continue
                    if a + b + c + d < 0:
                        continue
                    bests = find(prices, changes, a, b, c, d)
                    best = sum(bests.values())
                    if best > highest:
                        highest = best

    return highest

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















