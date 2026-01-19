from collections import Counter

input = open("input.txt").read().strip()

def parse(input: str):
    lines = input.splitlines()

    codes = []

    for left, right in [x.split('[') for x in lines]:
        checksum = right.strip(']')
        *name, id_ = left.split('-')
        id_ = int(id_)
        name = "-".join(name)
        codes.append((name, id_, checksum))

    return codes

def check(name, checksum):
    occ = Counter(name)
    c = "".join([x[0] for x in sorted(occ.items(),
                                      key = lambda o: (o[1], ord('z') - ord(o[0])),
                                      reverse = True)][:5])
    return checksum == c

def part1(input: str) -> int:
    codes = parse(input)
    total = 0

    for name, id_, checksum in codes:
        name = "".join(name.split('-'))
        if check(name, checksum):
            total += id_

    return total

def part2(input: str) -> int:
    codes = parse(input)
    new_codes = []

    for name, id_, checksum in codes:
        if check("".join(name.split('-')), checksum):
            new_codes.append((name, id_, checksum))

    codes = new_codes

    for name, id_, _ in codes:
        new_name = ""
        for letter in name:
            if letter == '-':
                new_name += letter
                continue

            l = ord(letter) - ord('a')
            l = (l + id_) % 26
            l += ord('a')
            new_name += chr(l)

        if new_name == "northpole-object-storage":
            return id_

    return 0

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















