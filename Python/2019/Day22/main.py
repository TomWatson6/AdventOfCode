import re

with open(0) as f:
    lines = [x.strip() for x in f.readlines()]

# cards = 119315717514047

cards = 10007
# cards = 10
instructions = []
instructions2 = []

for line in lines:
    if line.startswith("deal into"):
        instructions.append([0, lambda c, num: cards - c - 1])
    elif line.startswith("deal with"):
        num = int(list(re.findall(r"\d+", line))[-1])
        instructions.append([num, lambda c, num: (c * num) % cards])
    else:
        num = int(list(re.findall(r"-?\d+", line))[-1])
        num %= cards
        instructions.append([num, lambda c, num: c - num if num <= c else c + (cards - num)])

for line in lines[::-1]:
    if line.startswith("deal into"):
        instructions2.append([0, lambda c, num: cards - c - 1])
    elif line.startswith("deal with"):
        num = int(list(re.findall(r"\d+", line))[-1])
        instructions2.append([num, lambda c, num: (c * num) % cards])
    else:
        num = int(list(re.findall(r"-?\d+", line))[-1])
        num *= -1
        num %= cards
        instructions2.append([num, lambda c, num: c - num if num <= c else c + (cards - num)])



card = 2019
# card = 6
diffs = set()
ITERS = 101741582076661
cycled = False
x = 0

# for x in range(ITERS):
while x < ITERS:
    last = int(card)
    for num, i in instructions:
        card = i(card, num)

    if (card - last) in diffs and not cycled:
        rem_iters = ITERS - x + 1
        num_cycles = rem_iters // x
        x += num_cycles * x
        print(x)
        cycled = True

    diffs.add(card - last)
    x += 1

print(card)

# after = []

# for x, card in enumerate(list(range(cards))):
#     for num, i in instructions:
#         card = i(card, num)

#     after.append((card, x))

# after = sorted(after)

# print([x[1] for x in after])




















