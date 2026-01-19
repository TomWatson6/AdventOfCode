from collections import deque, defaultdict
from copy import deepcopy

input = open("input.txt").read().strip()

class Computer:
    def __init__(self, instructions, input_codes):
        self.ptr = 0
        self.input_codes = deque(input_codes)
        self.output_codes = []
        self.halted = False
        self.rel_base = 0

        self.instr = defaultdict(lambda: 0)
        for i, val in enumerate(instructions):
            self.instr[i] = val

    def run(self):
        while True:
            output = self.exec_instruction()

            if output is not None:
                return output

    def parse_opcode(self, values):
        val = str(self.instr[self.ptr])
        opcode = val[-2:]
        val = val[:-2][::-1]
        modes = []

        for i in range(values):
            if i < len(val):
                modes.append(int(val[i]))
            else:
                modes.append(0)

        return int(opcode), modes

    def get_value(self, mode, val):
        # Position
        if mode == 0:
            return self.instr[val]
        # Immediate
        elif mode == 1:
            return val
        # Relative
        elif mode == 2:
            return self.instr[self.rel_base + val]
        else:
            assert False, mode

    def set_value(self, mode, loc, val):
        # Position
        if mode == 0:
            self.instr[loc] = val
        # Immediate (Invalid)
        elif mode == 1:
            assert False, mode
        # Relative
        elif mode == 2:
            self.instr[self.rel_base + loc] = val
        else:
            assert False, mode

    def exec_instruction(self):
        opcode, modes = self.parse_opcode(0)

        match opcode:
            case 1: self.add()
            case 2: self.mult()
            case 3: self.input()
            case 4: return self.output()
            case 5: self.jump_if_true()
            case 6: self.jump_if_false()
            case 7: self.less_than()
            case 8: self.equals()
            case 9: self.adj_rel_base()
            case 99: 
                self.halted = True
                return self.instr[0]
            case _: assert False, opcode

    def add(self):
        opcode, modes = self.parse_opcode(3)

        a = self.get_value(modes[0], self.instr[self.ptr + 1])
        b = self.get_value(modes[1], self.instr[self.ptr + 2])

        self.set_value(modes[2], self.instr[self.ptr + 3], a + b)

        self.ptr += 4

    def mult(self):
        opcode, modes = self.parse_opcode(3)

        a = self.get_value(modes[0], self.instr[self.ptr + 1])
        b = self.get_value(modes[1], self.instr[self.ptr + 2])

        self.set_value(modes[2], self.instr[self.ptr + 3], a * b)

        self.ptr += 4

    def input(self):
        opcode, modes = self.parse_opcode(1)

        val = self.input_codes.popleft()
        self.set_value(modes[0], self.instr[self.ptr + 1], val)

        self.ptr += 2

    def output(self):
        opcode, modes = self.parse_opcode(1)
        o = self.get_value(modes[0], self.instr[self.ptr + 1])
        self.ptr += 2

        return o

    def jump_if_true(self):
        opcode, modes = self.parse_opcode(2)
        val = self.get_value(modes[0], self.instr[self.ptr + 1])
        o = self.get_value(modes[1], self.instr[self.ptr + 2])

        self.ptr = o if val != 0 else self.ptr + 3

    def jump_if_false(self):
        opcode, modes = self.parse_opcode(2)
        val = self.get_value(modes[0], self.instr[self.ptr + 1])
        o = self.get_value(modes[1], self.instr[self.ptr + 2])

        self.ptr = o if val == 0 else self.ptr + 3

    def less_than(self):
        opcode, modes = self.parse_opcode(3)
        
        a = self.get_value(modes[0], self.instr[self.ptr + 1])
        b = self.get_value(modes[1], self.instr[self.ptr + 2])
        self.set_value(modes[2], self.instr[self.ptr + 3], int(a < b))

        self.ptr += 4

    def equals(self):
        opcode, modes = self.parse_opcode(3)

        a = self.get_value(modes[0], self.instr[self.ptr + 1])
        b = self.get_value(modes[1], self.instr[self.ptr + 2])

        self.set_value(modes[2], self.instr[self.ptr + 3], int(a == b))

        self.ptr += 4

    def adj_rel_base(self):
        opcode, modes = self.parse_opcode(1)

        v = self.get_value(modes[0], self.instr[self.ptr + 1])
        self.rel_base += v

        self.ptr += 2

def parse(input: str):
    return [int(x.strip()) for x in input.split(',')]


PROGRAM = """NOT C T
AND D T
NOT A J
AND D J
OR T J
WALK
"""

def part1(input: str) -> int:
    instructions = parse(input)

    program = [ord(x) for x in list(PROGRAM)]

    computer = Computer(instructions, program)
    outputs = []

    while not computer.halted:
        output = computer.run()
        outputs.append(output)

    return outputs[-2]

PROGRAM2 = """NOT E T
NOT H J
AND T J
NOT J T
NOT C J
AND D J
AND T J
NOT A T
AND D T
OR T J
NOT B T
AND D T
OR T J
RUN
"""

def part2(input: str) -> int:
    instructions = parse(input)

    program = [ord(x) for x in list(PROGRAM2)]

    computer = Computer(instructions, program)
    outputs = []

    while not computer.halted:
        output = computer.run()
        outputs.append(output)

    return outputs[-2]

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















