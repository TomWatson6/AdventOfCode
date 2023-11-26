from sys import setrecursionlimit


setrecursionlimit(1000000)

gates = {}

class Gate:
    def __init__(self, parts):
        self.final = ""
        self.action = ""
        self.components = []
        if len(parts) == 1:
            val = parts[0]
            try:
                val = int(parts[0])
            except:
                val = parts[0]
            self.components.append(val)
        elif len(parts) == 2:
            # NOT
            self.action = parts[0]
            self.components.append(parts[1])
        elif len(parts) == 3:
            self.action = parts[1]
            val1 = parts[0]
            val2 = parts[2]
            try:
                val1 = int(parts[0])
            except:
                val1 = parts[0]
            try:
                val2 = int(parts[2])
            except:
                val2 = parts[2]
            self.components.append(val1)
            self.components.append(val2)

    ## TODO: Make sure to check for gates being an integer before calling value()
    def value(self):
        if self.final != "":
            return self.final
        if self.action == "NOT":
            self.final = bitwise_complement(get(self.components[0]))
            return self.final
        elif self.action == "AND":
            a = get(self.components[0])
            b = get(self.components[1])
            self.final = a & b
            return self.final
        elif self.action == "OR":
            a = get(self.components[0])
            b = get(self.components[1])
            self.final = a | b
            return self.final
        elif self.action == "LSHIFT":
            a = get(self.components[0])
            b = get(self.components[1])
            self.final = a << b
            return self.final
        elif self.action == "RSHIFT":
            a = get(self.components[0])
            b = get(self.components[1])
            self.final = a >> b
            return self.final
        else:
            self.final = get(self.components[0])
            return self.final

def get(x):
    if isinstance(x, int):
        return x
    else:
        return gates[x].value()

def get_input(path):
    g = {}

    with open(path) as f:
        input = [x.strip() for x in f.readlines()]

    for line in input:
        parts = [x.strip() for x in line.split("->")]
        k = parts[1]
        s = parts[0].split(" ")
        v = Gate(s)

        g[k] = v

    return g

def bitwise_complement(val):
    b = format(val, 'b').zfill(16)
    out = ""
    for a in b:
        if a == '0':
            out += "1"
        else:
            out += "0"
    return int(out, 2)

gates = get_input("input.txt")

print("Part 1: {}".format(gates["a"].value()))

gates = get_input("input.txt")

gates["b"] = Gate(["46065"])

print("Part 2: {}".format(gates["a"].value()))
