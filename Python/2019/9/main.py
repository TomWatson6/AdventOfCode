
ins_ptr = 0
input_code = 0
output_code = 0
relative_base = 0

class mode:
    position = 0
    immediate = 1
    relative = 2

def reset_values():
    global ins_ptr, input_code, output_code, relative_base

    ins_ptr = 0
    input_code = 0
    output_code = 0
    relative_base = 0

def add(params):
    global I, ins_ptr

    a = read(params[0][0], params[0][1])
    b = read(params[1][0], params[1][1])
    write(params[2][0], params[2][1], a + b)

    ins_ptr += len(params) + 1

def mult(params):
    global I, ins_ptr

    a = read(params[0][0], params[0][1])
    b = read(params[1][0], params[1][1])
    write(params[2][0], params[2][1], a * b)

    ins_ptr += len(params) + 1

def input(params):
    global I, ins_ptr, input_code

    # write(params[0][1], 1)
    write(params[0][0], params[0][1], input_code)

    ins_ptr += len(params) + 1

def output(params):
    global I, ins_ptr, output_code

    a = read(params[0][0], params[0][1])
    if a != 0:
        output_code = a

    ins_ptr += len(params) + 1

def jump_if_true(params):
    global I, ins_ptr

    a = read(params[0][0], params[0][1])
    b = read(params[1][0], params[1][1])

    if a != 0:
        ins_ptr = b
    else:
        ins_ptr += len(params) + 1

def jump_if_false(params):
    global I, ins_ptr

    a = read(params[0][0], params[0][1])
    b = read(params[1][0], params[1][1])

    if a == 0:
        ins_ptr = b
    else:
        ins_ptr += len(params) + 1

def less_than(params):
    global I, ins_ptr

    a = read(params[0][0], params[0][1])
    b = read(params[1][0], params[1][1])

    if a < b:
        write(params[2][0], params[2][1], 1)
    else:
        write(params[2][0], params[2][1], 0)

    ins_ptr += len(params) + 1

def equals(params):
    global I, ins_ptr

    a = read(params[0][0], params[0][1])
    b = read(params[1][0], params[1][1])

    if a == b:
        write(params[2][0], params[2][1], 1)
    else:
        write(params[2][0], params[2][1], 0)

    ins_ptr += len(params) + 1

def adjust_relative_base(params):
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
    while I[ins_ptr] != 99:
        opcode, modes = parse(I[ins_ptr])

        if opcode == 1:
            add(zip(modes, get_slice(ins_ptr + 1, ins_ptr + 4)))
        elif opcode == 2:
            mult(zip(modes, get_slice(ins_ptr + 1, ins_ptr + 4)))
        elif opcode == 3:
            input(zip(modes, get_slice(ins_ptr + 1, ins_ptr + 2)))
        elif opcode == 4:
            output(zip(modes, get_slice(ins_ptr + 1, ins_ptr + 2)))
        elif opcode == 5:
            jump_if_true(zip(modes, get_slice(ins_ptr + 1, ins_ptr + 3)))
        elif opcode == 6:
            jump_if_false(zip(modes, get_slice(ins_ptr + 1, ins_ptr + 3)))
        elif opcode == 7:
            less_than(zip(modes, get_slice(ins_ptr + 1, ins_ptr + 4)))
        elif opcode == 8:
            equals(zip(modes, get_slice(ins_ptr + 1, ins_ptr + 4)))
        elif opcode == 9:
            adjust_relative_base(zip(modes, get_slice(ins_ptr + 1, ins_ptr + 2)))
        else:
            assert False, I[ins_ptr]

    return I[0]

with open("input.txt") as f:
    I = {i: int(x) for i, x in enumerate(f.read().strip().split(","))}

CI = {x[0]: x[1] for x in I.items()}

input_code = 1
process(I)
print("Part 1:", output_code)

I = {x[0]: x[1] for x in CI.items()}

reset_values()
input_code = 2
process(I)
print("Part 2:", output_code)




















