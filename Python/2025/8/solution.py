
input = open("input.txt").read().strip()

def parse(input: str):
    return [tuple(map(int, x.split(","))) for x in input.splitlines()]

def distance(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2

def connect(coords, p2):
    circuits = []
    distances = {}

    for i in range(len(coords) - 1):
        for j in range(i + 1, len(coords)):
            distances[(coords[i], coords[j])] = distance(coords[i], coords[j])

    distances = sorted(distances.items(), key = lambda o: o[1])

    connections = 0
    considered = set()
    required = 1000 if len(coords) == 1000 else 10

    for (a, b), _ in distances:
        if connections == required and not p2:
            break

        found = False

        if a in considered and b in considered:
            left = None
            right = None

            for c in circuits:
                if not left and a in c:
                    left = c
                if not right and b in c:
                    right = c

            if not left or not right:
                assert False

            if left == right:
                connections += 1
                continue

            combined = left | right

            circuits.remove(left)
            circuits.remove(right)
            circuits.append(combined)

            if len(circuits[0]) == len(coords) and p2:
                return a[0] * b[0]

            connections += 1
        else:
            considered.add(a)
            considered.add(b)

            for c in circuits:
                if a in c:
                    found = True
                    if b in c:
                        found = False
                        break

                    c.add(b)
                    if len(circuits[0]) == len(coords) and p2:
                        return a[0] * b[0]
                    break

                if b in c:
                    found = True
                    if a in c:
                        found = False
                        break

                    c.add(a)
                    if len(circuits[0]) == len(coords) and p2:
                        return a[0] * b[0]
                    break
            else:
                found = True
                circuits.append(set([a, b]))

            if found:
                connections += 1

    circuits = sorted(circuits, key = lambda c: len(c), reverse = True)

    if not p2:
        return circuits

def part1(input: str) -> int:
    coords = parse(input)
    circuits = connect(coords, False)

    product = 1

    for c in circuits[:3]:
        product *= len(c)

    return product

def part2(input: str) -> int:
    coords = parse(input)
    ans = connect(coords, True)

    return ans

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















