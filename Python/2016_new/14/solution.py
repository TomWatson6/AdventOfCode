import hashlib
from functools import cache

input = open("input.txt").read().strip()

def parse(input: str):
    return input

@cache
def hash(x, times):
    for _ in range(times):
        x = hashlib.md5(x.encode()).hexdigest()

    return x

def repeating(h, amt, val = None):
    repeats = []

    prev = h[0]
    i = 0

    for ch in h:
        if ch == prev:
            i += 1
            continue

        repeats.append((prev, i))
        i = 1
        prev = ch

    repeats.append((h[-1], i))

    for ch, count in repeats:
        if count >= amt:
            if val is not None:
                if val == ch:
                    return ch
            else:
                return ch

def part1(input: str) -> int:
    salt = parse(input)
    keys = []

    i = 0

    while len(keys) < 64:
        h = hash(salt + str(i), 1)
        val = repeating(h, 3)
        if val is not None:
            for j in range(1, 1001):
                h2 = hash(salt + str(i + j), 1)
                if repeating(h2, 5, val) is not None:
                    keys.append(h)
                    break

        i += 1

    return i - 1

def part2(input: str) -> int:
    salt = parse(input)
    keys = []
    hashes = {}

    i = 0

    while len(keys) < 64:
        h = ""
        if i in hashes:
            h = hashes[i]
        else:
            h = hash(salt + str(i), 2017)
            hashes[i] = h

        val = repeating(h, 3)

        if val is not None:
            for j in range(1, 1001):
                h2 = ""
                if i + j in hashes:
                    h2 = hashes[i + j]
                else:
                    h2 = hash(salt + str(i + j), 2017)
                    hashes[i + j] = h2

                if repeating(h2, 5, val) is not None:
                    keys.append(h)
                    break

        i += 1

    return i - 1

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















