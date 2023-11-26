
def advance(player, move):
    player += move
    while player > 10:
        player -= 10
    return player

def play_game(player1, player2):
    p1_score = 0
    p2_score = 0
    end_state = lambda p1, p2: p1 >= 1000 or p2 >= 1000

    rolls = 0
    die_roll = 1
    player1_move = True

    while not end_state(p1_score, p2_score):
        move = 0
        for _ in range(3):
            move += die_roll
            die_roll += 1
            rolls += 1
            if die_roll > 100:
                die_roll = 1
        if player1_move:
            player1 = advance(player1, move)
            p1_score += player1
        else:
            player2 = advance(player2, move)
            p2_score += player2
        player1_move = not player1_move
    return (p1_score, p2_score, rolls)

def play_game2(p1, p2, s1, s2, memo):
    end_state = lambda s1, s2: s1 >= 21 or s2 >= 21
    total = (0, 0)

    if end_state(s1, s2):
        return (1, 0) if s1 > s2 else (0, 1)
    elif (p1, p2, s1, s2) in memo:
        return memo[(p1, p2, s1, s2)]
    else:
        for m1 in range(1, 4):
            for m2 in range(1, 4):
                for m3 in range(1, 4):
                    p1_ = int(p1)
                    s1_ = int(s1)
                    for m in [m1, m2, m3]:
                        p1_ = advance(p1_, m)
                    s1_ += p1_
                    w1, w2 = play_game2(p2, p1_, s2, s1_, memo)
                    memo[(p2, p1_, s2, s1_)] = (w1, w2)
                    total = (total[0] + w2, total[1] + w1)
    return total

def p1(output):
    print("Part 1:", output)

def p2(output):
    print("Part 2:", output)

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

player1 = int(lines[0][-1])
player2 = int(lines[1][-1])

p1_score, p2_score, rolls = play_game(player1, player2)

loser = min(p1_score, p2_score)

p1(loser * rolls)

memo = dict()

player1 = int(lines[0][-1])
player2 = int(lines[1][-1])

u1, u2 = play_game2(player1, player2, 0, 0, memo)

p2(max(u1, u2))
