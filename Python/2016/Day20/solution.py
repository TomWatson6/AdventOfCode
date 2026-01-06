
input = open("input.txt").read()

UPPER = 4294967295

def part1(input: str) -> int:
    lines = [[int(t) for t in x.strip().split("-")] for x in input.split("\n") if x != '']
    lines = sorted(lines, key = lambda k: (k[0], k[1]))
    lines = [range(lower, upper) for lower, upper in lines]

    for a in lines:
        if all(a.stop + 1 not in line for line in lines):
            return a.stop
            
    return 0

def combine(l1, l2):
    lower1, upper1 = l1
    lower2, upper2 = l2

    # 1 engulfs 2
    if lower1 <= lower2 <= upper2 <= upper1:
        return [l1]

    # 2 engulfs 1
    if lower2 <= lower1 <= upper1 <= upper2:
        return [l2]

    if lower1 <= lower2 <= upper1 <= upper2:
        return [[lower1, upper2]]

    if lower2 <= lower1 <= upper2 <= upper1:
        return [[lower2, upper1]]

    if lower1 <= upper1 < lower2 <= upper2:
        return [l1, l2]

    if lower2 <= upper2 < lower1 <= upper1:
        return [l2, l1]

def part2(input: str) -> int:
    blacklists = [[int(t) for t in x.strip().split("-")] for x in input.splitlines() if x != '']
    changed = True

    while changed:
        blacklists = sorted(blacklists)
        changed = False

        for i in range(len(blacklists) - 1):
            for j in range(i + 1, len(blacklists)):
                combined = combine(blacklists[i], blacklists[j])

                if len(combined) < 2:
                    changed = True
                    blacklists.remove(blacklists[j])
                    blacklists.remove(blacklists[i])
                    blacklists.append(combined[0])
                    break

            if changed:
                break

    ans = 0

    for (l1, u1), (l2, u2) in list(zip(blacklists, blacklists[1:])):
        assert u1 < l2
        ans += l2 - u1 - 1

    return ans

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))



















