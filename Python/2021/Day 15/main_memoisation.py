
import sys

def find_shortest_path(grid, start, end, current_path, memo):
    if start == end:
        return grid[start[0]][start[1]]
    else:
        y, x = start
        path_sizes = []

        if y != end[0]:
            if memo.get(tuple([y + 1, x])) is not None:
                path_sizes.append(memo[tuple([y + 1, x])])
            else:
                temp = [x for x in current_path[0]]
                temp.append([y, x])
                temp = (temp, current_path[1] + grid[y][x])
                best = find_shortest_path(grid, [y + 1, x], end, temp, memo)
                path_sizes.append(best)
        if x != end[1]:
            if memo.get(tuple([y, x + 1])) is not None:
                path_sizes.append(memo[tuple([y, x + 1])])
            else:
                temp = [x for x in current_path[0]]
                temp.append([y, x])
                temp = (temp, current_path[1] + grid[y][x])
                best = find_shortest_path(grid, [y, x + 1], end, temp, memo)
                path_sizes.append(best)

        shortest = grid[y][x] + min(path_sizes)
        memo[tuple(start)] = shortest
        return shortest

def inflate_grid(grid, size):
    large_grid = []

    for iy in range(size):
        for y in range(len(grid)):
            row = []
            for ix in range(size):
                for x in range(len(grid[0])):
                    increment = ix + iy
                    value = grid[y][x] + increment
                    value = value if value < 10 else value - 9
                    row.append(value)
            large_grid.append(row)
    return large_grid

def p1(output):
    print("Part 1:", output)

def p2(output):
    print("Part 2:", output)

#Requires about 1000 depth of recursion to work for second half of puzzle
sys.setrecursionlimit(1500)

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

grid = []

for line in lines:
    grid.append([int(x) for x in line])

memo = dict()

shortest = find_shortest_path(grid, [0, 0], [len(grid) - 1, len(grid[0]) - 1], ([], 0), memo)

p1(shortest - grid[0][0])

memo = dict()

large_grid = inflate_grid(grid, 5)

shortest = find_shortest_path(large_grid, [0, 0], [len(large_grid) - 1, len(large_grid[0]) - 1], ([], 0), memo)

p2(shortest - large_grid[0][0])

