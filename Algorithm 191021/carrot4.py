t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    board = [list(map(int, input().split())) for i in range(N)]
    get1, get2, get3, get4 = 0, 0, 0, 0
    start, end = 0, N-1
    for i in range(N):
        for j in range(N):
            if start < j < end:
                get1 += board[i][j]
                get4 += board[j][i]
            if i > N // 2 and end < j < start:
                get3 += board[i][j]
                get2 += board[j][i]
        start += 1
        end -= 1

    print("#{} {}".format(tc, max(get1, get2, get3, get4) - min(get1, get2, get3, get4)))
