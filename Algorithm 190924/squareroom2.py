import sys

sys.stdin = open("input (9).txt", "r")


def find(col, row, N):
    D[col][row] = 1
    q = []
    q.append((col, row))
    maxV = 1
    while q:
        ac, ar = q.pop()
        for i in range(4):
            nc = ac + dc[i]
            nr = ar + dr[i]
            if 0 <= nc < N and 0 <= nr < N:
                if building[nc][nr] == building[ac][ar] + 1:
                    if D[nc][nr] < D[ac][ar] + 1:
                        q.append((nc, nr))
                    D[nc][nr] = max(D[nc][nr], D[ac][ar] + 1)
                    if maxV < D[nc][nr]:
                        maxV = D[nc][nr]
    return maxV


t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    building = [list(map(int, input().split())) for i in range(N)]
    maxV = 0
    minn = 10000000
    D = [[0] * N for i in range(N)]
    dc = [0, 1, 0, -1]
    dr = [1, 0, -1, 0]
    for i in range(N):
        for j in range(N):
            nowV = find(i, j, N)
            if maxV < nowV:
                maxV = nowV
                minn = building[i][j]
            elif maxV == nowV:
                if minn > building[i][j]:
                    minn = building[i][j]

    print("#{} {} {}".format(tc, minn, maxV))
