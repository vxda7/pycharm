import sys
sys.stdin = open("sample_input (1).txt", "r")

def find(col, row, data):
    global mountain
    global best
    global maxV

    dc = [0, 1, 0, -1]
    dr = [1, 0, -1, 0]
    for i in range(4):
        nc = col + dc[i]
        nr = row + dr[i]
        if 0 <= nc < N and 0 <= nr < N:
            if mountain[col][row] > mountain[nc][nr]:
                find(nc, nr, data+1)
    if maxV < data:
        maxV = data


t = int(input())
for tc in range(1, t+1):
    N, K = map(int, input().split())
    mountain = []
    best = 0
    for i in range(N):
        get = list(map(int, input().split()))
        mountain.append(get)
        for j in range(N):
            if get[j] > best:
                best = get[j]

    maxV = 0
    data = 1
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == best:
                find(i, j, data)

    print("#{} {}".format(tc, maxV))