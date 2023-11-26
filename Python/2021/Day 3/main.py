def get_bit(lines, index, most_common):
    zero = 0
    one = 0
    for y  in range(len(lines)):
        if lines[y][index] == "0":
            zero += 1
        else:
            one += 1
    if one >= zero:
        return "1" if most_common else "0"
    else:
        return "0" if most_common else "1"

def p1(output):
    print("Part 1:", output)

def p2(output):
    print("Part 2:", output)

f = open("input.txt")
lines = [x.strip() for x in f.readlines()]
f.close()

gamma = ""
epsilon = ""

for x in range(len(lines[0])):
    gamma += get_bit(lines, x, True)
    epsilon += get_bit(lines, x, False)

p1(int(gamma, 2) * int(epsilon, 2))

og_ratings = lines.copy()
cs_ratings = lines.copy()

for x in range(len(og_ratings[0])):
    most_common = get_bit(og_ratings, x, True)
    og_ratings = [r for r in og_ratings if r[x] == most_common]
    if len(og_ratings) == 1:
        break

for x in range(len(cs_ratings[0])):
    least_common = get_bit(cs_ratings, x, False)
    cs_ratings = [r for r in cs_ratings if r[x] == least_common]
    if len(cs_ratings) == 1:
        break

p2(int(og_ratings[0], 2) * int(cs_ratings[0], 2))