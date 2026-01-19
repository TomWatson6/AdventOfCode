from collections import deque

input = open("input.txt").read().strip()

def parse(input: str):
    return int(input)

def is_open(number, x, y):
    val = x * x + 3 * x + 2 * x * y + y + y * y
    val += number
    val = bin(val)
    val = len([v for v in val if v == '1'])
    if val % 2 == 0:
        return True
    return False

def bfs(start, dest, number, p2):
    queue = deque([(start, 0)])
    seen = set()

    while queue:
        (x, y), d = queue.popleft()

        if d > 50 and p2:
            continue

        if (x, y) == dest and not p2:
            return d
        
        if (x, y) in seen:
            continue

        seen.add((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            xx = x + dx
            yy = y + dy

            if xx >= 0 and yy >= 0 and is_open(number, xx, yy):
                queue.append(((xx, yy), d + 1))

    return len(seen) if p2 else 0

def part1(input: str, coord: tuple[int, int]) -> int:
    number = parse(input)

    return bfs((1, 1), coord, number, False)

def part2(input: str, coord: tuple[int, int]) -> int:
    number = parse(input)

    return bfs((1, 1), coord, number, True)

if __name__ == "__main__":
    print("Part 1:", part1(input, (31, 39)))
    print("Part 2:", part2(input, (31, 39)))















