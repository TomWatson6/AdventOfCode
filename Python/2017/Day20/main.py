import re

with open(0) as f:
    lines = [x.strip() for x in f.readlines()]

class Particle:
    def __init__(self, line):
        px, py, pz, vx, vy, vz, ax, ay, az = list(map(int, re.findall(r"-?\d+", line)))
        self.px = px
        self.py = py
        self.pz = pz
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.ax = ax
        self.ay = ay
        self.az = az

    def collides(self, p):
        # s = ut + 1/2at**2
        pass


particles = []

t = 100000

for i, line in enumerate(lines):
    px, py, pz, vx, vy, vz, ax, ay, az = list(map(int, re.findall(r"-?\d+", line)))

    px += vx * t + 0.5 * ax * t**2
    py += vy * t + 0.5 * ay * t**2
    pz += vz * t + 0.5 * az * t**2

    particles.append((i, px, py, pz))

closest = min(particles, key = lambda p: abs(p[1]) + abs(p[2]) + abs(p[3]))

print("Part 1:", closest[0])


















