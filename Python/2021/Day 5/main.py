

def p1(output):
    print("Part 1:", output)

def p2(output):
    print("Part 2:", output)

with open("input.txt") as f:
    lines = [x for x in f.readlines()]

line_map = dict()

overlap = 0

for line in lines:
    start, end = line.split(" -> ")
    start = [int(x) for x in start.split(",")]
    end = [int(x) for x in end.split(",")]

    # If horizontal line
    if start[1] == end[1]:
        inc = 1 if end[0] >= start[0] else -1
        for i in range(start[0], end[0] + inc, inc):
            if line_map.get((i, start[1])) is None:
                line_map[(i, start[1])] = 1
            elif line_map.get((i, start[1])) == 1:
                line_map[(i, start[1])] += 1
                overlap += 1
    # If vertical line
    elif start[0] == end[0]:
        inc = 1 if end[1] >= start[1] else -1
        for i in range(start[1], end[1] + inc, inc):
            if line_map.get((start[0], i)) is None:
                line_map[(start[0], i)] = 1
            elif line_map.get((start[0], i)) == 1:
                line_map[(start[0], i)] += 1
                overlap += 1

p1(overlap)

overlap = 0
line_map = dict()

for line in lines:
    start, end = line.split(" -> ")
    start = [int(x) for x in start.split(",")]
    end = [int(x) for x in end.split(",")]

    # If horizontal line
    if start[1] == end[1]:
        inc = 1 if end[0] >= start[0] else -1
        for i in range(start[0], end[0] + inc, inc):
            if line_map.get((i, start[1])) is None:
                line_map[(i, start[1])] = 1
            elif line_map.get((i, start[1])) == 1:
                line_map[(i, start[1])] += 1
                overlap += 1
    # If vertical line
    elif start[0] == end[0]:
        inc = 1 if end[1] >= start[1] else -1
        for i in range(start[1], end[1] + inc, inc):
            if line_map.get((start[0], i)) is None:
                line_map[(start[0], i)] = 1
            elif line_map.get((start[0], i)) == 1:
                line_map[(start[0], i)] += 1
                overlap += 1
    # If diagonal line
    else:
        x_inc = 1 if end[0] >= start[0] else -1
        y_inc = 1 if end[1] >= start[1] else -1
        pos = tuple(start)
        while pos != (end[0] + x_inc, end[1] + y_inc):
            if line_map.get(pos) is None:
                line_map[pos] = 1
            elif line_map.get(pos) == 1:
                line_map[pos] += 1
                overlap += 1
            pos = (pos[0] + x_inc, pos[1] + y_inc)

p2(overlap)