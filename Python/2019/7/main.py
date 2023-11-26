
ins_ptr = 0
input_code = 0
output_code = 0
signal = 0
halted = False

class mode:
    position = 0
    immediate = 1

def add(params):
    global I, ins_ptr

    a = read(params[0][0], params[0][1])
    b = read(params[1][0], params[1][1])
    write(params[2][1], a + b)

    ins_ptr += len(params) + 1

def mult(params):
    global I, ins_ptr

    a = read(params[0][0], params[0][1])
    b = read(params[1][0], params[1][1])
    write(params[2][1], a * b)

    ins_ptr += len(params) + 1

def input(params, override):
    global I, ins_ptr, input_code

    write(params[0][1], override if override is not None else input_code)

    ins_ptr += len(params) + 1

def output(params):
    global I, ins_ptr, input_code

    a = read(params[0][0], params[0][1])
    if a != 0:
        input_code = a

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
        write(params[2][1], 1)
    else:
        write(params[2][1], 0)

    ins_ptr += len(params) + 1

def equals(params):
    global I, ins_ptr

    a = read(params[0][0], params[0][1])
    b = read(params[1][0], params[1][1])

    if a == b:
        write(params[2][1], 1)
    else:
        write(params[2][1], 0)

    ins_ptr += len(params) + 1

def parse(a):
    op = str(a).zfill(5)
    
    return int(op[-2:]), [int(x) for x in op[:-2][::-1]]

def read(m, x):
    global I

    if m == mode.position:
        return I[x]
    else:
        return x

def write(x, i):
    global I

    I[x] = i

def process(I, exit_on_output, signal_used):
    used = signal_used

    while I[ins_ptr] != 99:
        opcode, modes = parse(I[ins_ptr])
        # print(ins_ptr, opcode, modes)

        if opcode == 1:
            add(zip(modes, I[ins_ptr + 1: ins_ptr + 4]))
        elif opcode == 2:
            mult(zip(modes, I[ins_ptr + 1: ins_ptr + 4]))
        elif opcode == 3:
            input(zip(modes, I[ins_ptr + 1:ins_ptr + 2]), signal if not used else None)
            used = True
        elif opcode == 4:
            output(zip(modes, I[ins_ptr + 1: ins_ptr + 2]))
            if exit_on_output:
                return I[0]
        elif opcode == 5:
            jump_if_true(zip(modes, I[ins_ptr + 1: ins_ptr + 3]))
        elif opcode == 6:
            jump_if_false(zip(modes, I[ins_ptr + 1: ins_ptr + 3]))
        elif opcode == 7:
            less_than(zip(modes, I[ins_ptr + 1: ins_ptr + 4]))
        elif opcode == 8:
            equals(zip(modes, I[ins_ptr + 1: ins_ptr + 4]))
        else:
            assert False, I[ins_ptr]

    return I[0]

with open("input.txt") as f:
    I = [int(x) for x in f.read().strip().split(",")]

CI = I[:]

# perms = []

# for a in range(5):
#     for b in [x for x in range(5) if x != a]:
#         for c in [x for x in range(5) if x not in [a, b]]:
#             for d in [x for x in range(5) if x not in [a, b, c]]:
#                 for e in [x for x in range(5) if x not in [a, b, c, d]]:
#                     perms.append((a, b, c, d, e))

# largest = 0

# for x in [perms[0]]:
#     print(CI)
#     input_code = 0

#     for y in x:
#         signal = y
#         ins_ptr = 0
#         I = CI[:]

#         process(I)

#     largest = max(largest, input_code)

# print("Part 1:", largest)

perms = []

for a in range(5, 10):
    for b in [x for x in range(5, 10) if x != a]:
        for c in [x for x in range(5, 10) if x not in [a, b]]:
            for d in [x for x in range(5, 10) if x not in [a, b, c]]:
                for e in [x for x in range(5, 10) if x not in [a, b, c, d]]:
                    perms.append((a, b, c, d, e))

largest = 0
print(perms)

for x in perms:
    input_code = 0
    count = 0

    ins = []

    for _ in range(len(x)):
        i = CI[:]
        ins.append(i)

    amps = zip(x, ins, [0 for _ in range(len(x))])
    # print(amps)
    signal_used = False

    while any(t[1][t[2]] != 99 for t in amps):
        # print([t[1][0] for t in amps])
        # print(amps[count])
        signal = amps[count][0]

        ins_ptr = amps[count][2]
        I = amps[count][1]

        process(I, True, signal_used)

        amps[count] = (input_code, I[:], int(ins_ptr))

        if count == len(amps) - 1:
            signal_used = True

        count = (count + 1) % len(amps)

    print(",".join([str(t) for t in x]), input_code)
    largest = max(largest, input_code)
    print(amps)

print("Part 2:", largest)



























