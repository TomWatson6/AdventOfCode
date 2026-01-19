
input = open("input.txt").read().strip()

def parse(input: str):
    return [int(x) for x in input.strip().split('-')]

def valid(password):
    v = True
    v = v and any(a == b for a, b in zip(password, password[1:]))
    v = v and all(a <= b for a, b in zip(password, password[1:]))
    return v

def valid2(password):
    v = True

    C = []
    prev = ""
    curr = 0

    for p in password:
        if p != prev:
            C.append(curr + 1)
            curr = 0
        else:
            curr += 1

        prev = p

    C.append(curr + 1)

    v = v and any(c == 2 for c in C)
    v = v and all(a <= b for a, b in zip(password, password[1:]))

    return v

def part1(input: str) -> int:
    lower, upper = parse(input)
    ans = 0

    for i in range(lower, upper + 1):
        ans += valid(str(i))

    return ans

def part2(input: str) -> int:
    lower, upper = parse(input)
    ans = 0

    for i in range(lower, upper + 1):
        ans += valid2(str(i))

    return ans

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















