def find(start, N, K):
    direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    stack = [start]
    maxV = 0
    while stack != []:
        col, row, howlong, shovel, before, visited = stack.pop()
        if howlong > maxV:
            maxV = howlong
        for d in direction:
            nc = col + d[0]
            nr = row + d[1]
            if 0 <= nc < N and 0 <= nr < N:    # 칸안에 들어오는지?
                if (nc, nr) not in visited:
                    if before == 100:  # 전에 안팠다면
                        if board[col][row] > board[nc][nr]:    # 전보다 낮은 곳인지 확인
                            stack.append((nc, nr, howlong + 1, shovel, 100, visited + [(nc, nr)]))
                        else:  # 낮은 곳이지만 팔 수 있는지?
                            if shovel:
                                if board[col][row] > board[nc][nr] - K:  # 파면 전보다 낮아지는지 확인
                                    stack.append((nc, nr, howlong + 1, False, board[col][row] - 1,
                                                  visited + [(nc, nr)]))  # 더이상 못판다고 알려주고, 얼마나 패였는지 보내주기
                    else:       # 전에 팠다면
                        if before > board[nc][nr]:
                            stack.append((nc, nr, howlong + 1, shovel, 100, visited + [(nc, nr)]))
    return maxV


t = int(input())
for tc in range(1, t+1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(N)]

    #  가장 높은 곳 찾기
    highest = [0]
    maxhigh = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > maxhigh:
                highest = [(i, j, 1, True, 100, [(i, j)])]
                maxhigh = board[i][j]
            elif board[i][j] == maxhigh:
                highest.append((i, j, 1, True, 100, [(i, j)]))

    maxV = 0
    for high in highest:
        now = find(high, N, K)
        if now > maxV:
            maxV = now

    print("#{} {}".format(tc, maxV))
