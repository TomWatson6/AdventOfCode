from collections import deque, defaultdict
import math
def lcm(x, y):
    return x * y // math.gcd(x, y)

def lcm_list(numbers):
    if len(numbers) == 0:
        return None

    result = numbers[0]
    for i in range(1, len(numbers)):
        result = lcm(result, numbers[i])

    return result

with open(0) as f:
    lines = [x.strip() for x in f.readlines()]

C = {}
S = {}
conj = []
M = {}

for line in lines:
    left, right = line.split(" -> ")
    if left[0] in "%&":
        C[left[1:]] = (1 if left[0] == "%" else 2, right.split(", "))

        # Flip-flop starts in the off state
        if left[0] == "%":
            S[left[1:]] = False

        # Conjunction start without anything remembered
        if left[0] == "&":
            conj.append(left[1:])

    else:
        C[left] = (0, right.split(", "))

for c in conj:
    m = {}
    con = [k for k, v in C.items() if c in v[1]]
    for co in con:
        m[co] = 0
    M[c] = m

REC = defaultdict(int)

def push_button(i):
    global REC
    pulses = [0, 0]
    rx_hit = False
    # 0 == low
    # 1 == high
    Q = deque([("broadcaster", 0)])

    while Q:
        m, p = Q.popleft()
        pulses[p] += 1

        for k in states:
            if m == rx_feed and M[m][k] == 1:
                cycles[k] = i

        if p == 0 and REC[m] != 0:
            REC[m] = 1

        if m == "rx" and p == 0:
            rx_hit = True

        if m not in C:
            continue

        if C[m][0] == 1:
            if p == 1:
                continue
            S[m] = not S[m]

        # Broadcaster
        if C[m][0] == 0:
            for n in C[m][1]:
                if C[n][0] == 2:
                    M[n][m] = p
                Q.append((n, p))
        # Flip-Flop
        elif C[m][0] == 1:
            for n in C[m][1]:
                if C[n][0] == 2:
                    M[n][m] = int(S[m])
                Q.append((n, int(S[m])))
        # Conjunction
        else:
            for n in C[m][1]:
                if all([a == 1 for a in M[m].values()]):
                    if n in C:
                        if C[n][0] == 2:
                            M[n][m] = 0
                    Q.append((n, 0))
                else:
                    if n in C:
                        if C[n][0] == 2:
                            M[n][m] = 1
                    Q.append((n, 1))

    return pulses[0], pulses[1], rx_hit

rx_feed = None

def get_states():
    global rx_feed
    states = set()
    (feed,) = [k for k, v in C.items() if "rx" in v[1]]
    rx_feed = feed

    feeds = [k for k, v in C.items() if feed in v[1]]

    assert all(C[f][0] == 2 for f in feeds)

    states = set(feeds)
    return states

cycles = defaultdict(list)
states = get_states()

low, high = 0, 0
i = 0

while True:
    lo, hi, rx_hit = push_button(i + 1)
    low += lo
    high += hi

    i += 1

    if all(s in cycles for s in states):
        break

    if i == 1000:
        print("Part 1:", low * high)

print("Part 2:", lcm_list(list(cycles.values())))
























