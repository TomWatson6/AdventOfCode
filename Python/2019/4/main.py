
def never_decrease(number):
    n = str(number)

    for a, b in zip(n[:-1], n[1:]):
        if a > b:
            return False
        
    return True

def two_adjacent(number):
    n = str(number)

    for a, b in zip(n[:-1], n[1:]):
        if a == b:
            return True
        
    return False

def two_adjacent_p2(number):
    n = str(number)

    curr = 1
    last = n[0]
    counts = []

    for x in n[1:]:
        if x != last:
            counts.append(curr)
            curr = 0
        curr += 1
        last = x

    counts.append(curr)

    return any([x == 2 for x in counts])

with open("input.txt") as f:
    lower, upper = [int(x) for x in f.read().strip().split("-")]

count = 0
count2 = 0

for x in range(lower, upper):
    if all([never_decrease(x), two_adjacent(x)]):
        count += 1

    if all([never_decrease(x), two_adjacent_p2(x)]):
        print(x)
        count2 += 1

print("Part 1:", count)
print("Part 2:", count2)

















