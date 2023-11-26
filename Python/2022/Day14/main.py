

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    lines = [[tuple(y.split(",")) for y in x.split(" -> ")] for x in lines]

G = set()

def init_grid(lines):
    grid = {}
    max_y = 0
    
    for line in lines:
        for i in range(len(line) - 1):
            left = (int(line[i][0]), int(line[i][1]))
            right = (int(line[i+1][0]), int(line[i+1][1]))

            sx = 0
            sy = 0

            if right[0] - left[0] > 0:
                sx = 1
            elif left[0] > right[0]:
                sx = -1

            if right[1] - left[1] > 0:
                sy = 1
            elif left[1] - right[1] > 0:
                sy = -1

            x = left[0]
            y = left[1]
            
            max_y = max(max_y, y)

            while x != right[0] or y != right[1]:
                grid[(x, y)] = True
                G.add((x, y))
                x += sx
                y += sy
        
            max_y = max(max_y, y)
            grid[(x, y)] = True

    return grid, max_y

def fall(grid, x, y, max_y):
    start = (x, y)

    while y + 1 <= max_y:
        if not grid.get((x, y + 1)):
            grid[(x, y)] = None
            y += 1
        elif not grid.get((x - 1, y + 1)):
            grid[(x, y)] = None
            x -= 1
            y += 1
        elif not grid.get((x + 1, y + 1)):
            grid[(x, y)] = None
            x += 1
            y += 1
        elif start == (x, y):
            return False
        else:
            return True

        grid[(x, y)] = True

    grid[(x, y)] = None
    return None


def simulate(grid, x, y, max_y):
    count = 0

    grid[(x, y)] = True

    while True:
        outcome = fall(grid, x, y, max_y)
        if outcome is None:
            break
        elif not outcome:
            count += 1
            break
        else:
            count += 1
    
    return count

def print_grid():
    RM = min(x[0] for x in grid)
    RS = max(x[0] for x in grid)
    CM = min(x[1] for x in grid)
    CS = max(x[1] for x in grid)

    for c in range(CM, CS + 1):
        for r in range(RM, RS + 1):
            if (r, c) in G:
                print("#", end="")
            elif (r, c) in grid:
                print(".", end="")
            else:
                print(" ", end="")
        print()
    print()


grid, max_y = init_grid(lines)
outcome = simulate(grid, 500, 0, max_y)
print("Part 1:", outcome)

grid, max_y = init_grid(lines)
floor = (max_y + 2)

for x in range(500 - floor, 500 + floor + 1, 1):
    grid[(x, floor)] = True

outcome = simulate(grid, 500, 0, floor)
print("Part 2:", outcome)












