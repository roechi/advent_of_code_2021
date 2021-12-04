def check_board(hits):

    for i in range(5):
        count_x = 0
        count_y = 0
        for h in hits:
            if h[0] == i:
                count_x += 1
            if h[1] == i:
                count_y += 1
        if count_x == 5:
            return True
        if count_y == 5:
            return True
    return False


def get_score(board, hits, number):
    sum = 0
    for x in range(5):
        for y in range(5):
            if (x, y) not in hits:
                sum += board[x][y]

    return sum * number


def solve(numbers, boards):
    hits = [[] for i in range(len(boards))]

    for number in numbers:
        for i in range(len(boards)):
            curr_board = boards[i]
            for x in range(5):
                for y in range(5):
                    if number == curr_board[x][y]:
                        hits[i].append((x, y))
                        if check_board(hits[i]):
                            return get_score(curr_board, hits[i], number)




def solve2(numbers, boards):
    hits = [[] for _ in range(len(boards))]
    winning_board = None
    winning_number = None
    winning_boards = []
    for number in numbers:
        for i in range(len(boards)):
            curr_board = boards[i]
            for x in range(5):
                for y in range(5):
                    if number == curr_board[x][y] and i not in winning_boards:
                        hits[i].append((x, y))
                        if check_board(hits[i]):
                            winning_board = i
                            winning_number = number
                            winning_boards.append(i)

    return get_score(boards[winning_board], hits[winning_board], winning_number)


with open('input.txt', 'r') as input_file:
    numbers_str = input_file.readline().rstrip().split(',')
    numbers = list(map(int, numbers_str))

    input_file.readline()

    boards = []
    next_board = []
    lines = input_file.readlines()

    for line in lines:
        if line != '\n':
            stripped = line.rstrip().lstrip().split(' ')
            while '' in stripped:
                stripped.remove('')
            next_board.append([int(x.strip()) for x in stripped])
        else:
            boards.append(next_board)
            next_board = []

    boards.append(next_board)

    print('Solution part 1:')
    print(solve(numbers, boards))
    print('Solution part 2:')
    print(solve2(numbers, boards))