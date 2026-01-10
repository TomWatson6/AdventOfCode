
input = open("input.txt").read().strip()

def parse(input: str):
    return [int(x) for x in list(input.strip())]

def part1(input: str) -> int:
    numbers = parse(input)
    image_size = 25 * 6
    layers = {}

    for i in range(0, len(numbers), image_size):
        layer = numbers[i:i + image_size]
        layers[len([x for x in layer if x == 0])] = len([x for x in layer if x == 1]) * len([x for x in layer if x == 2])

    layers = sorted(layers.items(), key = lambda l: l[0])

    return layers[0][1]

def part2(input: str) -> int:
    numbers = parse(input)
    width = 25
    height = 6
    image_size = width * height
    layers = len(numbers) // image_size

    at = lambda l, r, c: l * width * height + r * width + c
    ans = []

    for r in range(height):
        row = ""
        for c in range(width):
            for l in range(len(numbers) // image_size):
                if numbers[at(l, r, c)] == 0:
                    row += ' '
                elif numbers[at(l, r, c)] == 1:
                    row += '#'
                else:
                    continue
                break

        ans.append(row)

    return "\n".join(ans)

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:\n", part2(input), sep="")















