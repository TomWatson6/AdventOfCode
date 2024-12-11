from collections import defaultdict

input = open("input.txt").read().strip()

def evolve(stones: list[int]) -> list[int]:
    new_stones = []

    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            new_stones.append(int(str(stone)[:len(str(stone)) // 2]))
            new_stones.append(int(str(stone)[len(str(stone)) // 2:]))
        else:
            new_stones.append(stone * 2024)

    return new_stones

def evolve2(stones: dict[int, int]) -> dict[int, int]:
    new_stones = defaultdict(int)

    for k, v in stones.items():
        if k == 0:
            new_stones[1] += v
        elif len(str(k)) % 2 == 0:
            k_str = str(k)
            left = int(k_str[:len(k_str) // 2])
            right = int(k_str[len(k_str) // 2:])
            new_stones[left] += v
            new_stones[right] += v
        else:
            new_stones[k * 2024] += v

    return new_stones

def part1(input: str) -> int:
    stones = [int(x) for x in input.split(' ')]

    for _ in range(25):
        stones = evolve(stones)

    return len(stones)

def part2(input: str) -> int:
    stones = defaultdict(int)

    for stone in [int(x) for x in input.split(' ')]:
        stones[stone] += 1

    for i in range(75):
        stones = evolve2(stones)


    return sum(stones.values())

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















