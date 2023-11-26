
with open("input.txt") as f:
    directions = [x.strip() for x in f.read().split(",")]

# D = {
#     "ne": 1j,
#     "sw": -1j,
#     "n": 1 + 1j, 
#     "s": -1 - 1j,
#     "nw": -1,
#     "se": 1
# }

# D = {
#     "n": (1, 0, 0),
#     "s": (-1, 0, 0),
#     "ne": (0, 1, 0),
#     "sw": (0, -1, 0),
#     "nw": (0, 0, 1),
#     "se": (0, 0, -1),
# }

D = {
    "n": 2j,
    "s": -2j,
    "nw": -1 + 1j,
    "ne": 1 + 1j, 
    "sw": -1 - 1j,
    "se": 1 - 1j
}

furthest = 0

def mag(p):
    return int(abs(p.real) + abs(p.imag)) // 2

def follow(directions):
    global furthest
    p = 0

    for dir in directions:
        p += D[dir]
        furthest = max(furthest, mag(p))

    return p

assert mag(follow("ne,ne,ne".split(","))) == 3
assert mag(follow("ne,ne,sw,sw".split(","))) == 0
assert mag(follow("ne,ne,s,s".split(","))) == 2
assert mag(follow("se,sw,se,sw,sw".split(","))) == 3

p = follow(directions)
p = mag(p)

print("Part 1:", p)
print("Part 2:", furthest)


















