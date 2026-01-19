from heapq import heappush, heappop
from collections import deque
import sys
sys.setrecursionlimit(int(1e9))

grid = {}

with open(0) as input:
    lines = input.read().strip().splitlines()
    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if lines[r][c] != ' ':
                grid[(r, c)] = lines[r][c]

def get_amphipods(grid):
    amp = []

    for k, v in grid.items():
        if v in "ABCD":
            amp.append((v, k))

    to_remove = []

    for i in range(len(amp)):
        if in_best_place(amp, amp[i]):
            to_remove.append(amp[i])

    amp = [a for a in amp if a not in to_remove]

    amp = sorted(amp, key = lambda a: a[0])
    return amp

A = [(r, 3) for r in range(2, 4 if len(grid) <= 57 else 6)]
B = [(r, 5) for r in range(2, 4 if len(grid) <= 57 else 6)]
C = [(r, 7) for r in range(2, 4 if len(grid) <= 57 else 6)]
D = [(r, 9) for r in range(2, 4 if len(grid) <= 57 else 6)]
CORRIDOR = 1
rooms = A + B + C + D
intermediate = [(CORRIDOR, 1), (CORRIDOR, 2), (CORRIDOR, 4), (CORRIDOR, 6), (CORRIDOR, 8), (CORRIDOR, 10), (CORRIDOR, 11)]
scores = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}

def pretty_print(grid, state):
    r_low = min(r for r, _ in grid.keys())
    r_high = max(r for r, _ in grid.keys())
    c_low = min(c for _, c in grid.keys())
    c_high = max(c for _, c in grid.keys())

    for r in range(r_low, r_high + 1):
        row = ""
        for c in range(c_low, c_high + 1):
            if (r, c) in grid and grid[(r, c)] == '#':
                row += '#'
            elif (r, c) in grid and (r, c) not in [s[1] for s in state] and (r, c) not in rooms:
                row += ' '
            elif (r, c) not in grid and (r, c) not in state:
                row += ' '
            elif (r, c) in [s[1] for s in state]:
                selected = [s[0] for s in state if s[1] == (r, c)][0]
                row += selected

        print(row)
    print()

def final_state(state):
    if not all(x[1] in A for x in state if x[0] == 'A'):
        return False
    if not all(x[1] in B for x in state if x[0] == 'B'):
        return False
    if not all(x[1] in C for x in state if x[0] == 'C'):
        return False
    if not all(x[1] in D for x in state if x[0] == 'D'):
        return False
    
    return True

def heuristic(state):
    return sum(scores[t[0]] for t in state)

def in_best_place(state, amp):
    t, (r, c) = amp
    amps = [s for s in state if s[0] == t]

    if t == 'A':
        if (r, c) == A[len(A) - 1 - (len(A) - len(amps))]:
            return True
        return False
    elif t == 'B':
        if (r, c) == B[len(B) - 1 - (len(B) - len(amps))]:
            return True
        return False
    elif t == 'C':
        if (r, c) == C[len(C) - 1 - (len(C) - len(amps))]:
            return True
        return False
    elif t == 'D':
        if (r, c) == D[len(D) - 1 - (len(D) - len(amps))]:
            return True
        return False

    return False

def h(state):
    # admissible heuristic: for each amphipod, distance to the nearest available target room cell (ignoring other amphipods)
    total = 0
    occ = {pos: t for t, pos in state}
    for t, pos in state:
        targets = {'A': A, 'B': B, 'C': C, 'D': D}[t]
        if pos in targets:
            # check no wrong type below
            below_ok = True
            for deeper in targets[targets.index(pos)+1:]:
                if deeper in occ and occ[deeper] != t:
                    below_ok = False
                    break
            if below_ok:
                continue
        best = 10**12
        for dest in targets:
            d = paths.get((pos, dest)) or bfs(pos, dest)
            if d and d < best:
                best = d
        if best < 10**12:
            total += best * scores[t]
    return total

