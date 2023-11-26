
class Monkey:
    def __init__(self, input):
        self.id = input[0].split(" ")[1].strip(":")
        self.items = list(map(int, input[1].split(": ")[1].split(", ")))
        self.op = input[2].split(" = ")[1]
        self.test = int(input[3].split(" ")[-1])
        self.pos = int(input[4].split(" ")[-1])
        self.neg = int(input[5].split(" ")[-1])
        self.inspections = 0

    def inspect(self):
        old = self.items[0]
        new = eval(self.op)
        self.items[0] = new // 3
        self.inspections += 1

    def inspect2(self, lcm):
        old = self.items[0]
        new = eval(self.op)
        self.items[0] = new % lcm
        self.inspections += 1

    def throw(self):
        item = self.items.pop(0)
        if item % self.test == 0:
            return (item, self.pos)
        return (item, self.neg)

    def print(self):
        print(self.id, self.items, self.op, self.test, self.pos, self.neg, self.inspections)

with open("input.txt") as f:
    sections = f.read().split("\n\n")
    monkeys = [Monkey([a.strip() for a in x.split("\n")]) for x in sections]
    monkeys2 = [Monkey([a.strip() for a in x.split("\n")]) for x in sections]

def print_monkeys():
    for m in monkeys:
        print(m.inspections, m.items)

for r in range(20):
    for m in monkeys:
        while len(m.items) > 0:
            m.inspect()
            item, m2 = m.throw()
            monkeys[m2].items.append(item)

monkeys = sorted(monkeys, key=lambda m: m.inspections)

print(f"Part 1: {monkeys[-1].inspections * monkeys[-2].inspections}")

lcm = 1

for m in monkeys2:
    lcm *= m.test

for r in range(10000):
    for m in monkeys2:
        while len(m.items) > 0:
            m.inspect2(lcm)
            item, m2 = m.throw()
            monkeys2[m2].items.append(item)

monkeys2 = sorted(monkeys2, key=lambda m: m.inspections)

print(f"Part 2: {monkeys2[-1].inspections * monkeys2[-2].inspections}")





























