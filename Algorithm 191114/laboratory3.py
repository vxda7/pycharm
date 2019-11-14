def f(start, end, left, chosen, where):
    global virus, empty, N, M, minV
    if start == end:
        print(where)
        # 퍼뜨리기
        tboard = [i[:] for i in board]
        tempty = 0
        stack = []
        maxtime = 0
        for one in where:
            stack.append(list(one) + [0])
        while stack != []:
            col, row, time = stack.pop(0)
            if maxtime < time:  # 한 경우에 최대 시간
                maxtime = time
            for direct in direction:
                nc = col + direct[0]
                nr = row + direct[1]
                if 0 <= nc < N and 0 <= nr < N:
                    if tboard[nc][nr] == 2:     # 비활성바이러스면
                        tboard[nc][nr] = 3      # 활성!
                        stack.append((nc, nr, time + 1))
                    elif tboard[nc][nr] == 0:   # 비어있으면
                        tboard[nc][nr] = 3
                        tempty += 1
                        stack.append((nc, nr, time + 1))
                    # 바이러스 또는 벽이면 무시
        if empty == tempty:     # 빈 공간에 모두 바이러스를 퍼뜨렸다면
            # print(maxtime, where)
            if minV > maxtime:
                minV = maxtime
    else:
        # 선택
        for one in virus_place:
            if one not in where:
                board[one[0]][one[1]] = 3
                f(start + 1, end, left - 1, chosen + 1, where + [one])
                board[one[0]][one[1]] = 2

            # 안선택
            if left <= M - chosen:
                f(start, end, left - 1, chosen + 1, where)



N, M = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
virus = 0   # 바이러스 갯수
virus_place = []    # 바이러스 좌표
empty = 0   # 채워야할 공간
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus += 1
            virus_place.append((i, j))
        elif board[i][j] == 0:
            empty += 1

minV = 10000
# 정보입력 끝
f(0, M, virus, 0, [])
if minV == 10000:
    print(-1)
else:
    print(minV)
