from collections import defaultdict, deque
import math

with open(0) as f:
    lines = [line.strip().split(" => ") for line in f.readlines()]

M = defaultdict(list)
MB = defaultdict(set)
A = {}
A['ORE'] = 1

for left, right in lines:
    left = left.split(", ")
    right = right.split()
    A[right[1]] = int(right[0])

    for l in left:
        amt, res = l.split()
        M[right[1]].append((res, int(amt)))
        MB[res].add(right[1])

# res = defaultdict(int)

# def dfs(req, amt):
#     global res
#     ore = 0

#     if req == "ORE":
#         res[req] += amt
#         return amt

#     for ingred, needed in M[req]:
#         # This is adjusted amount based on above amount passed in
#         n = needed * amt
#         # We need to make the max of the Amount we have to make vs. what's needed, always round up
#         # First we need to calculate how much we would have to make to encompass needed in the amount
#         a = math.ceil(n / A[ingred]) * A[ingred]
#         a1 = math.ceil((n - res[ingred]) / A[ingred]) * A[ingred]
#         if a1 < a:
#             ore += dfs(ingred, a1)
#         else:
#             ore += dfs(ingred, a)
#         res[ingred] -= n

#     res[req] += amt
#     return ore

# ore = dfs("FUEL", 1)

# print(res)
# print(ore)

def bfs(req, amt):
    Q = deque([(req, amt, A[req])])
    R = defaultdict(int)
    ore = 0

    while Q:
        req, amt, div = Q.popleft()

        if req == 'ORE':
            ore += amt / div
            continue

        final = 0

        r = math.ceil(amt - R[req] / A[req]) * A[req]
        a = math.ceil(amt / A[req]) * A[req]

        # If current resources makes a difference to amount required
        if r != a:
            # We need to calculate needed resources to make that difference
            d, _ = math.modf((amt - R[req] / A[req]))
            sub = int(d * A[req])
            R[req] -= sub
            final = r
            # print(r, a, d, sub, R[req], final)
        else:
            if a != (amt // A[req]) * A[req]:
                d, _ = math.modf(amt / A[req])
                R[req] += int(d * A[req])
            final = a

        for ingred, needed in M[req]:
            Q.append((ingred, final * needed, div * A[req]))

    return ore

ore = bfs("FUEL", 1)
print(ore)


















