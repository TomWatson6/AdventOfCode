
with open(0) as f:
    lines = [x.strip() for x in f.readlines()]

def get_num_cards(id_, winning_cards, memo):
    if id_ in memo:
        return memo[id_]

    total = 0

    if id_ in winning_cards:
        total += winning_cards[id_]

        for idx in range(id_ + 1, winning_cards[id_] + id_ + 1):
            total += get_num_cards(idx, winning_cards, memo)

        memo[id_] = total
        return total

    return 0

total = 0
cards = []
winning_cards = {}

for line in lines:
    left, right = line.split(" | ")
    all_left = [x for x in left.split(" ") if x != ""]
    left = all_left[2:]
    id_ = int(all_left[1].strip(":"))
    winning = [int(x.strip()) for x in left if x != ""]
    owned = [int(x.strip()) for x in right.split(" ") if x != ""]

    cards.append((id_, (winning, owned)))

    count = 0
    nums = []

    for num in owned:
        if num in winning:
            nums.append(num)
            count += 1

    if count > 0:
        total += 2**(count - 1)
        winning_cards[id_] = count

print("Part 1:", int(total))

total = len(cards)

for id_ in winning_cards.keys():
    total += get_num_cards(id_, winning_cards, {})

print("Part 2:", total)




















