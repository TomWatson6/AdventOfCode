

class Computer:
    def __init__(self, program, start):
        # print("initialised computer with program of length:", len(program))
        self.start = start
        self.values = [int(x) for x in program.split(",")]
        self.pos = 0

    def compute(self):
        while self.pos < len(self.values):
            # print(self.pos)
            ins = self.values[self.pos]
            opcode, modes = ins, []

            if len(str(ins)) >= 2:
                opcode = int(str(ins)[-2:])
                modes = [int(x) for x in str(ins)[:-2].zfill(3)[::-1]]
                # assert modes[0] == 0 # First must be position in order to store value

            if opcode != 99:
                if opcode == 1:
                    a, b, c = self.values[self.pos + 1], self.values[self.pos + 2], self.values[self.pos + 3]
                    if len(modes) == 0:
                        modes = [0 for _ in range(3)]
                    self.add(modes, [a, b, c])
                elif opcode == 2:
                    if len(modes) == 0:
                        modes = [0 for _ in range(3)]
                    a, b, c = self.values[self.pos + 1], self.values[self.pos + 2], self.values[self.pos + 3]
                    self.mult(modes, [a, b, c])
                elif opcode == 3:
                    v = self.values[self.pos + 1]
                    self.input(v)
                elif opcode == 4:
                    if len(modes) == 0:
                        modes = [0]
                    v = self.values[self.pos + 1]
                    final = self.values[self.pos + 2] == 99
                    self.output(modes[0], v, final)
                elif opcode == 5:
                    if len(modes) == 0:
                        modes = [0 for _ in range(2)]
                    a, b = self.values[self.pos + 1], self.values[self.pos + 2]
                    self.jump_if_true(modes, [a, b])
                elif opcode == 6:
                    if len(modes) == 0:
                        modes = [0 for _ in range(2)]
                    a, b = self.values[self.pos + 1], self.values[self.pos + 2]
                    self.jump_if_false(modes, [a, b])
                elif opcode == 7:
                    if len(modes) == 0:
                        modes = [0 for _ in range(3)]
                    a, b, c = self.values[self.pos + 1], self.values[self.pos + 2], self.values[self.pos + 3]
                    self.less_than(modes, [a, b, c])
                elif opcode == 8:
                    if len(modes) == 0:
                        modes = [0 for _ in range(3)]
                    a, b, c = self.values[self.pos + 1], self.values[self.pos + 2], self.values[self.pos + 3]
                    self.equals(modes, [a, b, c])

                # else:
                    # print("There is a problem with this shit code...", opcode)
            else:
                break

    def add(self, modes, vals):
        # print("add:", modes, vals)
        for i, m in enumerate(modes[:len(vals) - 1]):
            if m == 0:
                vals[i] = self.values[vals[i]]
        # print(vals)

        self.values[vals[2]] = vals[0] + vals[1]
        self.pos += 4

    def mult(self, modes, vals):
        # print("mult:", modes, vals)
        for i, m in enumerate(modes[:len(vals) - 1]):
            if m == 0:
                vals[i] = self.values[vals[i]]

        # print(vals)
        self.values[vals[2]] = vals[0] * vals[1]
        self.pos += 4

    def input(self, pos):
        # print("input:", pos)
        self.values[pos] = self.start
        self.pos += 2

    def output(self, mode, val, final):
        # print(f"{'val' if mode == 1 else 'pos'}: {val}")
        if mode == 0:
            val = self.values[val]
        # print("output:", mode, val, final)

        if val != 0 and not final:
            print("Program failed...")
            exit(-1)
        
        if val != 0 and final:
            print(f"Part 1: {val}")

        self.pos += 2

    def jump_if_true(self, modes, vals):
        for i, m in enumerate(modes):
            if m == 0:
                vals[i] = self.values[vals[i]]

        if vals[0] != 0:
            self.pos = vals[1]
            return
        
        self.pos += 3

    def jump_if_false(self, modes, vals):
        for i, m in enumerate(modes):
            if m == 0:
                vals[i] = self.values[vals[i]]

        if vals[0] == 0:
            self.pos = vals[1]
            return

        self.pos += 3

    def less_than(self, modes, vals):
        for i, m in enumerate(modes):
            if m == 0:
                vals[i] = self.values[vals[i]]

        if vals[0] < vals[1]:
            self.values[vals[2]] = 1
        else:
            self.values[vals[2]] = 0

        self.pos += 4

    def equals(self, modes, vals):
        for i, m in enumerate(modes):
            if m == 0:
                vals[i] = self.values[vals[i]]

        if vals[0] == vals[1]:
            self.values[vals[2]] = 1
        else:
            self.values[vals[2]] = 0

        self.pos += 4








