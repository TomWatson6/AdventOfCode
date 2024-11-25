import hashlib
from collections import deque

with open(0) as f:
    code = f.read().strip()

DIRS = {
    (-1, 0): "U",
    (1, 0): "D",
    (0, -1): "L",
    (0, 1): "R",
}

# result = hashlib.md5(input.encode()).hexdigest()

class Grid:
    def __init__(self, code: str, lines: list[str]):
        self.code = code
        self.grid = {}
        for i, line in enumerate(lines):
            for j, ch in enumerate(line):
                if ch == 'S':
                    self.start = (i, j)

                if ch == 'V':
                    self.vault = (i, j)

                self.grid[(i, j)] = ch

    def doors(self, code) -> list[tuple[tuple[int, int], bool]]:
        # Up, Down, Left, Right
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        hash = hashlib.md5(code.encode()).hexdigest()[:4]

        return list(zip(dirs, [x in ['b', 'c', 'd', 'e', 'f'] for x in hash]))

    def vault_path(self) -> int:
        queue = deque([(self.start, "")])
        
        while queue:
            pos, path = queue.popleft()
            r, c = pos

            if self.grid[pos] == 'V':
                return path

            dirs = self.doors(self.code + path)
            dirs = [x[0] for x in dirs if x[1] and (pos[0] + x[0][0], pos[1] + x[0][1]) in self.grid]

            for dr, dc in dirs:
                rr = r + dr
                cc = c + dc
                queue.append(((rr, cc), path + DIRS[tuple((dr, dc))]))

        return ""

    def longest_vault_path(self) -> int:
        queue = deque([(self.start, "")])
        longest = 0
        
        while queue:
            pos, path = queue.popleft()
            r, c = pos

            if self.grid[pos] == 'V':
                longest = max(longest, len(path))
                continue

            dirs = self.doors(self.code + path)
            dirs = [x[0] for x in dirs if x[1] and (pos[0] + x[0][0], pos[1] + x[0][1]) in self.grid]

            for dr, dc in dirs:
                rr = r + dr
                cc = c + dc
                queue.append(((rr, cc), path + DIRS[tuple((dr, dc))]))

        return longest

    def __repr__(self):
        output = f"Code: {self.code}, Start: {self.start}, Vault: {self.vault}\n"

        for r in range(max(r for r, c in self.grid.keys()) + 1):
            for c in range(max(c for r, c in self.grid.keys()) + 1):
                output += self.grid[(r, c)]

            output += "\n"

        return output

    
lines = ["S   ", "    ", "    ", "   V"]
grid = Grid(code, lines)
print("Part 1:", grid.vault_path())
print("Part 2:", grid.longest_vault_path())
























