from collections import defaultdict

def get_neighbours(grid, current):
    neighbours = []
    for y in [-1, 0, 1]:
        for x in [-1, 0, 1]:
            if abs(y) == abs(x):
                continue
            if 0 <= current[0] + y < len(grid) and 0 <= current[1] + x < len(grid[0]):
                neighbours.append([current[0] + y, current[1] + x])
    return neighbours

def get_heuristic_value(grid, node, goal):
    y = goal[0] - node[0]
    x = goal[1] - node[1]
    return y + x

def reconstruct_path(grid, came_from, current):
    total_path = [current]
    total_distance = grid[current[0]][current[1]]

    while current in came_from.keys():
        current = came_from[tuple(current)]
        total_distance += grid[current[0]][current[1]]
        total_path.append(current)
    total_path.reverse()
    return [total_path, total_distance]

def find_path(grid, start, goal):
    open_set = set()
    open_set.add(tuple(start))

    came_from = dict()

    g_score = defaultdict(lambda: 1e9)
    g_score[tuple(start)] = 0

    f_score = defaultdict(lambda: 1e9)
    f_score[tuple(start)] = get_heuristic_value(grid, start, goal)

    while len(open_set) != 0:
        current = min(open_set, key=lambda x: f_score[x])  
        if current == tuple(goal):
            return reconstruct_path(grid, came_from, current)
      
        open_set.remove(tuple(current))
        for neighbour in [t for t in get_neighbours(grid, current) if t != current]:
            tentative_g_score = g_score[tuple(current)] + grid[neighbour[0]][neighbour[1]]
            if tentative_g_score < g_score[tuple(neighbour)]:
                came_from[tuple(neighbour)] = tuple(current)
                g_score[tuple(neighbour)] = tentative_g_score
                f_score[tuple(neighbour)] = tentative_g_score + get_heuristic_value(grid, neighbour, goal)
                if tuple(neighbour) not in open_set:
                    open_set.add(tuple(neighbour))

    return [[], -1]

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

def output_directions(path):
    left = 0
    right = 0
    up = 0
    down = 0

    for x in range(len(path) - 1):
        before = path[x]
        after = path[x + 1]
        if after[1] - before[1] > 0:
            right += 1
        elif after[1] - before[1] < 0:
            left += 1

        if after[0] - before[0] > 0:
            down += 1
        elif after[0] - before[0] < 0:
            up += 1

    print("Left:", left)
    print("Right:", right)
    print("Up:", up)
    print("Down:", down)

def p1(output):
    print("Part 1:", output)

def p2(output):
    print("Part 2:", output)

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

grid = []

for line in lines:
    grid.append([int(x) for x in line])

path = find_path(grid, [0, 0], [len(grid) - 1, len(grid[0]) - 1])

p1(path[1] - grid[0][0])

output_directions(path[0])

large_grid = inflate_grid(grid, 5)

path = find_path(large_grid, [0, 0], [len(large_grid) - 1, len(large_grid[0]) - 1])

p2(path[1] - large_grid[0][0])

output_directions(path[0])


