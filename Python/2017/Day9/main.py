
with open("input.txt") as f:
    chars = f.read().strip()

i = 0
score = 0
depth = 1
garbage = False
count = 0

while i < len(chars):
    c = chars[i]
    if c == '!':
        i += 2
        continue

    if not garbage:
        if c == '{':
            score += depth
            depth += 1
        if c == '}':
            depth -= 1
        if c == '<':
            garbage = True
    elif c == '>':
        garbage = False
    elif garbage:
        count += 1

    i += 1

print("Part 1:", score)
print("Part 2:", count)















