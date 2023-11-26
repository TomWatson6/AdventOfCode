
class Coord:
    def __init__(self, r, c):
        self.R = r
        self.C = c

    def __str__(self):
        return "({}, {})".format(self.R, self.C)

    def __hash__(self):
        return hash((self.R, self.C))

    def __eq__(self, other):
        return (self.R, self.C) == (other.R, other.C)

class Tile:
    def __init__(self, pos, type):
        self.Pos = pos
        self.Type = type
        self.Final = False

    def __str__(self):
        return "{} -> {} {}".format(self.Pos, self.Type, "Correct Placement" if self.Final else "Incorrect Placement")

tiles = []

Corridor = 1

A = "A"
B = "B"
C = "C"
D = "D"
Amphipods = [A, B, C, D]
Wall = "#"
Available = "."
Empty = " "
high_R = 0

Cost = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000
}

Destination = {
    "A": 3,
    "B": 5,
    "C": 7,
    "D": 9
}

def column_depth():
    return high_R - Corridor

def is_blocked(path):
    blocking_bugs = []
    blocked = False

    for c in path:
        if tiles[c].Type in Amphipods:
            blocked = True
            blocking_bugs.append(tiles[c])
    return blocked, blocking_bugs

def simple_heuristic(t):
    c = Cost[t.Type]
    up = t.Pos.R - Corridor
    across = abs(t.Pos.C - Destination[t.Type])

    if across == 0:
        return 0

    return c * (up + across)

def heuristic(path):
    bug = tiles[path[0]]
    cost = Cost[bug.Type]
    return (len(path) - 1) * cost

def find_path(bug):
    simple_path = []
    
    # First go up until hitting corridor
    if bug.Pos.C != Destination[bug.Type]:
        for r in range(bug.Pos.R - 1, Corridor - 1, -1):
            simple_path.append(Coord(r, bug.Pos.C))

    # Then find movement needed to get to destination column
    start = 0
    if len(simple_path) > 0:
        start = simple_path[-1].C
    else:
        start = bug.Pos.C

    finish = Destination[bug.Type]

    inc = -1

    if start < finish:
        inc = 1

    # This should be skipped if already in correct position
    for c in range(bug.Pos.C + inc, Destination[bug.Type] + inc, inc):
        simple_path.append(Coord(simple_path[-1].R, c))

    # Then go down until you either hit same type amphipod or a wall
    if len(simple_path) > 0:
        curr = Coord(simple_path[-1].R, simple_path[-1].C)
    else:
        curr = Coord(bug.Pos.R, bug.Pos.C)

    num_correct = 0

    # [print(x) for x in simple_path]

    while curr.R != high_R:
        curr.R += 1
        if tiles[curr].Type == bug.Type:
            num_correct += 1

    if len(simple_path) > 0:
        curr = Coord(simple_path[-1].R, simple_path[-1].C)
    else:
        curr = Coord(bug.Pos.R, bug.Pos.C)

    for r in range(curr.R, high_R - num_correct, 1):
        curr.R += 1
        simple_path.append(Coord(curr.R, curr.C))

    simple_path.insert(0, Coord(bug.Pos.R, bug.Pos.C))

    return simple_path
    

def contents(col):
    return sorted([t for t in tiles if t.Pos.C == col], key = lambda t: t.Pos.R)

def num_incorrect():
    num = 0
    
    for t in tiles:
        if t.Type not in Amphipods:
            continue
        if t.Pos.C != Destination[t.Type]:
            num += 1

    return num

def print_heuristics():
    for t in tiles.values():
        print("({}, {}) -> {}".format(t.Pos.R, t.Pos.C, simple_heuristic(t)))

def print_tiles(func):
    for t in [x for x in tiles.values() if x.Type in Amphipods]:
        ret = func(t)
        out = func(t)
        if hasattr(ret, "__len__"):
            out = ", ".join([str(x) for x in ret])
        print("({}, {}) -> {}".format(t.Pos.R, t.Pos.C, out))

with open("simple_input.txt") as f:
    input = [x for x in f.readlines() if x != ""]
    input = [[y for y in x if y != "\n"] for x in input]

for r, row in enumerate(input):
    for c, col in enumerate(row):
        tiles.append(Tile(Coord(r, c), col))

tiles = {t.Pos: t for t in tiles}

high_R = max([t.Pos.R for t in tiles.values() if t.Type in Amphipods])

for n in Destination.values():
    l = [t for t in tiles.values() if t.Pos.C == n and t.Type in Amphipods]
    l = sorted(l, key=lambda t: t.Pos.R, reverse=True)
    for i, t in enumerate(l):
        if t.Pos.R == high_R - i and t.Pos.C == Destination[t.Type]:
            t.Final = True
        else:
            break

for t in tiles.values():
    if t.Type in Amphipods:
        print(t)

print_tiles(lambda t: find_path(t))
print_tiles(lambda t: heuristic(find_path(t)))
print_tiles(lambda t: is_blocked(find_path(t)))

# print_tiles(lambda t: t.Final)
# print_tiles(lambda t: simple_heuristic(t))

# Need to prioritise high costing paths and not increase their cost by having them move out of the way of other bugs
# Go through required moves from highest amount to lowest amount - figure out how to get tile to optimal location using recursive method?
# Recursive method: examine destination column - figure out how to shift stuff in it to make way for caller
'''
Plan of Action:
    For each amphipod, find destination target, lowest possible within it's destination corridor above other amphipods
    Move all other amphipods above existing in final destination if that is the case out of destination hall to make room for amphipod moving to that destination
    Loop through corridor amphipods to see if they can move in a clear path to where they need to be for their destination
    If this is the case, it could clear a path for the initial amphipod to move to it's destination
    If after moving all other amphipods, the destination is still not clear, then failure, and move to next possibility

    Move back and forth between the states: corridor, and hallways amphipods to see if they can move to their destination
    Loop through all as a starting pod, to see if that works
    BFS looks like the best way to search through possibilities for this

Rules: 
    Amphipod can only move to a spot in the corridor from the hallway that isn't ontop of another hallway (blocking the hallway)
    Amphipod once in the corridor can only move back into a hallway (it's destination square)

Mock of main function:
    func(leftovers (bugs that aren't in destination), current considered):
        if in corridor:
            if can_move_to_dest(current):
                move_to_dest
            else:
                blockers = get_blocking_in_order(current, dest)
                for blocking in blockers:



Things to consider:
    -> Can I move to destination
    -> How much will the path to the destination cost?
    -> When I move is the bug from the column I've moved from the correct bug for the column it's in
    -> When I get to destination, will I be the highest correct bug for that column

Consider using a map of Coord -> Amphipod, this would be easier for using A* path planning
If using a map - then reconsider including walls/empty/available tiles for blocks / available locations to move
    - This will most likely require refactor of some methods so far (might just be the printing ones)

Now that we have is_blocked, we should try to find a way to iterate through all possible paths - this could start with trying to move all incomplete placements to their correct columns (and correct placement somehow)
'''