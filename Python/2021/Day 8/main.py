
## Identify which sequences map to which numbers
def find_patterns(numbers, patterns):
    mapping = dict()
    simplified_numbers = numbers.copy()
    simplified_numbers = set(simplified_numbers)

    ## Patterns dict: character -> sizes of arrays it appears in
    ## Find similar patterns in current numbers passed in
    numbers_patterns = dict()
    for c in range(97, 104, 1):
        char = chr(c)
        set_sizes = []
        for v in list(simplified_numbers):
            if char in v:
                set_sizes.append(len(v))
        set_sizes.sort()
        numbers_patterns[char] = set_sizes
    return numbers_patterns

##   a
## b   c
##   d
## e   f
##   g
## map the above the the correct letters

number_mapping = dict()
number_mapping[0] = "abcefg"
number_mapping[1] = "cf"
number_mapping[2] = "acdeg"
number_mapping[3] = "acdfg"
number_mapping[4] = "bcdf"
number_mapping[5] = "abdfg"
number_mapping[6] = "abdefg"
number_mapping[7] = "acf"
number_mapping[8] = "abcdefg"
number_mapping[9] = "abcdfg"

string_mapping = dict()
string_mapping["abcefg"] = 0
string_mapping["cf"] = 1
string_mapping["acdeg"] = 2
string_mapping["acdfg"] = 3
string_mapping["bcdf"] = 4
string_mapping["abdfg"] = 5
string_mapping["abdefg"] = 6
string_mapping["acf"] = 7
string_mapping["abcdefg"] = 8
string_mapping["abcdfg"] = 9

patterns = dict()

for c in range(97, 104, 1):
    char = chr(c)
    set_sizes = []
    for v in number_mapping.values():
        if char in v:
            set_sizes.append(len(v))
    set_sizes.sort()
    patterns[char] = set_sizes
        

def p1(output):
    print("Part 1:", output)

def p2(output):
    print("Part 2:", output)

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

sequences = []

for i in range(len(lines)):
    lines[i] = [x.strip() for x in lines[i].split("|")]
    lines[i] = [x.split(" ") for x in lines[i]]
    place_holder = lines[i][0]
    place_holder.append('|')
    [place_holder.append(x) for x in lines[i][1]]
    lines[i] = place_holder
    temp = []
    for l in [x for x in lines[i] if x != '|']:
        l = "".join(sorted(l))
        temp.append(l)
    sequences.append(temp)

#print(sequences)

seq = []

for i in range(len(lines)):
    numbers_patterns = find_patterns(sequences[i], patterns)

    char_map = dict()

    for k, v in numbers_patterns.items():
        for k1, v1 in patterns.items():
            if v == v1:
                char_map[k] = k1
                break

    output = []

    for l in lines[i]:
        if l == '|':
            output.append(l)
        else:
            new_str = ""
            for c in l:
                new_str += char_map[c]
            output.append(new_str)
    for o in range(len(output)):
        if output[o] != '|':
            output[o] = string_mapping["".join(sorted(output[o]))]

    seq.append(output)

total = 0

for s in seq:
    pipe_found = False
    for item in s:
        if pipe_found:
            total += 1 if item in [1, 4, 7, 8] else 0
        elif item == '|':
            pipe_found = True

p1(total)

total = 0

for s in seq:
    pipe_found = False
    output = ""
    for item in s:
        if pipe_found:
            output = output + str(item)
        elif item == '|':
            pipe_found = True
    total += int(output)

p2(total)