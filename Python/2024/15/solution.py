from collections import deque

input = open("input.txt").read().strip()

def parse_input(input):
    chunks = input.split("\n\n")
    grid = {}
    robot = (0, 0)

    for r, row in enumerate(chunks[0].splitlines()):
        for c, ch in enumerate(row):
            grid[(r, c)] = ch
            if ch == '@':
                robot = (r, c)

    moves = chunks[1].split("\n")

    return grid, moves, robot

def parse_input2(input):
    chunks = input.split("\n\n")
    grid = {}
    robot = (0, 0)

    for r, row in enumerate(chunks[0].splitlines()):
        for c, ch in enumerate(row):
            match ch:
                case '#':
                    grid[(r, c * 2)] = ch
                    grid[(r, c * 2 + 1)] = ch
                case '@':
                    grid[(r, c * 2)] = ch
                    grid[(r, c * 2 + 1)] = '.'
                    robot = (r, c * 2)
                case '.':
                    grid[(r, c * 2)] = ch
                    grid[(r, c * 2 + 1)] = ch
                case 'O':
                    grid[(r, c * 2)] = '['
                    grid[(r, c * 2 + 1)] = ']'
                case _:
                    assert False, "invalid character in grid"

    moves = chunks[1].split("\n")

    return grid, moves, robot

DIR = {
    '<': (0, -1),
    '>': (0, 1),
    '^': (-1, 0),
    'v': (1, 0),
}

def move(robot, dir, grid):
    dir = DIR[dir]
    curr = (robot[0] + dir[0], robot[1] + dir[1])
    boxes_to_move = False

    while grid[curr] == 'O':
        curr = (curr[0] + dir[0], curr[1] + dir[1])
        boxes_to_move = True

    if grid[curr] in ['#', '@']:
        return robot

    if boxes_to_move:
        grid[curr] = 'O'

    dest = (robot[0] + dir[0], robot[1] + dir[1])

    grid[robot] = '.'
    grid[dest] = '@'

    return dest

def move2(robot, dir, grid):
    dir = DIR[dir]
    curr = (robot[0] + dir[0], robot[1] + dir[1])
    if grid[curr] == '.':
        grid[robot] = '.'
        grid[curr] = '@'
        return curr

    if grid[curr] == '#':
        return robot

    if dir[0] == 0:
        to_move = []
        while grid[curr] in ['[', ']']:
            to_move.append(curr)
            curr = (curr[0] + dir[0], curr[1] + dir[1])

        if grid[curr] == '#':
            return robot

        for m in to_move[::-1]:
            grid[(m[0] + dir[0], m[1] + dir[1])] = grid[m]

        grid[to_move[0]] = '@'
        grid[robot] = '.'
        return to_move[0]

    boxes = get_connected_boxes(curr, dir, grid)
    
    if all(grid[(x[0] + dir[0], x[1] + dir[1])] != '#' for x in boxes):
        for box in boxes:
            r, c = box

            grid[(r + dir[0], c + dir[1])] = grid[box]
            grid[(r, c)] = '.'

        grid[curr] = '@'
        grid[robot] = '.'

        return curr

    return robot

def get_connected_boxes(coord, dir, grid):
    queue = deque([coord])
    seen = set()

    while queue:
        curr = queue.popleft()

        if curr in seen:
            continue

        seen.add(curr)

        if grid[curr] == '[':
            queue.append((curr[0], curr[1] + 1))
        elif grid[curr] == ']':
            queue.append((curr[0], curr[1] - 1))

        nxt = (curr[0] + dir[0], curr[1] + dir[1])

        if grid[nxt] in ['[', ']']:
            queue.append(nxt)
            

    desc = dir[0] == 1

    return sorted(list(seen), key=lambda k: k[0], reverse=desc)

def calc_score(grid):
    total = 0
    for k, v in grid.items():
        if v in ['O', '[']:
            total += k[0] * 100 + k[1]

    return total

def part1(input: str) -> int:
    grid, moves, robot = parse_input(input)

    for move_set in moves:
        for m in move_set:
            robot = move(robot, m, grid)

    return calc_score(grid)

def part2(input: str) -> int:
    grid, moves, robot = parse_input2(input)

    for move_set in moves:
        for m in move_set:
            robot = move2(robot, m, grid)

    return calc_score(grid)

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















