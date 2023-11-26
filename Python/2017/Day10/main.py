
def reverse_segment(numbers, start, end):
    start = start % len(numbers)
    end = end % len(numbers)
    segment = []

    if end >= start:
        return numbers[0:start] + numbers[start:end][::-1] + numbers[end:len(numbers)]

    segment = numbers[start:len(numbers)] + numbers[0:end]
    segment = segment[::-1]

    last = len(numbers) - start

    numbers[start:len(numbers)] = segment[0:last]
    numbers[0:end] = segment[last:len(segment)]

    return numbers

def dense_hash(numbers):
    dense = []

    for i in range(len(numbers) // 16):
        segment = numbers[i * 16:i * 16 + 16]
        segment = " ^ ".join([str(x) for x in segment])
        num = eval(segment)
        dense.append(num)

    return dense

p2_instructions = []

with open("input.txt") as f:
    input = f.read()
    instructions = [int(x.strip()) for x in input.split(",")]

for i in input:
    p2_instructions.append(ord(i))

p2_instructions += [17, 31, 73, 47, 23]

skip_size = 0
pos = 0
numbers = [x for x in range(256)]

for inst in instructions:
    numbers = reverse_segment(numbers, pos, pos + inst)
    pos += inst + skip_size
    skip_size += 1

print("Part 1:", str(numbers[0] * numbers[1]))

skip_size = 0
pos = 0
numbers = [x for x in range(256)]

for _ in range(64):
    for inst in p2_instructions:
        numbers = reverse_segment(numbers, pos, pos + inst)
        pos += inst + skip_size
        skip_size += 1

dense = dense_hash(numbers)

output = "".join([hex(x)[2:].zfill(2) for x in dense])
print(output)















