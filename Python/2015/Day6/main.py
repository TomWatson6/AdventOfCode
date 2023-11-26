from collections import defaultdict

class Square:
    def __init__(self, s):
        parts = s.split(" ")
        if len(parts) == 4:
            self.action = parts[0]
            self.lower = [int(x) for x in parts[1].split(",")]
            self.upper = [int(x) for x in parts[3].split(",")]
        else:
            self.action = parts[1]
            self.lower = [int(x) for x in parts[2].split(",")]
            self.upper = [int(x) for x in parts[4].split(",")]

    def __str__(self):
        out = "({}, {}) -> ({}, {}) == {}".format(self.lower[0], self.lower[1], self.upper[0], self.upper[1], self.action)
        return out

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    squares = [Square(line) for line in lines]

grid = defaultdict(lambda: False)

for s in squares:
    for x in range(s.lower[0], s.upper[0] + 1):
        for y in range(s.lower[1], s.upper[1] + 1):
            if s.action == "toggle":
                grid[(x, y)] = not grid[(x, y)]
            elif s.action == "on":
                grid[(x, y)] = True
            elif s.action == "off":
                grid[(x, y)] = False
            else:
                exit(-1)

total = 0

for v in grid.values():
    if v:
        total += 1

print("Part 1:", total)

grid = defaultdict(lambda: 0)

for s in squares:
    for x in range(s.lower[0], s.upper[0] + 1):
        for y in range(s.lower[1], s.upper[1] + 1):
            if s.action == "toggle":
                grid[(x, y)] += 2
            elif s.action == "on":
                grid[(x, y)] += 1
            elif s.action == "off":
                grid[(x, y)] -= 1 if grid[(x, y)] > 0 else 0
            else:
                exit(-1)

total = 0

for v in grid.values():
    total += v

print("Part 2:", total)