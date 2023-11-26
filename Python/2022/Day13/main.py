with open("input.txt") as f:
    pairs = [x.split("\n") for x in f.read().strip().split("\n\n")]

def is_correct_order(left, right):
    i = 0

    while i < len(left) and i < len(right):
        left_type = 1 if hasattr(left[i], "__len__") else 0
        right_type = 1 if hasattr(right[i], "__len__") else 0
        outcome = None

        if left_type == 1 or right_type == 1:
            if left_type == 1:
                if right_type == 1:
                    outcome = is_correct_order(left[i], right[i])
                else:
                    outcome = is_correct_order(left[i], [right[i]])
            else:
                outcome = is_correct_order([left[i]], right[i])

            if outcome is not None:
                return outcome

            i += 1
            continue

        if left[i] < right[i]:
            return True
        elif left[i] > right[i]:
            return False

        i += 1

    if len(left) < len(right):
        return True
    elif len(left) > len(right):
        return False

total = 0

for i, pair in enumerate(pairs):
    left = eval(pair[0])
    right = eval(pair[1])

    if is_correct_order(left, right):
        total += i + 1

print("Part 1:", total)

packets = []

for pair in pairs:
    packets.append(pair[0])
    packets.append(pair[1])

div1 = [[2]]
div2 = [[6]]

loc1 = 1
loc2 = 2

for p in packets:
    pack = eval(p)

    if is_correct_order(pack, div1):
        loc1 += 1
    if is_correct_order(pack, div2):
        loc2 += 1

print("Part 2:", loc1 * loc2)



