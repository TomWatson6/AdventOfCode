
input = open("input.txt").read().strip()

def parse(input: str):
    lines = input.splitlines()
    sequences = []

    for line in lines:
        ins = []
        out = []
        inside = False
        nxt = ""

        for ch in line:
            if ch == '[':
                inside = True
                out.append(nxt)
                nxt = ""
                continue

            elif ch == ']':
                inside = False
                ins.append(nxt)
                nxt = ""
                continue

            nxt += ch

        if inside:
            ins.append(nxt)
        else:
            out.append(nxt)

        sequences.append((ins, out))

    return sequences

def abba(letters):
    for i in range(len(letters) - 3):
        j = i + 4
        segment = letters[i:j]
        if segment[0] == segment[1]:
            continue

        if segment[:len(segment) // 2] == segment[len(segment) // 2:][::-1]:
            return True

    return False

def bab(letters):
    abas = []

    for i in range(len(letters) - 2):
        j = i + 3
        segment = letters[i:j]

        if segment[0] == segment[2] and segment[1] != segment[0]:
            abas.append(segment)

    return [a[1] + a[0] + a[1] for a in abas]

def part1(input: str) -> int:
    sequences = parse(input)
    total = 0

    for ins, out in sequences:
        if any(abba(i) for i in ins):
            continue

        if any(abba(o) for o in out):
            total += 1

    return total

def part2(input: str) -> int:
    sequences = parse(input)
    total = 0

    for ins, out in sequences:
        babs = [bab(o) for o in out]
        babs = [a for b in babs for a in b]
        total += any(any(b in i for i in ins) for b in babs)

    return total

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















