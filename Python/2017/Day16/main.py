
with open(0) as f:
    moves = f.read().strip().split(",")

programs = list("abcdefghijklmnop") if len(moves) > 5 else list("abcde")
S = set()
S.add("".join(programs))
ITERS = 1000000000
i = 0
cycled = False

while i < ITERS:
    for move in moves:
        if move[0] == 's':
            amt = int(move[1:])
            programs = programs[-amt:] + programs[:-amt]
        elif move[0] == 'x':
            a, b = list(map(int, move[1:].split("/")))
            programs[a], programs[b] = programs[b], programs[a]
        elif move[0] == 'p':
            a, b = move[1:].split("/")
            a, b = programs.index(a), programs.index(b)
            programs[a], programs[b] = programs[b], programs[a]
        else:
            assert False

    if i == 0:
        print("Part 1:", "".join(programs))

    i += 1

    key = "".join(programs)
    if key in S and not cycled:
        cycled = True
        rem_cycles = (ITERS - i - 1) // i
        i += rem_cycles * i

    S.add(key)

print("Part 2:", "".join(programs))



















