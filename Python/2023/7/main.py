from collections import defaultdict

def strength(hand, p2):
    rep = {'T': 'A', 'J': '1' if p2 else 'B', 'Q': 'C', 'K': 'D', 'A': 'E'}
    types = {6: [5], 5: [1, 4], 4: [2, 3], 3: [1, 1, 3], 2: [1, 2, 2], 1: [1, 1, 1, 2]}

    hand = "".join([rep[x] if x in rep else x for x in hand])

    counts = defaultdict(int)

    for card in hand:
        counts[card] += 1

    if p2:
        target = list(counts.keys())[0]

        counts_copy = counts.copy()
        for card, count in counts.items():
            if card != '1':
                if count > counts_copy[target] or target == '1':
                    target = card

        if '1' in counts and target != '1':
            counts[target] += counts['1']
            del counts['1']

    vals = sorted(counts.values())

    for score, t in types.items():
        if vals == t:
            return score, hand

    return 0, hand

with open(0) as f:
    lines = [x.strip() for x in f.readlines()]

C = {}

for line in lines:
    left, right = line.split()
    C[left] = int(right)

for p2 in [False, True]:
    hands = sorted(C.keys(), key = lambda hand: strength(hand, p2))

    total = 0

    for i, hand in enumerate(hands):
        total += (i + 1) * C[hand]

    print("Part {}: {}".format(2 if p2 else 1, total))
















