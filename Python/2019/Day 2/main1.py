
from Computer import Computer

input = ""

with open("input.txt") as f:
    input = f.read().strip()
    
comp = Computer(input)
comp.values[1] = 12
comp.values[2] = 2

comp.compute()

print(f"Part 1: {comp.values[0]}")

for a in range(100):
    for b in range(100):
        comp = Computer(input)
        comp.values[1] = a
        comp.values[2] = b

        comp.compute()

        if comp.values[0] == 19690720:
            print(f"Part 2: {a * 100 + b}")
            exit(0)


