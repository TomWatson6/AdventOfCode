from collections import defaultdict

forbidden = ["ab", "cd", "pq", "xy"]

def contains_vowels(s, n):
    num = 0
    for c in s:
        if c in ["a", "e", "i", "o", "u"]:
            num += 1

    return num >= n

def double_letter(s):
    last = ""
    for c in s:
        if c == last:
            return True
        last = c

    return False

def excludes_forbidden(s):
    for i in range(len(s) - 1):
        check = str(s[i]) + str(s[i + 1])
        if check in forbidden:
            return False

    return True

def sandwiches(s):
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            return True

    return False

def has_two_pairs(s):
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

    for i in pairs.values():
        if i >= 2:
            return True

    return False


with open("input.txt") as f:
    strings = [x.strip() for x in f.readlines()]

nice = 0

for s in strings:
    if not contains_vowels(s, 3):
        continue
    if not double_letter(s):
        continue
    if not excludes_forbidden(s):
        continue
    nice += 1

print("Part 1:", str(nice))

nice = 0

for s in strings:
    if not has_two_pairs(s):
        continue
    if not sandwiches(s):
        continue
    nice += 1

print("Part 2:", str(nice))