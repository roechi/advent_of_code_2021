import functools


def solve(input_lines):
    player_one_pos = int(input_lines[0].rstrip().split(' ')[4])
    player_two_pos = int(input_lines[1].rstrip().split(' ')[4])

    player_one_score = 0
    player_two_score = 0

    turn = 0
    current_player = 0

    while player_one_score < 1000 and player_two_score < 1000:
        turn += 1
        steps = -3 + turn * 9

        if current_player == 0:
            player_one_pos += steps
            player_one_pos %= 10
            if player_one_pos == 0:
                player_one_pos = 10
            player_one_score += player_one_pos
            current_player = 1
        else:
            player_two_pos += steps
            player_two_pos %= 10
            if player_two_pos == 0:
                player_two_pos = 10
            player_two_score += player_two_pos
            current_player = 0

    if player_one_score >= 1000:
        return player_two_score * turn * 3
    else:
        return player_one_score * turn * 3


@functools.cache
def play_dirac(p1_pos, p2_pos, p1_scr, p2_score):
    if p2_score >= 21:
        return 0, 1

    wins1 = wins2 = 0
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                p1_pos_next = p1_pos + i + j + k
                p1_pos_next %= 10
                if p1_pos_next == 0:
                    p1_pos_next = 10
                w2, w1 = play_dirac(p2_pos, p1_pos_next, p2_score, p1_scr + p1_pos_next)
                wins1 += w1
                wins2 += w2

    return wins1, wins2


def solve2(input_lines):
    player_one_pos = int(input_lines[0].rstrip().split(' ')[4])
    player_two_pos = int(input_lines[1].rstrip().split(' ')[4])

    wins1, wins2 = play_dirac(player_one_pos, player_two_pos, 0, 0)

    return max([wins1, wins2])


with open('input.txt', 'r') as input_file:
    input_lines = input_file.readlines()

    print('Solution part 1:')
    print(solve(input_lines))
    print('Solution part 2:')
    print(solve2(input_lines))
