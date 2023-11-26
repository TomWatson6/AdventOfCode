from collections import defaultdict

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

total = 0

for line in lines:
    seen = set()
    left = line[:len(line) // 2]
    right = line[len(line) // 2:]
    [seen.add(x) for x in left]

    for x in right:
        if x in seen:
            p = 0
            if x.islower():
                p = ord(x) - ord('a') + 1
            else:
                p = ord(x) - ord('A') + 27
            total += p
            break

print("Part 1:", total)

total = 0

for i in range(0, len(lines) - 2, 3):
    seen = defaultdict(lambda: 0)

    for j in range(i, i + 3):
        S = set()
        for c in lines[j]:
            S.add(c)
        for s in S:
            seen[s] += 1

    found = [k for k, v in seen.items() if v == 3]
    assert len(found) == 1
    found = found[0]

    if found.islower():
        p = ord(found) - ord('a') + 1
    else:
        p = ord(found) - ord('A') + 27

    total += p

print("Part 2:", total)




