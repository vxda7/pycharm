def f(i, j, e, N):  # i,j 좌표, e 지나온 칸 수, N 미로의 크기
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    global maze
    global minV
    if maze[i][j] == 3:  # 도착지면
        if minV > 0:
            minV = e
    else:  # 도착지가 아니면
        maze[i][j] = 1  # 현재칸에 방문 표시(진행 방향에서 다시 들어오는 것 방지)
        for k in range(4):  # 이동 가능한 칸으로 이동
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:  # 미로를 벗어나지 않고
                if maze[ni][nj] != 1:  # 갈 수 있는 칸이면(벽이아니면)
                    f(ni, nj, e + 1, N)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [[int(x) for x in input()] for i in range(N)]
    sRow, sCol = 0, 0
    for i in range(N):
        if 2 in maze[i]:
            sRow = i
            sCol = maze[i].index(2)
    minV = 1000000000000
    f(sRow, sCol, 0, N)
    if minV == 1000000000000:
        minV = 0
    else:
        minV -= 1
    print("#{} {}".format(tc, minV))
