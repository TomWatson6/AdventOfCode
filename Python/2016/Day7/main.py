import re

def abba(input):
    sections = set()

    for i in range(len(input) - 3):
        sections.add(input[i:i + 4])

    for section in sections:
        seq = []

        for i in range(len(section)):
            seq.append(section[i]) 
            if len(section[i:]) >= len(seq):
                if "".join(seq[::-1]) != section[len(section) - len(seq):]:
                    break
            elif len(set(seq[:len(seq) - 1])) == len(seq[:len(seq) - 1]):
                return True
            else:
                break

    return False

def aba(input):
    sections = set()

    for i in range(len(input) - 2):
        sections.add("".join(input[i:i + 3]))

    abas = set()

    for section in sections:
        for i in range(len(section) - 2):
            if section[i] == section[i + 2] and section[i] != section[i + 1]:
                abas.add("".join(section[i:i + 3]))

    return abas

def bab(input, abas):
    for a in abas:
        b = a[1] + a[0] + a[1]
        if b in input:
            return True

    return False

def supports(s):
    left = re.findall("\w+(?=\[)", s)
    right = re.findall("(?<=\])\w+", s)
    middle = re.findall("(?<=\[)\w+(?=\])", s)

    s_left = []
    s_right = []
    s_middle = []

    for l in left:
        s_left.append(abba(l))

    for r in right:
        s_right.append(abba(r))

    for m in middle:
        s_middle.append(abba(m))

    s_left = any(s_left)
    s_right = any(s_right)
    s_middle = any(s_middle)

    if s_left or s_right:
        return not s_middle    

    return False

def supports2(s):
    left = re.findall("\w+(?=\[)", s)
    right = re.findall("(?<=\])\w+", s)
    middle = re.findall("(?<=\[)\w+(?=\])", s)

    abas = set()

    for l in left:
        [abas.add(x) for x in aba(l)]

    for r in right:
        [abas.add(x) for x in aba(r)]

    return any([bab(x, abas) for x in middle])


assert supports("abba[mnop]qrst")
assert not supports("abcd[bddb]xyyx")
assert not supports("aaaa[qwer]tyui")
assert supports("ioxxoj[asdfgh]zxcvbn")

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines() if x != ""]

tls = 0

for x in lines:
    if supports(x):
        tls += 1

print(f"Part 1: {tls}")

assert supports2("aba[bab]xyz")
assert not supports2("xyx[xyx]xyx")
assert supports2("aaa[kek]eke")
assert supports2("zazbz[bzb]cdb")

ssl = 0

for x in lines:
    if supports2(x):
        ssl += 1

print(f"Part 2: {ssl}")


