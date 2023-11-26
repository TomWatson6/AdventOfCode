
with open("input.txt") as f:
    rows = [[int(t) for t in x.strip().split("\t")] for x in f.readlines()]

total = 0

for row in rows:
    upper = max(row)
    lower = min(row)
    total += upper - lower

print("Part 1:", total)

total = 0

for row in rows:
    done = False
    for a in range(len(row) - 1):
        for b in range(1, len(row)):
            if a == b:
                continue
            if row[a] / row[b] == row[a] // row[b]:
                total += row[a] // row[b]
                done = True
                break
            if row[b] / row[a] == row[b] // row[a]:
                total += row[b] // row[a]
                done = True
                break

        if done:
            break

print("Part 2:", total)


















