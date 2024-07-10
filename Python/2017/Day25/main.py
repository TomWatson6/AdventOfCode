# In state A:
#   If the current value is 0:
#     - Write the value 1.
#     - Move one slot to the right.
#     - Continue with state B.
#   If the current value is 1:
#     - Write the value 0.
#     - Move one slot to the left.
#     - Continue with state F.

# In state B:
#   If the current value is 0:
#     - Write the value 0.
#     - Move one slot to the right.
#     - Continue with state C.
#   If the current value is 1:
#     - Write the value 0.
#     - Move one slot to the right.
#     - Continue with state D.

import re

with open(0) as f:
    blocks = f.read().split("\n\n")

state = list(re.findall(r"[A-Z]{1}", blocks[0].split("\n")[0]))[-1]
checksum = list(re.findall(r"\d+", blocks[0].split("\n")[1]))[0]

blocks = blocks[1:]
states = {}

for block in blocks:
    lines = [x.strip() for x in block.split("\n")]
    s = list(re.findall(r"[A-Z]{1}", lines[0]))[-1]






