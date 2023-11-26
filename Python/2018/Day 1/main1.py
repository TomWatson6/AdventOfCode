
with open("input.txt") as f:
    numbers = [int(x) for x in f.readlines()]
    total = sum(numbers)

    print("Part 1:", total)

    curr = 0
    i = 0
    s = set()

    while True:
        curr += numbers[i]

        if curr in s:
            print("Part 2:", curr)
            break

        s.add(curr)
        i = (i + 1) % len(numbers)




















