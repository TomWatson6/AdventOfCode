

S = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
}

M = {
    'A': "Rock",
    'B': "Paper",
    'C': "Scissors",
    'X': "Rock",
    'Y': "Paper",
    'Z': "Scissors",
}

W = {
    "Rock": "Scissors",
    "Scissors": "Paper",
    "Paper": "Rock",
}

L = {
    "Rock": "Paper",
    "Scissors": "Rock",
    "Paper": "Scissors",
}

D = {
    "Rock": "Rock",
    "Scissors": "Scissors",
    "Paper": "Paper",
}

O = {
    'X': lambda: W,
    'Y': lambda: D,
    'Z': lambda: L,
}

with open("input.txt") as f:
    moves = [x.strip().split() for x in f.readlines()]

score = 0

for op, me in map(lambda x: (M[x[0]], M[x[1]]), moves):
    score += S[me]

    if op == W[me]:
        score += 6
    elif me == W[op]:
        continue
    else:
        score += 3

print("Part 1:", score)

score = 0

for op, outcome in map(lambda x: (M[x[0]], x[1]), moves):
    me = O[outcome]()[op]
    
    score += S[me]
 
    if op == W[me]:
        score += 6
    elif me == W[op]:
        continue
    else:
        score += 3   

print("Part 2:", score)