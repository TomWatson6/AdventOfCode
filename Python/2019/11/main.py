from collections import defaultdict

ins_ptr = 0
input_code = 0
output_code = 0
relative_base = 0
outputs = 0

# d + 1 = right, d - 1 = left
DIR = {
    0: (0, -1), # Up
    1: (1, 0), # Right
    2: (0, 1), # Down
    3: (-1, 0) # Left
}

d = 0
G = defaultdict(int)
pos = (0, 0)
S = defaultdict(int)

class mode:
    position = 0
    immediate = 1
    relative = 2

class code:
    add = 1
    mult = 2
    input = 3
    output = 4
    jump_if_true = 5
    jump_if_false = 6
    less_than = 7
    equals = 8
    adjust_relative_base = 9
    halt = 99

def reset_values():
    global ins_ptr, input_code, output_code, relative_base

    ins_ptr = 0
    input_code = 0
    output_code = 0
    relative_base = 0

def add(params):
    params = list(params)
    global I, ins_ptr

    a = read(params[0][0], params[0][1])
    b = read(params[1][0], params[1][1])
    write(params[2][0], params[2][1], a + b)

    ins_ptr += len(params) + 1

def mult(params):
    params = list(params)
    global I, ins_ptr

    a = read(params[0][0], params[0][1])
    b = read(params[1][0], params[1][1])
    write(params[2][0], params[2][1], a * b)

    ins_ptr += len(params) + 1

def input(params):
    params = list(params)
    global I, ins_ptr, input_code

    # write(params[0][1], 1)
    write(params[0][0], params[0][1], input_code())

    ins_ptr += len(params) + 1

def output(params):
    params = list(params)
    global I, ins_ptr, output_code, outputs

    a = read(params[0][0], params[0][1])
    output_code = a
    outputs += 1

    ins_ptr += len(params) + 1

def jump_if_true(params):
    params = list(params)
    global I, ins_ptr

    a = read(params[0][0], params[0][1])
    b = read(params[1][0], params[1][1])

    if a != 0:
        ins_ptr = b
    else:
        ins_ptr += len(params) + 1

def jump_if_false(params):
    params = list(params)
    global I, ins_ptr

    a = read(params[0][0], params[0][1])
    b = read(params[1][0], params[1][1])

    if a == 0:
        ins_ptr = b
    else:
        ins_ptr += len(params) + 1

def less_than(params):
    params = list(params)
    global I, ins_ptr

    a = read(params[0][0], params[0][1])
    b = read(params[1][0], params[1][1])

    if a < b:
        write(params[2][0], params[2][1], 1)
    else:
        write(params[2][0], params[2][1], 0)

    ins_ptr += len(params) + 1

def equals(params):
    params = list(params)
    global I, ins_ptr

    a = read(params[0][0], params[0][1])
    b = read(params[1][0], params[1][1])

    if a == b:
        write(params[2][0], params[2][1], 1)
    else:
        write(params[2][0], params[2][1], 0)

    ins_ptr += len(params) + 1

def adjust_relative_base(params):
    params = list(params)
    global ins_ptr, relative_base

    a = read(params[0][0], params[0][1])

    relative_base += a

    ins_ptr += len(params) + 1

def parse(a):
    op = str(a).zfill(5)

    return int(op[-2:]), [int(x) for x in op[:-2][::-1]]

def read(m, x):
    global I, relative_base

    if m == mode.position:
        return I[x]
    elif m == mode.immediate:
        return x
    else:
        return I[relative_base + x]

def write(m, x, i):
    global I

    if m == mode.position:
        I[x] = i
    elif m == mode.relative:
        I[relative_base + x] = i
    else:
        assert False

def get_slice(start, finish):
    global I

    return [I[x] for x in range(start, finish)]

def process(I):
    global G, d, pos, output_code, outputs, ins_ptr
    while I[ins_ptr] != code.halt:
        opcode, modes = parse(I[ins_ptr])

        if opcode == code.add:
            add(zip(modes, get_slice(ins_ptr + 1, ins_ptr + 4)))
        elif opcode == code.mult:
            mult(zip(modes, get_slice(ins_ptr + 1, ins_ptr + 4)))
        elif opcode == code.input:
            input(zip(modes, get_slice(ins_ptr + 1, ins_ptr + 2)))
        elif opcode == code.output:
            output(zip(modes, get_slice(ins_ptr + 1, ins_ptr + 2)))
            if outputs % 2 == 1:
                if output_code == 0:
                    d = (d - 1) % 4
                elif output_code == 1:
                    d = (d + 1) % 4
                else:
                    assert False, output_code
                pos = (pos[0] + DIR[d][0], pos[1] + DIR[d][1])
            else:
                G[pos] = output_code
                S[pos] += 1

            # print(G)
            # print(pos, d, output_code)
        elif opcode == code.jump_if_true:
            jump_if_true(zip(modes, get_slice(ins_ptr + 1, ins_ptr + 3)))
        elif opcode == code.jump_if_false:
            jump_if_false(zip(modes, get_slice(ins_ptr + 1, ins_ptr + 3)))
        elif opcode == code.less_than:
            less_than(zip(modes, get_slice(ins_ptr + 1, ins_ptr + 4)))
        elif opcode == code.equals:
            equals(zip(modes, get_slice(ins_ptr + 1, ins_ptr + 4)))
        elif opcode == code.adjust_relative_base:
            adjust_relative_base(zip(modes, get_slice(ins_ptr + 1, ins_ptr + 2)))
        else:
            assert False, I[ins_ptr]

        # print(ins_ptr)

    return I[0]

def print_grid(grid):
    min_x = min(grid.keys(), key = lambda k: k[0])[0]
    max_x = max(grid.keys(), key = lambda k: k[0])[0]
    min_y = min(grid.keys(), key = lambda k: k[1])[1]
    max_y = max(grid.keys(), key = lambda k: k[1])[1]

    for y in range(min_y, max_y + 1):
        row = ""
        for x in range(min_x, max_x + 1):
            row += str(grid[(y, x)])

        print(row)
    print()

with open("input.txt") as f:
    I = {i: int(x) for i, x in enumerate(f.read().strip().split(","))}

II = defaultdict(int)

for k, v in I.items():
    II[k] = v

I = II

CI = {x[0]: x[1] for x in I.items()}

# Input reads current panel colour
# Output firstly outputs the colour to paint the current panel, secondly it outputs the direction to turn
# 0 = left, 1 = right by 90 degrees
# After turning, the robot moves forward one panel in the direction it is now facing

input_code = lambda: G[pos]

process(I)

print(len([s for s in S.values() if s != 0]))
# print(G)
# print(S)

# g_xlow = min([x[0] for x in G.keys()])
# g_xhigh = max([x[0] for x in G.keys()])
# g_ylow = min([x[1] for x in G.keys()])
# g_yhigh = max([x[1] for x in G.keys()])

# for y in range(g_ylow, g_yhigh + 1):
#     out = ""
#     for x in range(g_xlow, g_xhigh + 1):
#         if G[(x, y)] == 1:
#             out += "#"
#         else:
#             out += " "
#     print(out)
# print()

# print([k for k in S.values()])

# print(dir)
# V.append(pos)
# print(len(V), len(set(V)))
















