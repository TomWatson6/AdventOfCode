from math import atan2, degrees

with open("input.txt") as f:
    input = [[c for c in r.strip()] for r in f.readlines()]

asteroids = set()

for i, r in enumerate(input):
    for j, c in enumerate(r):
        if c == '#':
            asteroids.add((j, i))

def gcd(a, b):
    if a == 0:
        return abs(b)
    if b == 0:
        return abs(a)
    while b:
        a, b = b, a % b
    return abs(a)

assert gcd(7, 14) == 7
assert gcd(8, 19) == 1
assert gcd(2, 4) == 2

total = 0
station = (0, 0)

for a in asteroids:
    S = set()

    for b in [x for x in asteroids if x != a]:
        rel_pos = (b[0] - a[0], b[1] - a[1])
        div = gcd(rel_pos[0], rel_pos[1])
        S.add((rel_pos[0] // div, rel_pos[1] // div))

    if len(S) > total:
        total = len(S)
        station = a

print("Part 1:", total)

adjusted = [(a[0] - station[0], a[1] - station[1]) for a in asteroids if a != station]
# print(adjusted)
print(station)

parts = []
parts.append([a for a in adjusted if a[0] == 0 and a[1] < 0])
parts.append([a for a in adjusted if a[0] > 0 and a[1] < 0])
parts.append([a for a in adjusted if a[0] > 0 and a[1] == 0])
parts.append([a for a in adjusted if a[0] > 0 and a[1] > 0])
parts.append([a for a in adjusted if a[0] == 0 and a[1] > 0])
parts.append([a for a in adjusted if a[0] < 0 and a[1] > 0])
parts.append([a for a in adjusted if a[0] < 0 and a[1] == 0])
parts.append([a for a in adjusted if a[0] < 0 and a[1] < 0])

for i, p in enumerate(parts):
    if i % 2 == 1:
        parts[i] = sorted(p, key=lambda x: (x[1] / x[0], x[0] + x[1]))
    else:
        parts[i] = sorted(p, key=lambda x: abs(x[0]) + abs(x[1]))

from math import atan2, pi

# Calculate angles and distances
asteroids = [(x, y, atan2(x - station[0], y - station[1]), (x - station[0])**2 + (y - station[1])**2) for x, y in asteroids]

# Sort by angle (clockwise) and distance
asteroids.sort(key=lambda a: (-a[2] % (2 * pi), a[3]))

destroyed = []
last_angle = None

while len(destroyed) < 200:
    for asteroid in asteroids:
        if asteroid[2] != last_angle:
            destroyed.append(asteroid)
            last_angle = asteroid[2]
            if len(destroyed) == 200:
                break

# Calculate the answer
x, y, _, _ = destroyed[199]
print("Part 2:", (x * 100) + y)

# # Part 2
# last = (0, 0)
# curr = 0
# destroyed = 0

# while True:
#     to_delete = []

#     for i, p in enumerate(parts[curr % len(parts)]):
#         div = gcd(p[0], p[1])
#         norm = (p[0] // div, p[1] // div)
#         if norm == last:
#             continue
#         last = norm
#         print(last)
#         to_delete.append(i)
#         destroyed += 1

#         if destroyed == 200:
#             print("Part 2:", str((p[0] + station[0]) * 100 + (p[1] + station[1])))
#             exit()

#     print(to_delete)
#     print("Before Length:", len(parts[curr % len(parts)]))
#     parts[curr % len(parts)] = [p for i, p in enumerate(parts[curr % len(parts)]) if i not in to_delete]
#     print("After Length:", len(parts[curr % len(parts)]))
#     curr += 1























