
from collections import defaultdict

## Find every rotation/flip of the cube (all permutations of [FRONT, BACK, LEFT, RIGHT, UP, DOWN])
## For all beacons, try find 12 that match another scanner's beacons
## Define matching => Assume first matches by reversing relation of positions, find position difference
##  between first and second scanner, offset scanner positions by negative that relative position
##  If that relative position equals each scanner's negative relative position for the beacon, then match
## Build a tree from scanner 0 to all other scanner mapping relative positions from one another
## Have a way of simplifying the tree to have all scanner relative to scanner 0
##
## COMPLEXITY ESTIMATE:
## 38 Cubes -> 24 Rotations per cube -> 26 beacons per cube ~ 23K checks (REALLY LOW)
## Actually ~ 140 million checks at most, not the worst

class Scanner:
    def __init__(self, scanner_id, beacons):
        self.scanner_id = scanner_id
        self.beacons = beacons
        self.rotations = self.get_rotations(beacons)

    def rotate(self, beacons, axis):
        rotation = []
        
        for beacon in beacons:
            x, y, z = beacon
            if axis == 'x':
                x0 = int(x)
                z0 = int(-y)
                y0 = int(z)
            elif axis == 'y':
                y0 = int(y)
                z0 = int(-x)
                x0 = int(z)
            else:
                z0 = int(z)
                y0 = int(-x)
                x0 = int(y)
            rotation.append((x0, y0, z0))
        return rotation

    def get_faces(self, beacons):
        faces = []
        rotations = [[], ['x'], ['x', 'x'], ['x', 'x', 'x'], ['y'], ['y', 'y', 'y']]
        for rotation in rotations:
            face = [x for x in beacons]
            for axis in rotation:
                face = self.rotate(face, axis)
            faces.append((rotation, face))
        return faces

    def get_rotations(self, beacons):
        faces = self.get_faces(beacons)
        rotations = []
        for face in faces:
            f = [x for x in face[1]]
            rotations.append(face)
            for i in range(3):
                f = self.rotate(f, 'z')
                f1 = [x for x in face[0]]
                [f1.append('z') for _ in range(i + 1)]
                rotations.append((f1, f))
        return rotations

## ScannerTree => Tree of each scanner mapping to other, so 0 is root, others will branch off
## Method assign_child will attempt to match a ScannerTree as a child, if not it will return -1 (rejection)
##  assign_child will only check the children at the ends of the branches, as all others are already fully
##  checked
## Contains method for finding relative position of other scanner to root scanner and adding all beacons up
##  to a dictionary to filter out any dupes, all will be relative to root (0) node and hence will find correct
##  number of beacons... I HOPE

class ScannerTree:
    def __init__(self, root):
        self.root = root
        self.position = (0, 0, 0)
        self.children = []
        self.scanners_tried = dict()
 
    def print(self, level):
        s = "".join(["\t" for _ in range(level)])
        s += str(self.position)
        print(s)
        for child in self.children:
            child.print(level + 1)

    def get_absolute_positions(self, p):
        pos = (self.position[0] + p[0], self.position[1] + p[1], self.position[2] + p[2])
        output = [pos]

        for child in self.children:
            child_output = child.get_absolute_positions(pos)
            for c in child_output:
                output.append(c)
        return output

    def count_beacons(self):
        output = set()

        for beacon in self.root.beacons:
            output.add(beacon)

        for child in self.children:
            o = child.count_beacons()
            for o1 in o:
                output.add((o1[0] + child.position[0], o1[1] + child.position[1], o1[2] + child.position[2]))

        return output

    def try_add(self, scanner):
        success = self.assign_child(scanner)

        if not success and len(self.children) > 0:
            for i in range(len(self.children)):
                success = self.children[i].try_add(scanner)
                if success:
                    break

        return success

    def add_child(self, to_add, r2, relative_position):
        to_add.root.beacons = r2[1]
        to_add.root.rotations = to_add.root.get_rotations(r2[1])
        to_add.position = relative_position
        self.children.append(to_add)

    def assign_child(self, scanner):
        if self.scanners_tried.get(scanner.root.scanner_id) is not None:
            return False
        for r in scanner.root.rotations:
            position = self.get_matches(self.root.beacons, r)
            if position is not None:
                self.add_child(scanner, r, position)
                return True

        self.scanners_tried[scanner.root.scanner_id] = True
        scanner.scanners_tried[self.root.scanner_id] = True
        return False

    def get_matches(self, beacons, r):
        a1 = [x for x in beacons]
        a2 = [x for x in r[1]]
        get_pos = lambda b1, b2: (b1[0] - b2[0], b1[1] - b2[1], b1[2] - b2[2])

        rel_pos = defaultdict(int)

        for b1 in a1:
            for b2 in a2:
                rel_pos[get_pos(b1, b2)] += 1

        for k, v in rel_pos.items():
            if v >= 12:
                return k

def p1(output):
    print("Part 1:", output)

def p2(output):
    print("Part 2:", output)

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

scanners_dict = defaultdict(list)

scanner = []
counter = 0
current = -1
while counter < len(lines):
    if lines[counter].startswith("--- "):
        line = lines[counter].strip("--- ").strip(" ---").split(" ")
        current = int(line[1])
    elif lines[counter].find(',') > 0:
        scanner.append(tuple([int(x) for x in lines[counter].split(",")]))
    else:
        scanners_dict[current] = scanner
        scanner = []
    counter += 1
scanners_dict[current] = scanner

scanners = []
for k, v in scanners_dict.items():
    scanners.append(ScannerTree(Scanner(k, v)))

root_scanner = scanners[0]
del scanners[0]
loop_counter = 1

while len(scanners) > 0:
    to_remove = -1
    for i in range(len(scanners)):
        if root_scanner.try_add(scanners[i]):
            to_remove = i
            break

    if to_remove != -1:
        del scanners[to_remove]
        print("Remaining:", len(scanners))
    else:
        break
    loop_counter += 1

p1(len(root_scanner.count_beacons()))

positions = root_scanner.get_absolute_positions((0, 0, 0))

largest = 0

for i in range(len(positions) - 1):
    for j in range(1, len(positions), 1):
        x1, y1, z1 = positions[i]
        x2, y2, z2 = positions[j]
        man = abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)
        largest = max(man, largest)

p2(largest)
