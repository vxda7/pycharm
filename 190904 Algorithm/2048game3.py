def nozero(N):
    global board
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                board[i].remove(0)
                board[i].append(0)


def change(N):
    for i in range(N):
        for j in range(N):
            if j < N // 2:
                board[i][j], board[i][N - 1 - j] = board[i][N - 1 - j], board[i][j]


t = int(input())
for tc in range(1, t + 1):
    N, S = input().split()
    N = int(N)
    board = [list(map(int, input().split())) for i in range(N)]

    if S == 'up' or S == 'down':
        board = list(map(list, zip(*board)))
    if S == 'right' or S == 'down':
        change(N)
    nozero(N)
    for i in range(N):
        for j in range(N - 1):
            if board[i][j] == board[i][j + 1]:
                board[i][j] *= 2
                board[i][j + 1] = 0
                board[i].remove(0)
                board[i].append(0)
    if S == 'right' or S == 'down':
        change(N)
    if S == 'up' or S == 'down':
        board = list(map(list, zip(*board)))

    print("#{}".format(tc))
    for line in board:
        print(*line)
