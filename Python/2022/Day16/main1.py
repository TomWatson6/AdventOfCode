import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Input File")
args = parser.parse_args()

input_file = "input.txt"

if args.file:
    input_file = args.file

with open(input_file) as f:
    lines = [x.strip() for x in f.readlines()]

F = {}
M = {}

for line in lines:
    p = re.findall("[A-Z]{2}|(?<=\=)\d+", line)
    p = re.findall("[A-Z]{2}|(?<=\=)\d+", line)
    M[p[0]] = p[2:]
    F[p[0]] = int(p[1])

I = {}
non_empty = [k for k, v in F.items() if v != 0]

for i, e in enumerate(non_empty):
    I[e] = i

V = {}

for i, e in enumerate(non_empty):
    V[i] = e

DP = {}

def find(pos, visited, time):
    if time == 0:
        return 0
    
    key = (pos, visited, time)
    if key in DP:
        return DP[key]

    ans = 0

    if time > 0 and F[pos]>0:
        bit = 1 << I[pos]
        print(bit)
        if bit ^ visited:
            ans = max(ans, sum(F[V[i]] for i, x in enumerate(str(visited)) if x == '1') + find(pos, visited | bit, time-1))

    if time > 0:
        for n in M[pos]:
            ans = max(ans, sum(F[V[i]] for i, x in enumerate(str(visited)) if x == '1') + find(n, visited, time-1))

    DP[key] = ans
    return ans

print("Part 1:", find('AA', 0, 30))




