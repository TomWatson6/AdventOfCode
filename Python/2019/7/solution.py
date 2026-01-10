from collections import deque
from itertools import permutations

input = open("input.txt").read().strip()

class Computer:
    def __init__(self, instructions, input_codes):
        self.ptr = 0
        self.input_codes = deque(input_codes)
        self.output_codes = []
        self.instr = list(instructions)
        self.halted = False

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
            case 99: 
                self.halted = True
                return self.instr[0]
            case _: assert False, opcode

    def add(self):
        opcode, modes = self.parse_opcode(3)

        a = self.get_value(modes[0], self.instr[self.ptr + 1])
        b = self.get_value(modes[1], self.instr[self.ptr + 2])

        c = self.instr[self.ptr + 3]
        self.instr[c] = a + b

        self.ptr += 4

    def mult(self):
        opcode, modes = self.parse_opcode(3)

        a = self.get_value(modes[0], self.instr[self.ptr + 1])
        b = self.get_value(modes[1], self.instr[self.ptr + 2])

        c = self.instr[self.ptr + 3]
        self.instr[c] = a * b

        self.ptr += 4

    def input(self):
        o = self.instr[self.ptr + 1]
        val = self.input_codes.popleft()
        self.instr[o] = val
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

        self.ptr = o if val > 0 else self.ptr + 3

    def jump_if_false(self):
        opcode, modes = self.parse_opcode(2)
        val = self.get_value(modes[0], self.instr[self.ptr + 1])
        o = self.get_value(modes[1], self.instr[self.ptr + 2])

        self.ptr = o if val == 0 else self.ptr + 3

    def less_than(self):
        opcode, modes = self.parse_opcode(3)
        
        a = self.get_value(modes[0], self.instr[self.ptr + 1])
        b = self.get_value(modes[1], self.instr[self.ptr + 2])
        c = self.instr[self.ptr + 3]

        self.instr[c] = a < b

        self.ptr += 4

    def equals(self):
        opcode, modes = self.parse_opcode(3)
        
        a = self.get_value(modes[0], self.instr[self.ptr + 1])
        b = self.get_value(modes[1], self.instr[self.ptr + 2])
        c = self.instr[self.ptr + 3]

        self.instr[c] = a == b

        self.ptr += 4

def parse(input: str):
    return [int(x.strip()) for x in input.split(',')]

def part1(input: str) -> int:
    instructions = parse(input)

    perms = list(permutations([0, 1, 2, 3, 4]))
    largest = 0

    for perm in perms:
        amps = []

        for setting in perm:
            amps.append(Computer(instructions, [setting]))

        amps[0].input_codes.append(0)
        result = None

        for i in range(len(amps)):
            result = amps[i].run()

            if i < len(amps) - 1:
                amps[i + 1].input_codes.append(result)

        largest = max(largest, result)

    return largest

def part2(input: str) -> int:
    instructions = parse(input)

    perms = list(permutations([5, 6, 7, 8, 9]))
    largest = 0

    for perm in perms:
        amps = []

        for setting in perm:
            amps.append(Computer(instructions, [setting]))

        amps[0].input_codes.append(0)

        i = 0
        result = None

        while True:
            result = amps[i % len(amps)].run()
            amps[(i + 1) % len(amps)].input_codes.append(result)
            i += 1
            largest = max(largest, result)

            if all(a.halted for a in amps):
                break

    return largest

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















