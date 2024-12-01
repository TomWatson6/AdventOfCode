
with open(0) as f:
    input = f.read().strip()

class Tiles:
    def __init__(self, row):
        self.tiles = [row]

    def add_row(self):
        new_row = []

        for i in range(len(self.tiles[-1])):
            def safe(n):
                return not 0 <= n < len(self.tiles[-1]) or self.tiles[-1][n] == '.'

            left, middle, right = i - 1, i, i + 1

            match (safe(left), safe(middle), safe(right)):
                case False, False, True:
                    new_row.append('^')
                case True, False, False:
                    new_row.append('^')
                case False, True, True:
                    new_row.append('^')
                case True, True, False:
                    new_row.append('^')
                case _:
                    new_row.append('.')

        self.tiles.append("".join(new_row))

    def __repr__(self) -> str:
        output = '\n'.join(self.tiles)
        return f"{output}"

tiles = Tiles(input)

for _ in range(39):
    tiles.add_row()

total = sum(len([x for x in row if x == '.']) for row in tiles.tiles)

print("Part 1:", total)

for _ in range(399960):
    tiles.add_row()

total = sum(len([x for x in row if x == '.']) for row in tiles.tiles)

print("Part 2:", total)




















