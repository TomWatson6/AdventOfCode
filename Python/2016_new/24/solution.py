from collections import deque

input = open("input.txt").read().strip()

G = {}
N = {}
M = {}

def parse(input: str):
    global G, N

    for r, line in enumerate(input.splitlines()):
        for c, ch in enumerate(line):
            G[(r, c)] = ch
            if ch.isnumeric():
                N[int(ch)] = (r, c)

def bfs(start, dest):
    queue = deque([(start, 0)])
    seen = set()

    while queue:
        (r, c), d = queue.popleft()

        if (r, c) == dest:
            return d

        if (r, c) in seen:
            continue

        seen.add((r, c))

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rr = r + dr
            cc = c + dc

            if (rr, cc) in G and G[(r, c)] != '#':
                queue.append(((rr, cc), d + 1))

    return 0

def dfs(start, seen, dist, ret_zero = False):
    if len(seen) == len(N):
        if ret_zero:
            return dfs(start, seen - set([0]), dist, False)

        return dist
    
    outcomes = []

    for n in [n for n in N if n not in seen]:
        outcomes.append(dfs(n, seen | set([n]), dist + M[(start, n)], ret_zero))

    return min(outcomes)

def create_graph():
    global M

    for i in range(len(N) - 1):
        for j in range(i + 1, len(N)):
            dist = bfs(N[i], N[j])
            M[(i, j)] = dist
            M[(j, i)] = dist


def part1(input: str) -> int:
    parse(input)

    create_graph()

    return dfs(0, set([0]), 0, False)

def part2(input: str) -> int:
    parse(input)

    create_graph()

    return dfs(0, set([0]), 0, True)

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















