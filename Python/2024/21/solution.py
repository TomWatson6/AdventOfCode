from collections import deque, defaultdict, Counter
from functools import cache
from itertools import product

input = open("input.txt").read().strip()

numpad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"],
]

keypad = [
    [None, "^", "A"],
    ["<", "v", ">"],
]

def find_sequences(pad):
    pos = {}
    paths = defaultdict(list)

    for r in range(len(pad)):
        for c in range(len(pad[0])):
            if pad[r][c] is None:
                continue
            pos[pad[r][c]] = (r, c)

    for a in [x for sublist in pad for x in sublist]:
        if a is None:
            continue
        for b in [x for sublist in pad for x in sublist]:
            if b is None:
                continue

            queue = deque([(pos[a], "", set())])
            best = 10**20

            while queue:
                (r, c), path, seen = queue.popleft()

                if (r, c) == pos[b] and len(path) <= best:
                    best = len(path)
                    paths[(a, b)].append(path + 'A')

                if (r, c) in seen:
                    continue

                for dr, dc, ch in [(-1, 0, '^'), (1, 0, 'v'), (0, -1, '<'), (0, 1, '>')]:
                    rr = r + dr
                    cc = c + dc

                    if rr < 0 or rr >= len(pad) or cc < 0 or cc >= len(pad[0]) or pad[rr][cc] is None:
                        continue

                    queue.append(((rr, cc), path + ch, seen | set([(r, c)])))

    return paths

num_seqs = find_sequences(numpad)
dir_seqs = find_sequences(keypad)
dir_lengths = {k: len(v[0]) for k, v in dir_seqs.items()}

@cache
def find(code, depth):
    if depth == 1:
        return sum(dir_lengths[(x, y)] for x, y in zip('A' + code, code))

    length = 0

    for a, b in list(zip('A' + code, code)):
        length += min(find(c, depth - 1) for c in dir_seqs[(a, b)])

    return length

def build_paths(code, seqs):
    possibilities = []
    code = 'A' + code

    for a, b in list(zip(code, code[1:])):
        possibilities.append(seqs[(a, b)])

    return list("".join(p) for p in product(*possibilities))

def part1(input: str) -> int:
    total = 0

    for line in input.splitlines():
        paths = build_paths(line, num_seqs)
        length = 10**20

        for p in paths:
            length = min(length, find(p, 2))

        total += length * int(line[:-1])

    return total

def part2(input: str) -> int:
    total = 0

    for line in input.splitlines():
        paths = build_paths(line, num_seqs)
        length = 10**20

        for p in paths:
            length = min(length, find(p, 25))

        total += length * int(line[:-1])

    return total

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















