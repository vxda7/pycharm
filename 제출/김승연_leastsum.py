def find(i, j, hap):
    global board
    global N
    global minV
    if hap > minV:
        return
    if i == N - 1 and j == N - 1:
        if minV > hap:
            minV = hap
    else:
        if 0 <= i+1 < N:
            find(i + 1, j, hap + board[i+1][j])
        if 0 <= j+1 < N:
            find(i, j + 1, hap + board[i][j+1])


t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    board = [list(map(int, input().split())) for i in range(N)]
    temp = []
    minV = 1000000000000000
    find(0, 0, board[0][0])
    print("#{} {}".format(tc, minV))
