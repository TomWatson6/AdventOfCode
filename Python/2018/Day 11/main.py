

serial_number = 2568

def power_level(x, y):
    rack = x + 10
    power = rack * y
    power += serial_number
    power *= rack
    power = int(str(power)[-3])
    power -= 5
    return power

grid = {}

for x in range(1, 301):
    for y in range(1, 301):
        grid[(x, y)] = power_level(x, y)

largest = 0
largest_coord = (0, 0)
largest_dim = 0

for x in range(1, 299):
    for y in range(1, 299):
        total = 0
        for xx in range(x, x + 3):
            for yy in range(y, y + 3):
                total += grid[(xx, yy)]
        if total > largest:
            largest = total
            largest_coord = (x, y)

print(f"Part 1: {largest_coord[0]},{largest_coord[1]}")

largest = 0
largest_coord = (0, 0)
largest_dim = 0

for x in range(1, 301):
    for y in range(1, 301):
        offset = min(300 - x, 300 - y, 20) + 1
        for add in range(1, offset + 1):
            total = 0
            for xx in range(x, x + add):
                for yy in range(y, y + add):
                    total += grid[(xx, yy)]
            
            if total > largest:
                largest = total
                largest_coord = ((x, y))
                largest_dim = add

print(f"Part 2: {largest_coord[0]},{largest_coord[1]},{largest_dim}")
















