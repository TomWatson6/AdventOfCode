from collections import deque
import z3

input = open("input.txt").read().strip()

def parse(input: str):
    lines = input.splitlines()
    machines = []

    for lights, *buttons, joltage in [line.split() for line in lines]:
        lights = lights[1:-1]
        buttons = [list(map(int, button[1:-1].split(','))) for button in buttons]
        joltages = list(map(int, joltage[1:-1].split(',')))
        machines.append((lights, buttons, joltages))

    return machines

def find(machine):
    lights, buttons, _ = machine

    queue = deque([("".join(['.' for _ in range(len(lights))]), 0)])
    seen = set()

    while queue:
        curr, presses = queue.popleft()

        if curr == lights:
            return presses

        if curr in seen:
            continue

        seen.add(curr)

        for button in buttons:
            new_lights = ""

            for i in range(len(curr)):
                if i in button:
                    new_lights += '.' if curr[i] == '#' else '#'
                else:
                    new_lights += curr[i]

            queue.append((new_lights, presses + 1))

    return 0

def solve(buttons, joltages):
    values = []

    for i in range(len(buttons)):
        values.append(z3.Int(f"B{i}"))

    equations = []

    for i in range(len(joltages)):
        terms = []

        for j in range(len(buttons)):
            if i in buttons[j]:
                terms.append(values[j])

        equation = (sum(terms) == joltages[i])
        equations.append(equation)

    total = sum(values)

    output = z3.Optimize()
    output.minimize(total)

    for equation in equations:
        output.add(equation)

    for v in values:
        output.add(v >= 0)

    assert output.check()

    model = output.model()

    ans = 0

    for d in model.decls():
        ans += model[d].as_long()

    return ans

def part1(input: str) -> int:
    machines = parse(input)
    total = 0

    for machine in machines:
        total += find(machine)

    return total

def part2(input: str) -> int:
    machines = parse(input)
    total = 0

    for _, buttons, joltages in machines:
        total += solve(buttons, joltages)

    return total

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















