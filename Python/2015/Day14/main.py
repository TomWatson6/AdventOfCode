

class Reindeer:
    def __init__(self, s):
        parts = s.split(" ")
        self.name = parts[0]
        self.speed = int(parts[3])
        self.move_time = int(parts[6])
        self.rest_time = int(parts[13])

    def __str__(self):
        return "{} moves at {} for {} then rests for {}".format(self.name, self.speed, self.move_time, self.rest_time)

with open("simple_input.txt") as f:
    deers = [Reindeer(x) for x in f.readlines() if x != ""]

duration = 1000
distances = []
progress = {d.name: [] for d in deers}
move_map = {d.name: [] for d in deers}

for d in deers:
    dist = 0
    t = 0

    while t <= duration:
        for m in range(d.move_time):
            dist += d.speed
            t += 1
            progress[d.name].append(dist)
            if t > duration:
                break
            move_map[d.name].append(1)
            assert len(move_map[d.name]) == t

        if t > duration:
            break

        for r in range(d.rest_time):
            t += 1
            progress[d.name].append(dist)
            if t > duration:
                break
            move_map[d.name].append(0)
            assert len(move_map[d.name]) == t

    distances.append(dist)

print("Part 1: {}".format(max(distances)))

distances = {d.name: 0 for d in deers}
points = {d.name: 0 for d in deers}
t = 0

while t < duration:
    for d in deers:
        distances[d.name] += d.speed * move_map[d.name][t]

    m = max(distances.items(), key=lambda v: v[1])

    for k, v in distances.items():
        if v == m[1]:
            points[m[0]] += 1

    t += 1

segments = []
cum_segs = []

for k, v in move_map.items():
    cum_seg = []
    segment = []
    curr = 1

    for i in range(1, len(v)):
        if v[i] == v[i-1]:
            curr += 1
        else:
            segment.append(curr)
            if len(cum_seg) > 0:
                cum_seg.append(curr + cum_seg[-1])
            else:
                cum_seg.append(curr)
            curr = 1
    cum_seg.append(curr + cum_seg[-1])
    segment.append(curr)

    cum_segs.append(cum_seg)
    segments.append(segment)

points = {d.name: 0 for d in deers}

for i in range(1, duration + 1):
    m = max(progress.items(), key=lambda v: v[1][i])
    points[m[0]] += 1

print(cum_segs)
print(segments)
print([sum(s) for s in segments])
print(points)
print([len(m) for m in move_map.values()])
[print("{}: {}".format(x[0], len(x[1]))) for x in progress.items()]

print("Part 2: {}".format(max(points.items(), key=lambda v: v[1])))









