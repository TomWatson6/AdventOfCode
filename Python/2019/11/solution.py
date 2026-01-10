from collections import deque, defaultdict
from itertools import permutations

input = open("input.txt").read().strip()

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class Computer:
    def __init__(self, instructions, input_codes, grid):
        self.ptr = 0
        self.input_codes = deque(input_codes)
        self.output_codes = []
        self.halted = False
        self.rel_base = 0
        self.grid = grid
        self.pos = (0, 0)
        self.dir = 0

        # 0 is color to paint, 1 is direction
        self.mode = 0

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
            case 4: self.output()
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

        # val = self.input_codes.popleft()
        val = 1 if self.pos in self.grid and self.grid[self.pos] == '#' else 0
        # val = 1 if self.pos in self.grid else 0
        self.set_value(modes[0], self.instr[self.ptr + 1], val)

        self.ptr += 2

    def output(self):
        opcode, modes = self.parse_opcode(1)
        o = self.get_value(modes[0], self.instr[self.ptr + 1])
        self.ptr += 2

        # Color Paint Mode
        if self.mode == 0:
            if o == 0:
                self.grid[self.pos] = '.'
            elif o == 1:
                self.grid[self.pos] = '#'
            else:
                assert False, o

            self.mode = 1

        elif self.mode == 1:
            if o == 0:
                self.dir = (self.dir - 1) % len(DIRS)
            elif o == 1:
                self.dir = (self.dir + 1) % len(DIRS)
            else:
                assert False, o

            self.pos = (self.pos[0] + DIRS[self.dir][0], self.pos[1] + DIRS[self.dir][1])
            self.mode = 0

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

def part1(input: str) -> int:
    instructions = parse(input)

    computer = Computer(instructions, [], {})
    computer.run()

    return len(computer.grid.values())

def part2(input: str) -> int:
    instructions = parse(input)

    computer = Computer(instructions, [], {(0, 0): '#'})
    computer.run()

    low_r = min(computer.grid.keys(), key = lambda k: k[0])[0]
    high_r = max(computer.grid.keys(), key = lambda k: k[0])[0]
    low_c = min(computer.grid.keys(), key = lambda k: k[1])[1]
    high_c = max(computer.grid.keys(), key = lambda k: k[1])[1]

    rows = []

    for r in range(low_r, high_r + 1):
        row = ""
        for c in range(low_c, high_c + 1):
            if (r, c) in computer.grid and computer.grid[(r, c)] == '#':
                row += '#'
            else:
                row += ' '

        rows.append(row)

    return "\n".join(rows)

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:\n", part2(input), sep = "")















