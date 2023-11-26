
def move(numbers, index, amount):
    i = int(index)
    val = abs(amount) % (len(numbers) - 1)
    val = val if amount > 0 else -val

    goal = (index + val) % len(numbers)

    wrap = lambda t: (t + (1 if amount > 0 else -1)) % len(numbers)

    while i != goal:
        n = wrap(i)
        numbers[i], numbers[n] = numbers[n], numbers[i]
        i = wrap(i)

with open("input.txt") as f:
    numbers = [int(x.strip()) for x in f.readlines()]
    numbers = list(enumerate(numbers))

M = len(numbers)

for i in range(M):
    n = [(index, x) for index, x in enumerate(numbers) if x[0] == i][0]
    move(numbers, n[0], n[1][1])

start_index = [i for i, x in enumerate(numbers) if x[1] == 0][0]

total = 0

for i in range(start_index + 1000, start_index + 3001, 1000):
    index = i % M
    total += numbers[index][1]

print("Part 1:", total)

with open("input.txt") as f:
    numbers = [int(x.strip()) for x in f.readlines()]
    numbers = list(enumerate(numbers))

M = len(numbers)
decryption_key = 811589153

for _ in range(10):
    for i in range(M):
        n = [(index, x) for index, x in enumerate(numbers) if x[0] == i][0]
        move(numbers, n[0], n[1][1] * decryption_key)

start_index = [i for i, x in enumerate(numbers) if x[1] == 0][0]

total = 0

for i in range(start_index + 1000, start_index + 3001, 1000):
    index = i % M
    total += numbers[index][1] * decryption_key

print("Part 2:", total)









