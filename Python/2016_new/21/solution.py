
input = open("input.txt").read().strip()

PASSWORD = "abcdefgh"

def parse(input: str):
    return input.splitlines()

def scramble(instructions, password = None, backwards = False):
    if password is None:
        password = list(PASSWORD)

    for ins in instructions:
        parts = ins.split()
        if ins.startswith("swap position"):
            a, b = int(parts[2]), int(parts[5])
            password[a], password[b] = password[b], password[a]

        if ins.startswith("swap letter"):
            a, b = password.index(parts[2]), password.index(parts[5])
            password[a], password[b] = password[b], password[a]

        if ins.startswith("rotate left"):
            x = int(parts[2])

            for _ in range(x):
                if backwards:
                    password = password[-1:] + password[:-1]
                else:
                    password = password[1:] + password[:1]

        if ins.startswith("rotate right"):
            x = int(parts[2])

            for _ in range(x):
                if backwards:
                    password = password[1:] + password[:1]
                else:
                    password = password[-1:] + password[:-1]

        if ins.startswith("rotate based"):
            x = password.index(parts[6])
            mappings = {1: 1, 3: 2, 5: 3, 7: 4, 2: 6, 4: 7, 6: 0, 0: 1}

            if backwards:
                x = mappings[x]
            else:
                if x >= 4:
                    x += 1
                x += 1

            for _ in range(x):
                if backwards:
                    password = password[1:] + password[:1]
                else:
                    password = password[-1:] + password[:-1]

        if ins.startswith("reverse"):
            a, b = int(parts[2]), int(parts[4])
            password = password[:a] + password[a:b + 1][::-1] + password[b + 1:]

        if ins.startswith("move"):
            a, b = 0, 0

            if backwards:
                b, a = int(parts[2]), int(parts[5])
            else:
                a, b = int(parts[2]), int(parts[5])

            if b > a:
                password = password[:a] + password[a + 1:b + 1] + [password[a]] + password[b + 1:]
            else:
                password = password[:b] + [password[a]] + password[b:a] + password[a + 1:]

    return "".join(password)

def part1(input: str) -> int:
    instructions = parse(input)

    return scramble(instructions)

def part2(input: str) -> int:
    instructions = parse(input)[::-1]

    return scramble(instructions, list("fbgdceah"), True)

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















