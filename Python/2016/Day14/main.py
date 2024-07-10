from hashlib import md5

with open(0) as f:
    salt = f.read().strip()

def three_in_a_row(s):
    count = 0
    last = -1

    for c in s:
        if c == last:
            count += 1 if count != 0 else 2
        else:
            count = 0

        last = c
        if count == 3:
            return c

    return False

def five_in_a_row(s, t):
    count = 0
    last = -1

    for c in s:
        if c == last and c == t:
            count += 1 if count != 0 else 2
        else:
            count = 0

        last = c
        if count == 5:
            return True

    return False

def fives_in_a_row(s):
    last = -1
    count = 0

    counts = []

    for c in s:
        if c != last:
            counts.append((last, count + 1))
            count = 0
        else:
            count += 1

        last = c

    counts.append((c, count + 1))

    return set([c[0] for c in counts if c[1] == 5])

def hash(s):
    return md5(s.encode('utf-8')).hexdigest()

def hash2(s):
    for _ in range(2017):
        s = md5(s.encode('utf-8')).hexdigest()

    return s

i = 0
keys = 0
DP = {}

while True:
    # print("Processing:", i)
    h = hash2(salt + str(i))
    t = three_in_a_row(h)
    if t:
        for j in range(i + 1, i + 1002):
            if j in DP:
                outcome = DP[j]
            else:
                h2 = hash2(salt + str(j))
                outcome = fives_in_a_row(h2)
                if len(outcome) > 0:
                    print(h2, outcome)
                DP[j] = outcome

            if t in outcome:
                print(keys, i)
                keys += 1
                if keys == 64:
                    print(i)
                    exit()

    i += 1

# NOT 20316

















