
with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

def gcd(x, y):
   while y:
       x, y = y, x % y
   return x

def lcm(x, y):
   lcm = (x * y) // gcd(x, y)
   return lcm

bus_times = [(int(x[1]), x[0]) for x in enumerate(lines[1].split(",")) if x[1] != 'x']

inc = bus_times[0][0]
bus_times.pop(0)
time = 0

while len(bus_times) > 0:
    next_bus = bus_times.pop()
    bus_time, offset = next_bus

    while (time + offset) % bus_time != 0:
        time += inc

    inc = lcm(inc, bus_time)

print(f"Part 2: {time}")










