from collections import deque, defaultdict, Counter

input = open("input.txt").read().strip()

dists = {
    'A': 0,
    '^': 1,
    '>': 1,
    'v': 2,
    '<': 3,
}

keypad = {
    (0, 0): '7',
    (0, 1): '8',
    (0, 2): '9',
    (1, 0): '4',
    (1, 1): '5',
    (1, 2): '6',
    (2, 0): '1',
    (2, 1): '2',
    (2, 2): '3',
    (3, 1): '0',
    (3, 2): 'A',
}

keypad_start = (3, 2)

dir_keypad = {
    (0, 1): '^',
    (0, 2): 'A',
    (1, 0): '<',
    (1, 1): 'v',
    (1, 2): '>',
}

dir_keypad_start = (0, 2)

DP = {}
DP_BIG = {}

class Robot:
    def __init__(self, inner):
        self.id = inner
        if inner:
            self.robot = Robot(inner - 1)
            self.keypad = dir_keypad
            self.start = dir_keypad_start
        else:
            self.robot = None
            self.keypad = keypad
            self.start = keypad_start

    # Pass press_sequence type ['0239A'] so it matches return type of find_paths
    def press_sequence(self, seq):
        if self.robot is not None:
            seq = self.robot.press_sequence(seq)

        paths = []

        for s in seq:
            if s in DP_BIG:
                paths += DP_BIG[s]
                continue
            addition = self.find_paths(s)
            paths += addition
            DP_BIG[s] = addition

        p = len(min(paths, key=lambda k: len(k)))

        # print(Counter(len(t) for t in paths))

        before = len(paths)
        paths = [t for t in paths if len(t) == p] 
        print("Before reduction:", before, "After Reduction:", len(paths), "Len:", len(paths[0]))

        return paths

    def find_paths(self, seq):
        to_return = defaultdict(list)
        curr = tuple(self.start)

        for i, move in enumerate(seq):
            paths, curr = self.find(curr, move)
            for path in [x for x in paths if len(x) == len(min(paths, key = lambda k: len(k)))]:
                if i == 0:
                    to_return[i].append(path)
                    continue

                for prev in to_return[i - 1]:
                    to_return[i].append(prev + path)

        return to_return[i]

    def convert_path(self, dirs):
        path = ""

        for d in dirs:
            match d:
                case (-1, 0):
                    path += '^'
                case (1, 0):
                    path += 'v'
                case (0, -1):
                    path += '<'
                case (0, 1):
                    path += '>'
                case _:
                    assert False, d

        return path

    def build_path(self, dirs):
        path = self.convert_path(dirs)
        return "".join(path) + 'A'

    def find(self, start, dest):
        if (start, dest) in DP:
            return DP[(self.keypad[start], dest)]

        queue = deque([(start, [], set())])
        valid = []
        dest_loc = (0, 0)

        while queue:
            (r, c), path, seen = queue.popleft()

            if self.keypad[(r, c)] == dest:
                dest_loc = (r, c)
                p = self.build_path(path)
                if len(valid) == 0 or (len(valid) > 0 and len(p) <= len(valid[0])):
                    valid.append(p)
                else:
                    break
                continue

            if (r, c) in seen:
                continue

            seen.add((r, c))

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                rr = r + dr
                cc = c + dc

                if (rr, cc) not in self.keypad:
                    continue

                queue.append(((rr, cc), path + [(dr, dc)], set(seen)))

        DP[(self.keypad[start], dest)] = valid, dest_loc
        return valid, dest_loc

    def __repr__(self):
        if self.robot:
            return f"(ID: {self.id} | Keypad: DIR_KEYPAD | Inner: {self.robot})"
        return f"(ID: {self.id} | Keypad: NORMAL_KEYPAD)"

# 379A -- Nothing matters about order
# ^A^^<<A>>AvvvA -- As long as directions are grouped, it should be shortest
# <A>A<AAv<AA>>^AvAA^Av<AAA^>A -- All grouped symbols above must be closest distance to each other for shortest path

def parse_input(input):
    lines = input.splitlines()

    return lines

def part1(input: str) -> int:
    lines = parse_input(input)
    robot = Robot(2)

    total = 0

    for buttons in lines:
        s = robot.press_sequence([buttons])
        total += len(min(s, key=lambda k: len(k))) * int(buttons[:-1])

    return total

def part2(input: str) -> int:
    lines = parse_input(input)
    robot = Robot(26)

    total = 0

    for buttons in lines:
        s = robot.press_sequence([buttons])

        total += len(min(s, key=lambda k: len(k)))

    return total

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















