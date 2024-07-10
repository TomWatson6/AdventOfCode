import re
from collections import deque

class Type:
    Generator = 0
    Microchip = 1

class Item:
    def __init__(self, name):
        if "generator" in name:
            self.type = Type.Generator
        else:
            self.type = Type.Microchip

        self.name = name.split()[0]
        self.moved = False

    def __repr__(self):
        return f"{'Microchip' if self.type else 'Generator'} - {self.name}"

with open(0) as f:
    lines = [x.strip() for x in f.readlines()]

F = []

for line in lines:
    line = list(re.findall(r"([a-z-]+ microchip|\w+ generator)", line))
    F.append([Item(x.replace("-compatible", "")) for x in line])

F = [f for f in F if f != []]
print(F)

Q = deque([0, []])
S = set()

# STARTING CONFIGURATION
# [
#     ['thulium generator', 'thulium microchip', 'plutonium generator', 'strontium generator'],
#     ['plutonium microchip', 'strontium microchip'],
#     ['promethium generator', 'promethium microchip', 'ruthenium generator', 'ruthenium microchip'],
# ]

"""
What can happen?
 - Random things can be placed onto the lift, between 1 and 2 items
 - The lift moves up or down
Fails when:
 - Microchip that has moved is without it's generator on the same level
"""

while Q:
    floor, cargo = Q.popleft()

    combined = F[floor] + cargo
    chips = [x for x in F if x.moved and x.type == Type.Microchip]
    valid = True

    for chip in chips:
        if chip.name not in [x.name for x in F if x.type == Type.Generator and x.name == chip.name]:
            valid = False




















