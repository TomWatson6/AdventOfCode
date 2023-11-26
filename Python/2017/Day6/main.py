
with open("input.txt") as f:
    stacks = [int(x.strip()) for x in f.read().split(" ")]

configs = set()
count = 0
p1 = 0
seen = ""

while True:
    config = "|".join([str(x) for x in stacks])
    if config == seen:
        break
    if p1 == 0 and config in configs:
        p1 = count
        seen = config
    configs.add(config)

    max_num = max(stacks)
    max_indexes = [i for i, x in enumerate(stacks) if x == max_num]
    max_index = min(max_indexes)
    
    stacks[max_index] = 0

    for i in range(max_num):
        stacks[(max_index + i + 1) % len(stacks)] += 1

    count += 1

print("Part 1:", p1)
print("Part 2:", count - p1)











