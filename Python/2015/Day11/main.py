from collections import defaultdict
import time

lower = 97
upper = 122

def is_inc(s):
    chars = []

    for c in s:
        chars.append(ord(c))

    for i in range(len(chars) - 2):
        if chars[i] + 1 == chars[i + 1] and chars[i + 1] + 1 == chars[i + 2]:
            return True

    return False

def excludes(s):
    for c in s:
        if c in ["i", "o", "l"]:
            return False

    return True

def two_pairs(s):
    pairs = defaultdict(lambda: 0)
    last = ""

    for i in range(len(s) - 1):
        a = str(s[i])
        b = str(s[i + 1])
        c = a + b

        if last == c:
            continue

        last = c

        pairs[c] += 1

    matches = []

    for k, v in pairs.items():
        if k[0] == k[1]:
            matches.append(k) 

    if len(matches) >= 2:
        return True

    return False

def valid(s):
    if not is_inc(s):
        return False
    if not excludes(s):
        return False
    if not two_pairs(s):
        return False
    return True

def increment(s):
    chars = []

    for c in s:
        chars.append(ord(c))

    for i in range(len(chars) - 1, -1, -1):
        if chars[i] == 122:
            chars[i] = 97
        else:
            chars[i] += 1
            break

    output = ""

    for c in chars:
        output += chr(c)

    return output

with open("input.txt") as f:
    input = f.read().strip()

start = time.time()

while not valid(input):
    input = increment(input)

end = time.time()

print("Part 1: {} in {:.3f} seconds".format(input, end - start))

input = increment(input)

start = time.time()

while not valid(input):
    input = increment(input)

end = time.time()

print("Part 2: {} in {:.3f} seconds".format(input, end - start))
