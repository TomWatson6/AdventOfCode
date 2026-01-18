import hashlib

input = open("input.txt").read().strip()

def parse(input: str):
    return input

def find_password(door, num_zeros):
    i = 0
    password = ""

    while len(password) < 8:
        test = door + str(i)
        hashed = hashlib.md5(test.encode("utf-8")).hexdigest()

        if hashed.startswith('0' * num_zeros):
            password += hashed[num_zeros]

        i += 1

    return password

def find_password2(door, num_zeros):
    i = 0
    password = ['.'] * 8

    while any(c == '.' for c in password):
        test = door + str(i)
        hashed = hashlib.md5(test.encode("utf-8")).hexdigest()

        if hashed.startswith('0' * num_zeros):
            pos, ch = hashed[num_zeros], hashed[num_zeros + 1]
            if pos.isalpha():
                i += 1
                continue

            pos = int(pos)

            if 0 <= pos < len(password) and password[pos] == '.':
                password[int(pos)] = ch
        i += 1

    return "".join(password)

def part1(input: str) -> int:
    door = parse(input)
    password = find_password(door, 5)

    return password

def part2(input: str) -> int:
    door = parse(input)
    password = find_password2(door, 5)

    return password

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















