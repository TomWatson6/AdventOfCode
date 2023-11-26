import re
from copy import deepcopy
import sys
from collections import deque

sys.setrecursionlimit(99999999)

    

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

F = {}
M = {}

for line in lines:
    p = re.findall("[A-Z]{2}|(?<=\=)\d+", line)
    M[p[0]] = p[2:]
    F[p[0]] = int(p[1])

'''
    SOLUTION

    if all visited, return remaining depth
    when reaching the end return 0
    at each level return find(...) + sum([M[x] for x in visited])

'''

start = 'AA'
MAX_DEPTH = 30
T = (0, [])
DP = {}

def reconstruct_path(C, start, end):
    path = [start]

    x = start

    while x != end:
        path.append(C[x])
        x = C[x]

    return path[::-1]


def find_route(start, dest):
    Q = deque([start])
    C = {}

    V = set()
    while len(Q) > 0:
        node = Q.popleft()
        V.add(node)

        for adj in M[node]:
            if adj not in V:
                C[adj] = node
                Q.append(adj)
            if adj == dest:
                return reconstruct_path(C, dest, start)


def find_routes(nodes):
    X = {}

    for node in nodes:
        for dest in [n for n in nodes if n != node]:
            X[(node, dest)] = find_route(node, dest)

    return X

NODES = [k for k, v in F.items() if v != 0 or k == 'AA']
R = find_routes(NODES)

def find_best(curr, visited, depth):
    if depth <= 5:
        print("working")

    visited.add(curr)

    if depth >= MAX_DEPTH:
        return 0
        # return (max depth - moves + 2) * F[curr]

    N = []
    for n in [x for x in NODES if x not in visited]:
        path = R[(curr, n)]
        N.append(find_best(n, deepcopy(visited), depth + len(path) - 1))

    output = max(N) + (MAX_DEPTH - depth - 2) * F[curr] if len(N) > 0 else 0
    return output


def find(curr, depth, visited, path):
    path.append(curr)
    # print(path)

    if (curr, tuple(sorted(list(visited)))) in DP:
        return DP[(curr, tuple(sorted(list(visited))))]

    if curr not in visited:
        if F[curr] != 0:
            depth += 1

    visited.add(curr)

    if depth >= MAX_DEPTH:
        return 0

    VALUES = []

    for next in M[curr]:
        found = find(next, depth + 1, deepcopy(visited), deepcopy(path))
        DP[(curr, tuple(sorted(list(visited))))] = found
        VALUES.append(found)

    first = path.index(curr)
    val = max(VALUES) + (depth - first + 1) * F[curr]
    return val


    


def explore(curr, depth, total, visited, path):
    global T
    path.append(curr)

    # if len(path) > 16:
    #     for i in range(8, len(path), 2):
    #         if path[len(path)-i*2:][:i] == path[len(path)-i*2:][i:] or path[len(path)-i*2:][:i] == path[len(path)-i*2:][:i][::-1]:
    #             return

    is_open = False

    if depth == 4:
        print("At depth 4")

    if curr not in visited:
        visited.add(curr)
        total += (MAX_DEPTH - depth) * F[curr]
    else:
        is_open = True

    # if (curr, depth, tuple(list(visited))) in DP:
    #     T.append(DP[(curr, depth, tuple(sorted(list(visited))))] + total)

    if depth >= MAX_DEPTH:
        # DP[(curr, depth, tuple(sorted(list(visited))))] = total
        # T.append((total, path))
        T = max(T, (total, path), key=lambda k: k[0])
        return

    for next in M[curr]:
        # dd = 1 if is_open else 2
        explore(next, depth + 2, deepcopy(total), deepcopy(visited), deepcopy(path))

# explore(start, 0, 0, set(), [])
# print(T)

# output = find(start, 0, set(), [])
# print(output)
# print(len([x for x in F.values() if x != 0]))

routes = find_routes([k for k, v in F.items() if v != 0])

print(routes)
print(len(routes))
# print(find_best(start, set(), 0))
print(min(R.values(), key=lambda r: len(r)))
print(max(R.values(), key=lambda r: len(r)))
print(find_best(start, set(), 0))










