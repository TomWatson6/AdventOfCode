import re

with open("input.txt") as f:
    input = f.read().strip()

parts = [x.group() for x in re.finditer(r"(\(\d+x\d+\))+\w+", input)]

print(parts)




