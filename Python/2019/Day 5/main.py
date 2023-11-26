from Computer import Computer

input = ""

with open("input.txt") as f:
    input = f.read().strip()

comp = Computer(input, 1)

comp.compute()

comp = Computer(input, 5)

comp.compute()










