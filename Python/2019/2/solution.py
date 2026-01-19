
input = open("input.txt").read().strip()

class Computer:
    def __init__(self, instructions):
        self.ptr = 0
        self.instr = instructions

    def run(self):
        while True:
            output = self.exec_instruction()

            if output is not None:
                return output


    def exec_instruction(self):
        match self.instr[self.ptr]:
            case 1: self.add()
            case 2: self.mult()
            case 99: return self.instr[0]

    def add(self):
        a = self.instr[self.ptr + 1]
        b = self.instr[self.ptr + 2]
        c = self.instr[self.ptr + 3]
        self.instr[c] = self.instr[a] + self.instr[b]

        self.ptr += 4

    def mult(self):
        a = self.instr[self.ptr + 1]
        b = self.instr[self.ptr + 2]
        c = self.instr[self.ptr + 3]
        self.instr[c] = self.instr[a] * self.instr[b]

        self.ptr += 4

def parse(input: str):
    return [int(x.strip()) for x in input.split(',')]

def part1(input: str) -> int:
    instructions = parse(input)

    instructions[1] = 12
    instructions[2] = 2

    computer = Computer(instructions)

    return computer.run()

def part2(input: str) -> int:
    req = 19690720

    for a in range(100):
        for b in range(100):
            instructions = parse(input)
            instructions[1] = a
            instructions[2] = b

            computer = Computer(instructions)
            if computer.run() == req:
                return a * 100 + b

    return 0

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