def dijkstras():
    start_state = tuple(sorted(get_amphipods(grid)))
    import math
    heap = []
    gscore = {start_state: 0}
    heappush(heap, (h(list(start_state)), start_state))
    iterations = 0

    while heap:
        f, state = heappop(heap)
        g = gscore.get(state, math.inf)
        iterations += 1
        if iterations % 10000 == 0:
            print(f"iters={iterations}, len(state)={len(state)}, g={g}, h={h(list(state))}")

        if final_state(list(state)):
            return g

        occ = {pos: t for t, pos in state}

        for i, (t, pos) in enumerate(state):
            targets = {'A': A, 'B': B, 'C': C, 'D': D}[t]
            if pos in targets:
                idx = targets.index(pos)
                wrong_below = any((p in occ and occ[p] != t) for p in targets[idx+1:])
                if not wrong_below:
                    continue

            if pos in rooms:
                for inter in intermediate:
                    if inter in occ:
                        continue
                    if clear_path(list(state), pos, inter):
                        dist = paths.get((pos, inter)) or bfs(pos, inter)
                        new_state = list(state)
                        new_state[i] = (t, inter)
                        new_state_t = tuple(sorted(new_state))
                        newg = g + dist * scores[t]
                        if newg < gscore.get(new_state_t, math.inf):
                            gscore[new_state_t] = newg
                            heappush(heap, (newg + h(list(new_state_t)), new_state_t))

            elif pos in intermediate:
                room_positions = targets
                if any((p in occ and occ[p] != t) for p in room_positions):
                    continue
                for dest in reversed(room_positions):
                    if dest in occ:
                        continue
                    if clear_path(list(state), pos, dest):
                        dist = paths.get((pos, dest)) or bfs(pos, dest)
                        new_state = list(state)
                        new_state[i] = (t, dest)
                        new_state_t = tuple(sorted(new_state))
                        newg = g + dist * scores[t]
                        if newg < gscore.get(new_state_t, math.inf):
                            gscore[new_state_t] = newg
                            heappush(heap, (newg + h(list(new_state_t)), new_state_t))
                        break

    return None

DP = {}
seen = set()

def find(state, depth):
    key = tuple(state)

    if key in seen:
        return int(1e10)

    seen.add(key)
    
    if depth > 20:
        return int(1e10)

    if len(state) == 0:
        return 0

    if key in DP:
        return DP[key]

    outcomes = []
    
    for amp, (r, c) in state:
        if (r, c) in intermediate:
            selected = []
            if amp == 'A': selected = A
            if amp == 'B': selected = B
            if amp == 'C': selected = C
            if amp == 'D': selected = D

            for dest in selected:
                if clear_path(state, (r, c), dest):
                    dist = bfs((r, c), dest)
                    new_state = list(state)
                    new_state.append((amp, dest))
                    new_state.remove((amp, (r, c)))
                    outcomes.append(dist * scores[amp] + find(new_state, depth + 1))
        else:
            for dest in intermediate:
                if clear_path(state, (r, c), dest):
                    dist = bfs((r, c), dest)
                    new_state = list(state)
                    new_state.append((amp, dest))
                    new_state.remove((amp, (r, c)))
                    outcomes.append(dist * scores[amp] + find(new_state, depth + 1))

    if len(outcomes) > 0:
        best = min(outcomes)
        DP[key] = best

        return best
    
    return int(1e10)

checks = {}

def clear_path(state, start, dest):
    check = []

    if (start, dest) in checks:
        check = checks[(start, dest)]
    else:
        low_c = min(start[1], dest[1])
        high_c = max(start[1], dest[1])
        check += [(r, start[1]) for r in range(CORRIDOR, start[0])]
        check += [(CORRIDOR, c) for c in range(low_c, high_c + 1)]
        check += [(r, dest[1]) for r in range(CORRIDOR, dest[0] + 1)]
        check = set(check)
        checks[(start, dest)] = check

    if any(s[1] in check and s[1] != start for s in state):
        return False

    return True

paths = {}

def bfs(start, dest):
    if (start, dest) in paths:
        return paths[(start, dest)]

    queue = deque([(start, 0)])
    seen = set()

    while queue:
        (r, c), d = queue.popleft()

        if (r, c) == dest:
            paths[(start, dest)] = d
            paths[(dest, start)] = d
            return d

        if (r, c) in seen:
            continue

        seen.add((r, c))

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rr = r + dr
            cc = c + dc

            if (rr, cc) in grid and grid[(rr, cc)] != '#':
                queue.append(((rr, cc), d + 1))

    return 0

p1 = dijkstras()
# state = get_amphipods(grid)
# p1 = find(state, 0)

print("Part 1:", p1)




