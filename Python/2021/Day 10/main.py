

def p1(output):
    print("Part 1:", output)

def p2(output):
    print("Part 2:", output)

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

total_corr = 0
score = 0
incomplete = []

scoring = dict()
scoring[')'] = 3
scoring[']'] = 57
scoring['}'] = 1197
scoring['>'] = 25137

bracket_map = dict()
bracket_map['('] = ')'
bracket_map['['] = ']'
bracket_map['{'] = '}'
bracket_map['<'] = '>'

for line in lines:
    stack = []
    corrupted = False
    for c in line:
        if c in ['(', '[', '{', '<']:
            stack.append(c)
        elif c == bracket_map[stack[-1]]:
            stack.pop()
        else:
            corrupted = True
            score += scoring[c]
            break
    if len(stack) > 0 and not corrupted:
        incomplete.append(line)
    if corrupted:
        total_corr += 1

p1(score)

char_values = dict()
char_values[')'] = 1
char_values[']'] = 2
char_values['}'] = 3
char_values['>'] = 4

totals = []

for line in incomplete:
    total = 0
    stack = []
    for c in line:
        if c in ['(', '[', '{', '<']:
            stack.append(c)
        elif c == bracket_map[stack[-1]]:
            stack.pop()
    stack.reverse()
    for c in stack:
        char = bracket_map[c]
        total *= 5
        total += char_values[char]
    totals.append(total)

totals.sort()
p2(totals[len(totals) // 2])