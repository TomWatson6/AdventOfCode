
input = open("input.txt").read().strip()

def parse(input: str):
    return input.splitlines()

def part1(input: str) -> int:
    instructions = parse(input)

    cards = [i for i in range(10007)]

    for ins in instructions:
        if ins.startswith("cut"):
            n = int(ins.split()[-1])
            cards = cards[n:] + cards[:n]
        elif ins.startswith("deal with increment"):
            n = int(ins.split()[-1])
            new_cards = list(cards)
            for i in range(len(new_cards)):
                new_cards[(i * n) % len(new_cards)] = cards[i]
            cards = new_cards
        elif ins == "deal into new stack":
            cards = cards[::-1]

    return cards.index(2019)

def inv(a, n): return pow(a, n-2, n)

def part2(input: str) -> int:
    instructions = parse(input)

    amount = 119315717514047
    shuffles = 101741582076661
    a, b = 1, 0

    for ins in instructions:
        la, lb = 0, 0

        if ins.startswith("cut"):
            n = int(ins.split()[-1])
            la, lb = 1, -n
        elif ins.startswith("deal with increment"):
            n = int(ins.split()[-1])
            la, lb = n, 0
        elif ins == "deal into new stack":
            la, lb = -1, -1

        a = (la * a) % amount
        b = (la * b + lb) % amount

    ma = pow(a, shuffles, amount)
    mb = (b * (ma - 1) * inv(a-1, amount)) % amount

    return ((2020 - mb) * inv(ma, amount)) % amount

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















