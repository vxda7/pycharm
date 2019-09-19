def check(col, row, N):
    global board
    for i in range(N):
        if 0 <= col - i < N:
            if board[i][row] == 1:
                return False
            if 0 <= row + i < N:
                if board[col - i][row + i] == 1:
                    return False
            if 0 <= row - i < N:
                if board[col - i][row - i] == 1:
                    return False
    return True


def find(i, N):
    global cnt, board, info
    if i == N:  # 모든 줄에 퀸을 놓은 경우
        cnt += 1
    else:
        for j in range(N):
            # 다른 줄에 j번 열에 퀸이 없어야 하고
            # 왼쪽 대각선과 오른쪽 대각선에 퀸이 없어야 한다.
            if check(i, j, N):
                board[i][j] = 1
                find(i + 1, N)


t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    cnt = 0
    board = [[0] * N for i in range(N)]
    find(0, N)
    print("#{} {}".format(tc, cnt))
