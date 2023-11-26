
import time
from collections import defaultdict

def calculate(number):
    if number <= 1:
        return 1
    else:
        return number + calculate(number - 1)

def get_x(initial, time):
    x = 0
    while time > 0:
        x += initial

        if initial > 0:
            initial -= 1
        elif initial < 0:
            initial += 1
        time -= 1
    return x

def get_y(initial, time):
    y = 0
    while time > 0:
        y += initial

        initial -= 1
        time -= 1
    return y

def p1(output):
    print("Part 1:", output)

def p2(output):
    print("Part 2:", output)

start_time = time.time()

with open("input.txt") as f:
    line = f.read().strip()

line = line.strip("target area: ")
target_area = [x.strip("x=").strip("y=") for x in line.split(", ")]

x_value = 0

target_x = [int(x) for x in target_area[0].split("..")]
target_y = [int(y) for y in target_area[1].split("..")]

x_step = 1 if (sum(target_x) // 2) > 0 else -1
y_step = 1 if (sum(target_y) // 2) > 0 else -1

for x in range(0, x_step * 1000, x_step):
    x_final = calculate(x)
    if x_final >= target_x[0] and x_value == 0:
        x_value = x 
        break

y_start = abs(target_y[0]) - 1
y_max = calculate(y_start)

p1(y_max)

print("Part 1 took:", round(time.time() - start_time, 2), "seconds")
start_time = time.time()

x_times = defaultdict(set)
y_times = defaultdict(set)

for t in range(1, (y_start + 1) * 3, 1):
    for x in range(x_value, target_x[1] + 1, 1):
        hit = get_x(x, t)
        if target_x[0] <= hit <= target_x[1]:
            x_times[t].add(x)

    for y in range(target_y[0], y_start + 1, 1):
        hit = get_y(y, t)
        if target_y[0] <= hit <= target_y[1]:
            y_times[t].add(y)


points = set()
hits = 0

for t in range(1, (y_start + 1) * 3, 1):
    for sx in x_times[t]:
        for sy in y_times[t]:
            points.add((sx, sy))

hits = len(points)

for x in range(target_x[0], target_x[1] + 1, 1):
    for y in range(target_y[0], target_y[1] + 1, 1):
        points.remove((x, y))

points = list(points)
points = sorted(points, key=lambda x: x[0])

p2(hits)
 
print("Part 2 took:", round(time.time() - start_time, 2), "seconds")

