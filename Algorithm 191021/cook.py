t = int(input())
for tc in range(1, t+1):
    N = int(input())
    synergy = [list(map(int, input().split())) for i in range(N)]


t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    board = [list(map(int, input().split())) for i in range(N)]
    t1, t2, t3, t4 = 0, 0, 0, 0
    start, end = 0, N - 1
    for i in range(N):
        for j in range(N):
            if start < j < end:
                t1 += board[i][j]
                t3 += board[j][i]
            if i > N // 2:
                if end < j < start:
                    t2 += board[i][j]
                    t4 += board[j][i]

        start += 1
        end -= 1
    print("#{} {}".format(tc, max(t1, t2, t3, t4) - min(t1, t2, t3, t3)))