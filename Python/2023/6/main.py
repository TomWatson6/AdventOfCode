# import cmath
import math

with open(0) as f:
    lines = [x.strip() for x in f.readlines()]

time = list(map(int, [x.strip() for x in lines[0].split()][1:]))
distance = list(map(int, [x.strip() for x in lines[1].split()][1:]))

product = 1

for t, d in zip(time, distance):
    wins = 0
    for x in range(t):
        outcome = (t - x) * x
        if outcome > d:
            wins += 1

    product *= wins

print("Part 1:", product)

time = int("".join([str(x) for x in time]))
distance = int("".join([str(x) for x in distance]))

wins = 0
for x in range(time):
    outcome = (time - x) * x
    if outcome > distance:
        wins += 1

print("Part 2:", wins)




















