import re

with open(0) as f:
    row, column = list(map(int, re.findall(r"\d+", f.read().strip())))

row -= 1
column -= 1

def next(n):
    n *= 252533
    n %= 33554393
    return n

def get(row, column):
    n = 20151125
    curr = 0
    r = 0
    c = 0

    while (r, c) != (row, column):
        if c == curr:
            curr += 1
            r = curr
            c = 0
        else:
            r -= 1
            c += 1

        n = next(n)

    return n

print(get(row, column))




















