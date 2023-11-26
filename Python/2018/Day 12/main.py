import re

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

state = lines[0].split()[2]
rules = set([x.split()[0] for x in lines[2:] if x.split()[2] == '#'])

def evolve(state):
    new_state = ""

    for x in range(-2, len(state) + 2):
        section = ""
        for xx in range(x - 2, x + 3):
            if xx < 0 or xx > len(state) - 1:
                section += "."
                continue
            section += state[xx]

        if section in rules:
            new_state += "#"
        else:
            new_state += "."

    assert len(new_state) == len(state) + 4

    return new_state

iterations = 50000000000
DP = {}
i = 0
count = 0

while i < iterations:
    trimmed = list(re.findall("(?<!=#)(#.*#)(?!=#)", state))[0]
    if trimmed in DP:
        t = DP[trimmed]
        print(t)
        mul = iterations // t
        i += t * mul
    DP[trimmed] = i
    new_state = evolve(state)
    assert len(state) == len("".join(new_state[2:-2]))
    if state == "".join(new_state[2:-2]):
        count = i - 1
        break
    state = new_state
    print(len(state))
    i += 1
    count += 1

ans = sum([i - count * 2 if x == '#' else 0 for i, x in enumerate(state)])
print("Part 1:", ans)














