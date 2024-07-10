from collections import defaultdict
from copy import deepcopy

start = [6, 4, 12, 1, 20, 0, 16]
S = defaultdict(list)

for i, s in enumerate(start):
    S[s].append(i)

CS = deepcopy(S)

def play_game(iterations):
    global S
    last = start[-1]

    for i in range(len(start), iterations):
        if len(S[last]) > 1:
            last = i - S[last][-2] - 1
        else:
            last = 0

        if len(S[last]) > 1:
            S[last] = [S[last][-1]]
        S[last].append(i)

    return last

print("Part 1:", play_game(2020))

S = CS
print("Part 2:", play_game(30000000))






















