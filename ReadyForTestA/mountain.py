def find(top, N, K):
    global earth
    trycnt = []
    cnt = 0
    while top != []:
        piece = top.pop()
        high = piece[0]
        topcol = piece[1]
        toprow = piece[2]
        tempsave = top[-1]
        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]
        for dir in range(4):
            ni = topcol + di[dir]
            nj = toprow + dj[dir]
            if 0 <= ni < N and 0 <= nj < N:
                if earth[ni][nj] < high:
                    top.append([earth[ni][nj], ni, nj])
        if top[-1] == tempsave:
            trycnt.append()


import sys

sys.stdin = open('sample_input.txt', 'r')

t = int(input())
for tc in range(1, t + 1):
    N, K = map(int, input().split())
    earth = []
    best = 0
    top = []
    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(N):
            if best < line[j]:
                best = line[j]
                top = [[best, i, j]]
            elif best == line[j]:
                top.append([best, i, j])

    print(top)
    # _____ 입력
    # print("#{} {}".format(tc, find(top, N, K)))
