

f = open("input.txt")
numbers = [x.strip() for x in f.readlines()]
f.close()

numbers = [x.strip("+") for x in numbers]
numbers = [int(x) for x in numbers]

final = 0
seen = dict()

for number in numbers:
    final += number

print("Part 1:", final)

cumulative_frequency = 0
x = 0

while True:
    if(seen.get(cumulative_frequency)):
        break

    seen[cumulative_frequency] = True

    cumulative_frequency += numbers[x % len(numbers)]
    x += 1

print("Part 2:", cumulative_frequency)