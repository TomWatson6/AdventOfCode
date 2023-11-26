
with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

M = [[int(x[0]), int(x[1])] for x in [line.split(": ") for line in lines]]

severity = 0

def pos(range, time):
    if time == 0:
        return 0
    if (time // range) % 2 == 0:
        return time % range
    return range - (time % range)

assert pos(4, 5) == 3
assert pos(4, 2) == 2
assert pos(4, 8) == 0
assert pos(15, 73) == 13

for k, v in M:
    if pos(v - 1, k) == 0:
        severity += k * v

print("Part 1:", severity)

caught = True
delay = 0

while caught:
    caught = False
    for k, v in M:
        if pos(v - 1, k + delay) == 0:
            caught = True
            break
    
    delay += 1

delay -= 1
    
print("Part 2:", delay)





































