
input = open("input.txt").read().strip()

def parse_input(input: str) -> list[str]:
    # 123 -> 0..222
    output = []
    for i in range(0, len(input), 2):
        used = input[i]
        for _ in range(int(used)):
            output.append(str(i // 2))
        if i == len(input) - 1:
            break
        free = input[i + 1]
        for _ in range(int(free)):
            output.append('.')

    return output

def parse_input2(input: str) -> list[list[str]]:
    # 123 -> [['0'], ['.' '.'], ['1', '1', '1']]
    output = []
    for i in range(0, len(input), 2):
        used = input[i]
        used_arr = []
        for _ in range(int(used)):
            used_arr.append(str(i // 2))
        output.append(used_arr)
        if i == len(input) - 1:
            break
        free = input[i + 1]
        free_arr = []
        for _ in range(int(free)):
            free_arr.append('.')
        output.append(free_arr)

    return output

def compact(disk: list[str]) -> list[str]:
    left = 0
    right = len(disk) - 1

    while left <= right:
        while disk[left] != '.':
            left += 1
        while disk[right] == '.':
            right -= 1
        disk[left], disk[right] = disk[right], disk[left]

    return [d for d in disk if d != '.']

def compact2(disk: list[list[str]]) -> list[list[str]]:
    left = 0
    right = len(disk) - 1
    considered = set()
    to_consider = 0

    for d in [di for di in disk if len(di) > 0]:
        if d[0] == '.':
            continue
        to_consider += 1

    while True:
        while (len(disk[right]) > 0 and disk[right][0] in considered) or disk[right][0] == '.':
            if right < 0:
                break
            right -= 1
        while len(disk[left]) < len(disk[right]) or disk[left][0] != '.':
            if left >= right:
                break
            left += 1

        new_part = []
        leftovers = []

        for i in range(len(disk[left])):
            if i < len(disk[right]):
                new_part.append(disk[right][i])
            else:
                leftovers.append(disk[left][i])

        considered.add(disk[right][0])

        if left != right:
            disk = disk[:left] + [new_part] + [leftovers] + disk[left + 1:right] + [['.' for _ in range(len(disk[right]))]] + disk[right + 1:]

        disk = remove_fragmentation(disk)
        left = 0
        right = len(disk) - 1

        if len(considered) == to_consider:
            break

    return disk

def remove_fragmentation(disk: list[list[str]]) -> list[list[str]]:
    new_disk = []
    nxt = []

    for d in disk:
        if len(d) == 0:
            continue
        elif '.' in d:
            nxt += d
            continue
        elif len(nxt) != 0:
            new_disk.append(nxt)
            nxt = []

        if '.' not in d:
            new_disk.append(d)

    return new_disk

def checksum(disk: list[str]) -> int:
    total = 0

    for i, d in enumerate(disk):
        if d == '.':
            continue
        total += i * int(d)

    return total

def part1(input: str) -> int:
    disk = parse_input(input)
    disk = compact(disk)

    return checksum(disk)

def part2(input: str) -> int:
    disk = parse_input2(input)
    disk = compact2(disk)
    flattened = [l for sublist in disk for l in sublist]
    return checksum(flattened)

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















