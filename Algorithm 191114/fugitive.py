t = int(input())
for tc in range(1, t+1):
    # 세로, 가로, 맨홀위치 세로 가로, 지난 시간
    N, M, R, C, L = map(int, input().split())
    underground = [list(map(int, input().split())) for i in range(N)]
    # 0, 1, 2, 3 상하좌우
    possible = [(), (0, 1, 2, 3), (0, 1), (2, 3), (0, 3), (1, 3), (1, 2), (0, 2)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    stack = [(R, C, 1)]

    while stack != []:
        col, row, time = stack.pop(0)
        shape = underground[col][row]
        underground[col][row] = 9  # 지나간 곳
        if shape != 9 and time < L:  # 안지나온 곳일 때   시간이 남았을 때
            for one in possible[shape]:
                nc = col + directions[one][0]
                nr = row + directions[one][1]
                if 0 <= nc < N and 0 <= nr < M:
                    # 0, 1, 2, 3 상하좌우
                    next = underground[nc][nr]
                    if next != 0 and next != 9:
                        if one == 0 and 1 in possible[next]:    # 위 아래 만남
                            stack.append((nc, nr, time + 1))
                        elif one == 1 and 0 in possible[next]:  # 아래 위 만남
                            stack.append((nc, nr, time + 1))
                        elif one == 2 and 3 in possible[next]:  # 좌우 만남
                            stack.append((nc, nr, time + 1))
                        elif one == 3 and 2 in possible[next]:  # 우좌 만남
                            stack.append((nc, nr, time + 1))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if underground[i][j] == 9:
                cnt += 1
    print("#{} {}".format(tc, cnt))