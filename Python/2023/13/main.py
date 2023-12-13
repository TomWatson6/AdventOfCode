from collections import defaultdict

def get_reflection_horiz(grid):
    scores = {}

    for r in range(len(grid)):
        score = 0
        for i in range(min(r + 1, len(grid) - r - 1)):
            slice1 = [grid[r - i][c] for c in range(len(grid[0]))]
            slice2 = [grid[r + i + 1][c] for c in range(len(grid[0]))]
            if slice1 == slice2:
                score += 1
            else:
                break
        else:
            if score != 0:
                scores[r] = score

    row_reflection = not all(v == 0 for k, v in scores.items())

    return row_reflection, set([k + 1 for k in scores.keys()])

def get_reflection_vert(grid):
    scores = {}

    for c in range(len(grid[0])):
        score = 0
        for i in range(min(c + 1, len(grid[0]) - c - 1)):
            slice1 = [grid[r][c - i] for r in range(len(grid))]
            slice2 = [grid[r][c + i + 1] for r in range(len(grid))]
            if slice1 == slice2:
                score += 1
            else:
                break
        else:
            if score != 0:
                scores[c] = score

    col_reflection = not all(v == 0 for k, v in scores.items())

    return col_reflection, set([k + 1 for k in scores.keys()])

def print_grid(grid):
    for r in range(len(grid)):
        out = ""
        for c in range(len(grid[0])):
            out += grid[r][c]
        print(out)


with open(0) as f:
    grids = [[list(t) for t in x.strip().split("\n")] for x in f.read().split("\n\n")]

row = 0
col = 0

row2 = 0
col2 = 0

for grid in grids:
    horiz, row_scores = get_reflection_horiz(grid)
    vert, col_scores = get_reflection_vert(grid)

    if horiz and len(row_scores) == 1:
        row += list(row_scores)[0]
    else:
        col += list(col_scores)[0]

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] = '#' if grid[r][c] == '.' else '.'

            horiz2, new_row_scores = get_reflection_horiz(grid)
            vert2, new_col_scores = get_reflection_vert(grid)

            if horiz2 and len([x for x in new_row_scores if x not in row_scores]) > 0:
                row2 += [x for x in new_row_scores if x not in row_scores][0]
                break

            if vert2 and len([x for x in new_col_scores if x not in col_scores]) > 0:
                col2 += [x for x in new_col_scores if x not in col_scores][0]
                break

            grid[r][c] = '#' if grid[r][c] == '.' else '.'

        else:
            continue

        break

print("Part 1:", row * 100 + col)
print("Part 2:", row2 * 100 + col2)




















