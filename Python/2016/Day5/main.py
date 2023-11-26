import hashlib
import time

lower = 48
upper = 55

def hash(s):
    result = hashlib.md5(s.encode())

    return result.hexdigest()

with open("input.txt") as f:
    door_id = f.read().strip()

start = time.time()

password = ""
counter = 0

while len(password) < 8:
    h = hash(door_id + str(counter))
    if h.startswith("00000"):
        password += h[5]
    counter += 1

end = time.time()

print("Part 1: {} in {:.3f} seconds".format(password, end - start))

start = time.time()

password = ["_" for _ in range(8)]
counter = 0

while "_" in password:
    h = hash(door_id + str(counter))
    if h.startswith("00000"):
        if lower <= ord(h[5]) <= upper:
            if password[int(h[5])] == "_":
                password[int(h[5])] = h[6]
    counter += 1

end = time.time()

print("Part 2: {} in {:.3f} seconds".format("".join(password), end - start))
