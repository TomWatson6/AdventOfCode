from collections import deque, defaultdict
from copy import deepcopy

input = open("input.txt").read().strip()

class TileType:
    Wall = '#'
    Empty = '.'
    Oxygen = 'O'

DIRS = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

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

        if o == 0:
            return TileType.Wall
        elif o == 1:
            return TileType.Empty
        elif o == 2:
            return TileType.Oxygen
        else:
            assert False, "OUTPUT CODE INVALID:" + str(o)

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

def bfs(instructions, p2):
    queue = deque([
        (Computer(instructions, [1]), 0, (0, 0)),
        (Computer(instructions, [2]), 0, (0, 0)),
        (Computer(instructions, [3]), 0, (0, 0)),
        (Computer(instructions, [4]), 0, (0, 0)),
    ])

    seen = set()
    seen.add((0, 0))
    grid = {}

    while queue:
        computer, depth, pos = queue.popleft()
        d = DIRS[computer.input_codes[0]]

        new_pos = (pos[0] + d[0], pos[1] + d[1])

        if new_pos in seen:
            continue

        seen.add(new_pos)

        tile = computer.run()
        grid[new_pos] = tile

        if tile == TileType.Wall:
            continue

        pos = new_pos

        if tile == TileType.Oxygen:
            if not p2:
                return depth + 1

        for i in range(1, 5):
            new_computer = deepcopy(computer)
            new_computer.input_codes.append(i)

            queue.append((new_computer, depth + 1, deepcopy(pos)))

    return grid if p2 else 0

def bfs2(grid, start):
    queue = deque([(start, 0)])
    seen = set()
    largest = 0

    while queue:
        (r, c), d = queue.popleft()

        if (r, c) in seen:
            continue

        seen.add((r, c))

        largest = max(largest, d)

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rr = r + dr
            cc = c + dc

            if (rr, cc) in grid and grid[(rr, cc)] == TileType.Empty:
                queue.append(((rr, cc), d + 1))

    return largest

def part1(input: str) -> int:
    instructions = parse(input)

    ans = bfs(instructions, False)

    return ans

def part2(input: str) -> int:
    instructions = parse(input)

    grid = bfs(instructions, True)
    start = [key for key in grid.keys() if grid[key] == TileType.Oxygen][0]

    ans = bfs2(grid, start)

    return ans

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















