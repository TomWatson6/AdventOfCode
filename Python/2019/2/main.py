
def add(a, b, c):
    global I

    I[c] = I[a] + I[b]
    return 4

def mult(a, b, c):
    global I

    I[c] = I[a] * I[b]
    return 4

with open("input.txt") as f:
    I = [int(x) for x in f.read().strip().split(",")]

CI = I[:]
I[1] = 12
I[2] = 2

def process(I):
    index = 0
    
    while I[index] != 99:
        if I[index] == 1:
            index += add(I[index + 1], I[index + 2], I[index + 3])
        elif I[index] == 2:
            index += mult(I[index + 1], I[index + 2], I[index + 3])
        else:
            assert False, I[index]

    return I[0]

print("Part 1:", process(I))

required_output = 19690720

for x in range(99):
    for y in range(99):
        I = CI[:]
        I[1] = x
        I[2] = y

        if process(I) == required_output:
            print("Part 2:", 100 * x + y)
            exit(0)




















