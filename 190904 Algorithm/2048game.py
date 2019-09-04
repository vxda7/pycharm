def change(i, j, S, ok):
    global board
    global setting
    global N
    di, dj = setting[S]  # 증가값
    ni, nj = i + di, j + dj  # 변화값
    before = board[i][j]
    after = board[ni][nj]

    if S == 'up':
        print(board)
        if i == 0 and after == 0:
            if i < N - 2:
                change(i + 1, j, S, False)
        if before == after and ok and before != 0:
            board[i][j] = before + after
            board[ni][nj] = 0
            if i < N - 2:
                change(i + 1, j, S, ok)
        elif before == 0:
            board[i][j] = after
            board[ni][nj] = 0
            if i < N - 2:
                change(i + 1, j, S, False)
                change(i, j, S, ok)
        else:
            if i < N - 2:
                change(i + 1, j, S, ok)


def doit(N, S):
    global board
    board = list(map(list, zip(*board)))
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                del board[i][j]
                board[i].append(0)
    board = list(map(list, zip(*board)))


t = int(input())
for tc in range(1, t + 1):
    N, S = input().split()
    N = int(N)
    board = [list(map(int, input().split())) for i in range(N)]
    setting = {'up': [1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}
    for j in range(N):
        doit(N, S)
        change(0, j, S, True)

    print("#{}".format(tc))
    for line in board:
        print(*line)
