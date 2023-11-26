from collections import defaultdict
import math

with open("simple_input.txt") as f:
    lines = [line.strip().split(" => ") for line in f.readlines()]

M = {}
A = {}

for line in lines:
    parts = line[0].split(", ")
    input = [p.split(" ") for p in parts]
    output = tuple([x for x in line[1].split(" ")])

    M[output[1]] = [(x[1], int(x[0])) for x in input]

    if output[1] in A:
        assert False, output[1]

    A[output[1]] = int(output[0])

R = defaultdict(int)

def make(r):
    global R

    req = M[r]

    for mat, amt in req:
        print(mat, amt)
        if mat == "ORE":
            R[mat] += amt
            continue

        if mat in R and R[mat] >= amt:
            continue

        need = amt - R[mat]
        to_make = int(math.ceil(need / A[mat]))
        print(to_make)
        for _ in range(to_make):
            make(mat)
        R[mat] += to_make
        print(R)
            
make("FUEL")

print(R)

















