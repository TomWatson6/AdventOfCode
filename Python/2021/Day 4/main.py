from board import Board

def p1(output):
    print("Part 1:", output)

def p2(output):
    print("Part 2:", output)

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

numbers = [int(x) for x in lines[0].split(",")]
lines = lines[2:]

board_input = []
input = []

for line in lines:
    if len(line) == 0:
        board_input.append(input)
        input = []
    else:
        input.append([x for x in line.split(" ") if x != ""])
board_input.append(input)

boards = [Board(x) for x in board_input]

winning_boards = []

for x in range(len(numbers)):
    for board in boards:
        board.mark(numbers[x])
        if board.is_winner():
            winning_boards.append((board, numbers[x]))
    boards = [x for x in boards if x not in [y[0] for y in winning_boards]]

first_winner = winning_boards[0][0]
first_winning_number = winning_boards[0][1]
first_remainder = sum(first_winner.get_remaining())

last_winner = winning_boards[-1][0]
last_winning_number = winning_boards[-1][1]
last_remainder = sum(last_winner.get_remaining())

p1(first_winning_number * first_remainder)
p2(last_winning_number * last_remainder)