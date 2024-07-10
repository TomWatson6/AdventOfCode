from collections import defaultdict, deque
import networkx as nx
import random

with open(0) as f:
    lines = [x.strip() for x in f.readlines()]

M = defaultdict(list)
nodes = set()
G = nx.Graph()

for line in lines:
    left, right = line.split(": ")
    right = right.split()

    for r in right:
        M[left].append(r)
        M[r].append(left)
        G.add_edge(left, r, capacity=1.0)

cut_value = 100

while cut_value > 3:
    k1 = random.choice(list(M.keys()))
    k2 = random.choice(list(M.keys()))

    cut_value, partition = nx.minimum_cut(G, k1, k2)

print("Answer:", len(partition[0]) * len(partition[1]))








