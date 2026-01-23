import re
from collections import deque
from copy import deepcopy

input = open("input.txt").read().strip()

def parse(input: str):
    floors = []
    
    for i, line in enumerate(input.splitlines()):
        microchips = list(re.findall(r"\w+(?=\-compatible microchip)", line))
        microchips = [(Type.Microchip, m) for m in microchips]

        generators = list(re.findall(r"\w+(?= generator)", line))
        generators = [(Type.Generator, g) for g in generators]

        floors.append([*microchips, *generators])

    return floors

class Type:
    Generator = 0
    Microchip = 1

def is_safe(floors):
    safe = True
    for floor in floors:
        microchips = [f for f in floor if f[0] == Type.Microchip]
        generators = [f for f in floor if f[0] == Type.Generator]

        if not all(m[1] in [g[1] for g in generators] for m in microchips) and len(generators) > 0:
            return False

        if any(m[1] not in [g[1] for g in generators] and len(generators) > 0 for m in microchips):
            return False

    return True

def final_state(floors):
    if all(len(f) == 0 for i, f in enumerate(floors) if i != len(floors) - 1):
        return True

    return False

def bfs(floors):
    queue = deque([(floors, 0, 0)])
    seen = set()

    while queue:
        state, elevator, steps = queue.popleft()

        if final_state(state):
            return steps

        key = tuple([elevator, tuple(tuple(t[0] for t in s) for s in state)])

        if key in seen:
            continue

        seen.add(key)

        for i in [-1, 1]:
            if all(len(s) == 0 for s in state[:elevator]) and i == -1:
                continue

            if 0 <= elevator + i < len(state):
                for a in range(len(state[elevator])):
                    new_state = list([list(s) for s in state])
                    new_state[elevator + i].append(state[elevator][a])
                    new_state[elevator].remove(state[elevator][a])

                    if is_safe(new_state):
                        queue.append((new_state, elevator + i, steps + 1))

                if len(state[elevator]) > 1:
                    for a in range(len(state[elevator]) - 1):
                        for b in range(a + 1, len(state[elevator])):
                            new_state = list([list(s) for s in state])
                            new_state[elevator + i].append(state[elevator][a])
                            new_state[elevator + i].append(state[elevator][b])
                            new_state[elevator].remove(state[elevator][b])
                            new_state[elevator].remove(state[elevator][a])

                            if is_safe(new_state):
                                queue.append((new_state, elevator + i, steps + 1))

    return 0

def part1(input: str) -> int:
    floors = parse(input)

    return bfs(floors)

def part2(input: str) -> int:
    floors = parse(input)
    floors[0] += [(0, 'elerium'), (1, 'elerium'), (0, 'dilithium'), (1, 'dilithium')]

    return bfs(floors)

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















