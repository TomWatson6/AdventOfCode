import hashlib

def hash(input):
    b = hashlib.md5(input.encode())
    return b.hexdigest()

with open("input.txt") as f:
    input = f.read().strip()

num = 0

for i in range(99999999):
    s = str(i)
    h = input + s
    ret = hash(h)
    if ret.startswith("00000"):
        num = i
        break

print("Part 1:", num)

num = 0

for i in range(99999999):
    s = str(i)
    h = input + s
    ret = hash(h)
    if ret.startswith("000000"):
        num = i
        break

print("Part 2:", num)