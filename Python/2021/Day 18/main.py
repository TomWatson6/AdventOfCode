
import math

def simplify(pair):
    last_number = -1
    depth = 0
    i = 0
    ## Check for explosions
    while i < len(pair):
        if pair[i] == '[':
            depth += 1
        elif pair[i] == ']':
            depth -= 1
        elif pair[i] != ',':
            if depth > 4 and pair[i + 1] != ']' and pair[i + 3] == ']':
                ## EXPLODE ONLY IF FORMAT [A,B]
                if last_number != -1:
                    pair[last_number] = str(int(pair[last_number]) + int(pair[i]))
                i += 2
                end = i + 1
                while end < len(pair):
                    if pair[end] not in ['[', ']', ',']:
                        pair[end] = str(int(pair[end]) + int(pair[i]))
                        break
                    end += 1
                pair[i - 3] = '0'
                del pair[i - 2: i + 2]
                return pair
            else:
                last_number = i
        i += 1
    i = 0
    depth = 0
    ## Check for splits
    while i < len(pair):
        if pair[i] not in ['[', ']', ',']:
            if len(pair[i]) > 1:
                ## SPLITTING TIME
                num = int(pair[i])
                left = math.floor(num / 2)
                right = math.ceil(num / 2)
                insertion = ['[', str(left), ',', str(right), ']']
                del pair[i]
                for s in range(5):
                    pair.insert(i + s, insertion[s])
                return pair 
        i += 1
    return pair

def find_magnitude(pairs, is_outer):
    totals = []
    comma_seen = False
    pos = 0
    while pos < len(pairs):
        value = 0
        if pairs[pos] == '[': 
            nesting_level = 1
            end = pos + 1
            while nesting_level > 0:
                if pairs[end] == '[':
                    nesting_level += 1
                elif pairs[end] == ']':
                    nesting_level -= 1
                end += 1
            totals.append(find_magnitude(pairs[pos + 1:end - 1], False))
            pos = end
        elif pairs[pos] != ',':
            totals.append(int(pairs[pos]))

        pos += 1
    
    if len(totals) > 1:
        return (totals[0] * 3) + (totals[1] * 2)
    else:
        return totals[0]

def p1(output):
    print("Part 1:", output)

def p2(output):
    print("Part 2:", output)

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

for i in range(len(lines) - 1):
    line = '[' + "".join(lines[i]) + ',' + "".join(lines[i + 1]) + ']'
    while True:
        temp = "".join([x for x in line])
        line = simplify([x for x in line])

        if temp == "".join(line):
            break
    lines[i + 1] = line

magnitude = find_magnitude(lines[-1], True)

p1(magnitude)
magnitudes = []

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

for i1 in range(len(lines) - 1):
    for i2 in range(1, len(lines), 1):
        line = '[' + "".join(lines[i1]) + ',' + "".join(lines[i2]) + ']'
        while True:
            temp = "".join([x for x in line])
            line = simplify([x for x in line])

            if temp == "".join(line):
                break

        magnitudes.append(find_magnitude(line, True))

        line = '[' + "".join(lines[i2]) + ',' + "".join(lines[i1]) + ']'
        while True:
            temp = "".join([x for x in line])
            line = simplify([x for x in line])

            if temp == "".join(line):
                break

        magnitudes.append(find_magnitude(line, True))

magnitude = max(magnitudes)

p2(magnitude)

