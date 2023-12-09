
with open(0) as f:
    lines = [x.strip() for x in f.readlines()]

def get_next(seq, p2):
    elem = -1
    if p2:
        elem = 0

    hist = []
    hist.append(seq[:])
    new_seq = []

    while not all(x == 0 for x in new_seq) or new_seq == []:
        new_seq = []

        for i in range(len(seq) - 1):
            new_seq.append(seq[i + 1] - seq[i])

        hist.append(new_seq)

        seq = new_seq

    hist[-1].append(0)

    for i in range(len(hist) - 2, -1, -1):
        hist[i].insert(elem, hist[i][elem] - hist[i + 1][elem] if p2 else -hist[i + 1][elem])

    return hist[0][elem]

for p2 in [False, True]:
    total = 0

    for line in lines:
        nums = list(map(int, line.split()))

        total += get_next(nums, p2)

    print("Part {}: {}".format(2 if p2 else 1, total))



















