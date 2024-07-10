import re
from collections import defaultdict

with open(0) as f:
    data = f.read().strip()

def decompress(s, p2):
    if '(' not in s:
        return len(s)

    total = 0

    while '(' in s:
        total += s.find('(')

        s = s[s.find('('):]
        marker = s[1:s.find(')')].split('x')
        s = s[s.find(')') + 1:]

        if p2:
            total += decompress(s[:int(marker[0])], p2) * int(marker[1])
        else:
            total += len(s[:int(marker[0])]) * int(marker[1])

        s = s[int(marker[0]):]

    total += len(s)

    return total

print("Part 1:", decompress(data, False))
print("Part 2:", decompress(data, True))
