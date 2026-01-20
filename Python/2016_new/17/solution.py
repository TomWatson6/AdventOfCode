import hashlib
from collections import deque

input = open("input.txt").read().strip()

def parse(input: str):
    return input

def hash(x):
    return hashlib.md5(x.encode()).hexdigest()

def is_open(i, x):
    x = hash(x)
    return x[i] in "bcdef"

def bfs(start, dest, h, p2):
    queue = deque([(start, "")])
    paths = []

    while queue:
        (r, c), p = queue.popleft()

        if (r, c) == dest:
            if p2:
                paths.append(len(p))
                continue
            else:
                return p

        for i, (dr, dc, ch) in enumerate([(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]):
            rr = r + dr
            cc = c + dc

            if 0 <= rr <= dest[0] and 0 <= cc <= dest[1] and is_open(i, h + p):
                queue.append(((rr, cc), p + ch))

    return paths[-1]

def part1(input: str) -> int:
    h = parse(input)

    path = bfs((0, 0), (3, 3), h, False)

    return path

def part2(input: str) -> int:
    h = parse(input)

    longest_path = bfs((0, 0), (3, 3), h, True)

    return longest_path

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















