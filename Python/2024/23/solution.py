from collections import defaultdict, Counter

input = open("input.txt").read().strip()

def parse_input(input):
    lines = input.splitlines()
    conn = defaultdict(list)

    for line in lines:
        left, right = line.split("-")
        conn[left].append(right)
        conn[right].append(left)

    return conn

def find_groups(conn):
    groups = set()

    for k, v in conn.items():
        for i in range(len(v) - 1):
            for j in range(i + 1, len(v)):
                if v[j] in conn[v[i]] and v[i] in conn[v[j]]:
                    groups.add(tuple(sorted([k, v[i], v[j]])))

    return [g for g in groups if any(t.startswith('t') for t in g)]

def find_connected_groups(conn):
    output = set()

    for k, v in conn.items():
        connections = defaultdict(int)

        for val in v:
            c = set()
            c.add(val)

            for va in [t for t in v if t != val]:
                if val in conn[va]:
                    c.add(va)

            c.add(k)
            connections[",".join(tuple(sorted(c)))] += 1

        connections = [k for k, v in connections.items() if v == len(k.split(",")) - 1]

        if len(connections) > 0:
            output.add(max(connections, key=len))

    return output


def part1(input: str) -> int:
    conn = parse_input(input)
    groups = find_groups(conn)

    return len(groups)

def part2(input: str) -> int:
    conn = parse_input(input)
    groups = find_connected_groups(conn)

    return max(groups, key = lambda k: len(k))

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















