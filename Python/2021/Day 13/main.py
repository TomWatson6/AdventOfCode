

def fold(dots, instruction):
    result = dict()

    direction, line = instruction.split("=")

    for k in dots.keys():
        if direction == 'y':
            if k[1] > int(line):
                y = int(line) - (k[1] - int(line))
                result[(k[0], y)] = True
            else:
                result[k] = True
        else:
            if k[0] > int(line):
                x = int(line) - (k[0] - int(line))
                result[(x, k[1])] = True
            else:
                result[k] = True
    return result


def p1(output):
    print("Part 1:", output)

def p2(output):
    print("Part 2:", output)

def print_dots(dots, path):
    x_max = max([x[0] for x in dots.keys()]) + 1
    y_max = max([x[1] for x in dots.keys()]) + 1

    file = open(path, 'w')

    for y in range(y_max):
        for x in range(x_max):
            if dots.get((x, y)) == True:
                file.write('#')
            else:
                file.write(' ')
        file.write("\r\n")
    file.close()

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

dot_coords = [tuple([int(y) for y in x.strip().split(",")]) for x in lines if x != "" and not x.startswith("fold")]
instructions = [x.strip()[11:] for x in lines if x.startswith("fold")]

dots = dict()

for d in dot_coords:
    dots[d] = True

result = fold(dots, instructions[0])

p1(len(result))

dots = dict()

for d in dot_coords:
    dots[d] = True

for i in instructions:
    dots = fold(dots, i)

print_dots(dots, 'output.txt')
