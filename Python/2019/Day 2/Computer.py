

class Computer:
    def __init__(self, program):
        self.values = [int(x) for x in program.split(",")]
        self.pos = 0

    def compute(self):
        while self.pos < len(self.values):
            if self.values[self.pos] != 99:
                a, b, c = self.values[self.pos + 1], self.values[self.pos + 2], self.values[self.pos + 3]
                if self.values[self.pos] == 1:
                    self.add(a, b, c)
                elif self.values[self.pos] == 2:
                    self.mult(a, b, c)
            else:
                break
            
            self.pos += 4

    def add(self, a, b, c):
        self.values[c] = self.values[a] + self.values[b]

    def mult(self, a, b, c):
        self.values[c] = self.values[a] * self.values[b]









