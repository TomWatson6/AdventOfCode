
def print_grid(grid):
    for y in grid:
        for x in y:
            if x == "#":
                print(x, end="")
            else:
                print(" ", end="")
        print()

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines() if x != ""]

X = 50
Y = 6

grid = [["." for _ in range(X)] for _ in range(Y)]

def evolve(grid, lines, X, Y):
    for line in lines:
        parts = line.split(" ")
        if line.startswith("rect"):
            x, y = [int(t) for t in parts[1].split("x")]
            for i in range(y):
                for j in range(x):
                    grid[i][j] = "#"
        elif line.startswith("rotate column"):
            pos = int(parts[2].strip("x="))
            curr = [x[pos] for x in grid]
            mag = int(parts[4])
            next = ["." for _ in range(Y)]

            for i, c in enumerate(curr):
                next[(i + mag) % Y] = c

            for i in range(len(grid)):
                grid[i][pos] = next[i]
        elif line.startswith("rotate row"):
            pos = int(parts[2].strip("y="))
            curr = grid[pos]
            mag = int(parts[4])
            next = ["." for _ in range(X)]

            for i, c in enumerate(curr):
                next[(i + mag) % X] = c

            grid[pos] = next
        else:
            print(f"invalid instruction: {line}")
            assert False

evolve(grid, lines, X, Y)
        
total = 0

for y in grid:
    for x in y:
        if x == "#":
            total += 1

print(f"Part 1: {total}")

print("Part 2:")
print_grid(grid)




