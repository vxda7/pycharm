def find(N):
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            if k != i:
                for j in range(1, N + 1):
                    if j != k and j != i:
                        # dpboard[i][j] = min(dpboard[i][k] + dpboard[k][j], dpboard[i][j])
                        if dpboard[i][k] and dpboard[k][j]:
                            dpboard[i][j] = 1

t = int(input())
for tc in range(1, t+1):
    N = int(input())    # 학생 수
    M = int(input())    # 화살표 수
    dpboard = [[0]*(N + 1) for i in range(N + 1)]
    for i in range(M):
        a, b = map(int, input().split())
        dpboard[a][b] = 1
    find(N)
    # print(dpboard)
    can = 0
    for i in range(1, N + 1):
        cnt = 0
        for j in range(1, N + 1):
            if dpboard[i][j] != 0:
                cnt += 1
            elif dpboard[j][i] != 0:
                cnt += 1
        if cnt == N - 1:
            can += 1
    print("#{} {}".format(tc, can))