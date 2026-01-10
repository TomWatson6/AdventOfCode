from copy import deepcopy
from collections import deque
from heapq import heappush, heappop

input = open("input.txt").read().strip()

total_keys = 0

def parse(input: str):
    global total_keys
    total_keys = 0
    grid = [list(line) for line in input.splitlines()]
    starts = []

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '@':
                starts.append((r, c))

            if grid[r][c] not in ['#', '.', '@'] and grid[r][c].islower():
                total_keys += 1

    return grid, starts

def bfs(grid, start, dest):
    queue = deque([(start, 0, set(), set())])
    seen = set()

    while queue:
        (r, c), d, keys, gates = queue.popleft()

        if (r, c) in seen:
            continue

        seen.add((r, c))

        if grid[r][c].isalpha():
            if grid[r][c].islower():
                keys.add(grid[r][c])
            else:
                gates.add(grid[r][c])

        if (r, c) == dest:
            return d, keys, gates

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rr = r + dr
            cc = c + dc

            if 0 <= rr < len(grid) and 0 <= cc < len(grid[0]) and grid[rr][cc] != '#':
                new_keys = deepcopy(keys)
                new_gates = deepcopy(gates)

                queue.append(((rr, cc), d + 1, new_keys, new_gates))

    return 0, set(), set()

def dijkstras(graph, start):
    queue = []
    heappush(queue, (0, start, set()))

    while queue:
        depth, key, seen = heappop(queue)

        if len(seen) == total_keys:
            return depth

        for (_, b), (d, k, g) in [(k, v) for k, v in graph.items() if k[0] == key and k[1] not in seen and k[1] != '@']:
            new_keys = seen | k
            if all(x.lower() in new_keys for x in g):
                if any(q[0] <= depth + d and q[1] == b and q[2] == new_keys for q in queue):
                    continue

                heappush(queue, (depth + d, b, new_keys))

    return 0

def dijkstras2(graph, s1, s2, s3, s4):
    queue = []
    heappush(queue, (0, s1, s2, s3, s4, set()))

    while queue:
        depth, k1, k2, k3, k4, seen = heappop(queue)

        if len(seen) == total_keys:
            return depth

        for (a, b), (d, k, g) in [(k, v) for k, v in graph.items() if k[0] in [k1, k2, k3, k4] and k[1] not in seen and k[1] not in [s1, s2, s3, s4]]:
            new_keys = seen | k
            if all(x.lower() in new_keys for x in g):
                if a == k1 and not any(q[0] <= depth + d and b == q[1] and k2 == q[2] and k3 == q[3] and q[4] == k4 and q[5] == new_keys for q in queue):
                    heappush(queue, (depth + d, b, k2, k3, k4, new_keys))
                elif a == k2 and not any(q[0] <= depth + d and k1 == q[1] and b == q[2] and k3 == q[3] and k4 == q[4] and q[5] == new_keys for q in queue):
                    heappush(queue, (depth + d, k1, b, k3, k4, new_keys))
                elif a == k3 and not any(q[0] <= depth + d and k1 == q[1] and k2 == q[2] and b == q[3] and k4 == q[4] and q[5] == new_keys for q in queue):
                    heappush(queue, (depth + d, k1, k2, b, k4, new_keys))
                elif a == k4 and not any(q[0] <= depth + d and k1 == q[1] and k2 == q[2] and k3 == q[3] and b == q[4] and q[5] == new_keys for q in queue):
                    heappush(queue, (depth + d, k1, k2, k3, b, new_keys))

    return 0

def get_keys(grid):
    keys = []
    starts = []

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c].isalpha() and grid[r][c].islower() or grid[r][c] == '@':
                keys.append((r, c))
                if grid[r][c] == '@':
                    starts.append((r, c))

    return keys, starts

def make_graph(grid):
    graph = {}
    keys, starts = get_keys(grid)
    M = {}

    if len(starts) > 1:
        for i, s in enumerate(starts):
            M[s] = str(i)

    for a in range(len(keys) - 1):
        for b in range(a + 1, len(keys)):
            dist, keys_found, gates_found = bfs(grid, keys[a], keys[b])

            if dist == 0:
                continue

            r1, c1 = keys[a]
            r2, c2 = keys[b]

            ch1 = grid[r1][c1]
            ch2 = grid[r2][c2]

            if len(starts) > 1:
                if keys[a] in M:
                    ch1 = M[keys[a]]
                if keys[b] in M:
                    ch2 = M[keys[b]]

            graph[(ch1, ch2)] = (dist, keys_found, gates_found)
            graph[(ch2, ch1)] = (dist, keys_found, gates_found)

    return graph

def part1(input: str) -> int:
    grid, _ = parse(input)

    graph = make_graph(grid)
    dist = dijkstras(graph, '@')

    return dist

def part2(input: str) -> int:
    grid, starts = parse(input)

    if len(starts) == 1:
        r, c = starts[0]

        for dr in range(-1, 2):
            for dc in range(-1, 2):
                rr = r + dr
                cc = c + dc

                if abs(dr) == abs(dc) and not dr == dc == 0:
                    grid[rr][cc] = '@'
                else:
                    grid[rr][cc] = '#'

    graph = make_graph(grid)
    dist = dijkstras2(graph, '0', '1', '2', '3')

    return dist

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















