import matplotlib.pyplot as plt
from collections import deque
from typing import Dict, Tuple, List, Optional

class Grid:
    def __init__(self, squares: Dict[Tuple[int, int], str], start: Tuple[int, int], dest: Tuple[int, int]):
        self.squares = squares
        self.start = start
        self.dest = dest

    @classmethod
    def from_string(cls, value: str) -> 'Grid':
        squares = {}
        start = (0, 0)
        dest = (0, 0)

        for i, line in enumerate(value.splitlines()):
            for j, c in enumerate(line):
                if c == 'S':
                    start = (i, j)
                elif c == 'E':
                    dest = (i, j)
                squares[(i, j)] = c

        return cls(squares, start, dest)

    def get_valid_adjacents(self, loc: Tuple[int, int]) -> List[Tuple[int, int]]:
        adjacents = []
        curr = 'a' if self.squares[loc] == 'S' else self.squares[loc]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dr, dc in directions:
            rr, cc = loc[0] + dr, loc[1] + dc

            if (rr, cc) in self.squares:
                neighbor_char = self.squares[(rr, cc)]
                neighbor = 'z' if neighbor_char == 'E' else neighbor_char

                if ord(neighbor) <= ord(curr) + 1:
                    adjacents.append((rr, cc))

        return adjacents

    def find_path(self, start: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
        queue = deque([(start, 0)])
        seen = {start}
        came_from = {}

        while queue:
            curr, depth = queue.popleft()

            if self.squares[curr] == 'E':
                path = [curr]
                while curr in came_from:
                    curr = came_from[curr]
                    path.append(curr)
                path.reverse()
                return path

            for adj in self.get_valid_adjacents(curr):
                if adj not in seen:
                    seen.add(adj)
                    queue.append((adj, depth + 1))
                    came_from[adj] = curr

        return None

    def visualize_path(self, path: List[Tuple[int, int]]):
        rows = max(r for r, _ in self.squares.keys()) + 1
        cols = max(c for _, c in self.squares.keys()) + 1

        grid = [[' ' for _ in range(cols)] for _ in range(rows)]
        for (r, c), value in self.squares.items():
            grid[r][c] = value

        for r, c in path:
            if grid[r][c] not in ('S', 'E'):
                grid[r][c] = 'X'

        for line in grid:
            print(''.join(line))

        fig, ax = plt.subplots()
        ax.set_xlim(-0.5, cols - 0.5)
        ax.set_ylim(-0.5, rows - 0.5)
        ax.set_xticks(range(cols))
        ax.set_yticks(range(rows))
        ax.grid(True)

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 'S':
                    ax.text(c, rows - 1 - r, 'S', va='center', ha='center', fontsize=12, color='green')
                elif val == 'E':
                    ax.text(c, rows - 1 - r, 'E', va='center', ha='center', fontsize=12, color='red')
                elif val == 'X':
                    ax.text(c, rows - 1 - r, 'X', va='center', ha='center', fontsize=12, color='blue')
                else:
                    ax.text(c, rows - 1 - r, val, va='center', ha='center', fontsize=10, color='black')

        plt.gca().invert_yaxis()
        plt.show()

if __name__ == "__main__":
    # input_data = """
# Sabc
# abcd
# abcd
# abcdE
# """
    input_data = open("input.txt").read().strip()
    grid = Grid.from_string(input_data)
    path = grid.find_path(grid.start)

    if path:
        grid.visualize_path(path)
    else:
        print("No path found")

