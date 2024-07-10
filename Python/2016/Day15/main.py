import re

with open(0) as f:
    lines = [re.findall(r"(\d+)", x.strip()) for x in f.readlines()]

class Disc:
    def __init__(self, positions, curr):
        self.positions = int(positions)
        self.curr = int(curr) - 1

    def __repr__(self):
        return f"Disc: Positions: {self.positions}, Curr: {self.curr}"

discs = []

for _, positions, _, curr in lines:
    discs.append(Disc(positions, curr))

i = 0
curr = 0

done = [False for _ in range(len(discs))]

while any(not d for d in done):
    disc = discs[curr]


















