
with open("input.txt") as f:
    polymer = f.read().strip()

def solve(polymer):
    done = False

    while not done:
        R = set()
        i = 0
        done = True

        while i < len(polymer) - 1:
            left, right = polymer[i:i+2]
            if left.lower() == right.lower():
                if (left.isupper() and right.islower()) or (left.islower() and right.isupper()):
                    R.add(i)
                    R.add(i + 1)
                    done = False
                    i += 1

            i += 1

        new_polymer = ""

        for p in range(len(polymer)):
            if p not in R:
                new_polymer += polymer[p]

        polymer = str(new_polymer)

    return len(polymer)

print("Part 1:", solve(polymer))

P = {}

for i in range(ord('a'), ord('z') + 1):
    p = polymer.replace(chr(i), '')
    p = p.replace(chr(i - 32), '')
    output = solve(p)
    P["".join([chr(i - 32), chr(i)])] = output

ans = min(P.values())

print("Part 2:", ans)















