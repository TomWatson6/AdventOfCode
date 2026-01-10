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

def intersections(grid):
    inter = []

    for r in range(1, len(grid) - 2):
        for c in range(1, len(grid[0]) - 2):
            checks = [(r, c), (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            if all(grid[r][c] == '#' for r, c in checks):
                inter.append((r, c))

    return sum([r * c for r, c in inter])

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def find(grid, start, d):
    path = []
    r, c = start
    curr = 0
    count = 0

    while True:
        count += 1
        for i, (dr, dc) in enumerate([DIRS[d], DIRS[(d - 1) % len(DIRS)], DIRS[(d + 1) % len(DIRS)]]):
            rr = r + dr
            cc = c + dc
            if 0 <= rr < len(grid) and 0 <= cc < len(grid[0]) and grid[rr][cc] == '#':
                if i == 0:
                    curr += 1
                    r = rr
                    c = cc
                    break

                if curr != 0:
                    path.append(curr)
                if i == 1:
                    d = (d - 1) % len(DIRS)
                    path.append('L')
                if i == 2:
                    d = (d + 1) % len(DIRS)
                    path.append('R')

                curr = 0
                break
        else:
            break

    if curr != 0:
        path.append(curr)

    return [str(p) for p in path]

grid = []

def get_patterns(path, lower, upper):
    patterns = defaultdict(lambda: 0)

    for i in range(len(path) - upper - 1):
        for j in range(i + lower, i + upper + 1):
            str_pattern = ",".join(path[i:j])
            if len(str_pattern) > upper * 2:
                continue
            pattern = tuple(path[i:j])
            patterns[pattern] += 1

    patterns = {k: v for k, v in patterns.items() if all(c not in ['A', 'B', 'C'] for c in k)}

    return patterns

def reduce(path, pattern, routine):
    new_path = list(path)
    changed = True

    while changed:
        changed = False

        for i in range(len(new_path) - len(pattern)):
            j = i + len(pattern)
            segment = new_path[i:j]
            if tuple(segment) == pattern:
                new_path = new_path[:i] + [routine] + new_path[j:]
                changed = True

    return new_path

def part1(input: str) -> int:
    global grid
    instructions = parse(input)

    computer = Computer(instructions, [])
    while not computer.halted:
        output = computer.run()
        grid.append(output)

    grid = ''.join(chr(x) for x in grid)
    grid = [list(x.strip()) for x in grid.splitlines()]
    grid = grid[:-2]

    return intersections(grid)

def part2(input: str) -> int:
    instructions = parse(input)
    start = (0, 0)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '^':
                start = (r, c)
                break
        if start != (0, 0):
            break

    path = find(grid, start, 0)
    patterns = get_patterns(path, 1, 10)
    patterns = list(patterns.keys())

    for a in range(len(patterns) - 2):
        for b in range(a + 1, len(patterns) - 1):
            for c in range(b + 1, len(patterns)):
                path = find(grid, start, 0)
                path = reduce(path, patterns[a], 'A')
                path = reduce(path, patterns[b], 'B')
                path = reduce(path, patterns[c], 'C')

                if all(p in ['A', 'B', 'C'] for p in path) and len(path) <= 10:
                    path = ','.join(path) + '\n'
                    a = ','.join(patterns[a]) + '\n'
                    b = ','.join(patterns[b]) + '\n'
                    c = ','.join(patterns[c]) + '\n'
                    after = 'n\n'
                    input_codes = [ord(x) for x in path + a + b + c + after]

                    instructions[0] = 2
                    computer = Computer(instructions, input_codes)
                    outputs = []

                    while not computer.halted:
                        output = computer.run()
                        outputs.append(output)

                    return outputs[-2]

    return 0

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















