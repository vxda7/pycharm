def f(left, want, where):     # 고를때 증가, 고를 수, 남은 안고른 바이러스 수, 골라진 바이러스 좌표
    global virus, empty, N, M, minV
    if want == 0:
        # 퍼뜨리기
        tboard = [i[:] for i in board]
        tempty = 0
        stack = []
        maxtime = 0
        for one in where:
            # print(where)
            stack.append(list(one) + [0, 0])
        while stack != []:
            col, row, time, isitvirus = stack.pop(0)
            if tboard[col][row] == 2:
                tboard[col][row] = 3
            if maxtime < time and isitvirus == 0:  # 한 경우에 최대 시간
                maxtime = time
            # if empty == tempty:
            #     # print(time)
            #     # if time == 3:
            #     #     print(tboard)
            #     #     print(where)
            #     break
            for direct in direction:
                nc = col + direct[0]
                nr = row + direct[1]
                if 0 <= nc < N and 0 <= nr < N:
                    if tboard[nc][nr] == 2:     # 비활성바이러스면
                        tboard[nc][nr] = 3      # 활성!
                        stack.append((nc, nr, time + 1, 1))
                        # if where == [(0, 0), (1, 5), (3, 0), (4, 3)]:
                        #     for iii in tboard:
                        #         print(iii)
                        #     print('#####################', time + 1)
                    elif tboard[nc][nr] == 0:   # 비어있으면
                        tboard[nc][nr] = 3
                        tempty += 1
                        stack.append((nc, nr, time + 1, 0))
                        # if where == [(0, 0), (1, 5), (3, 0), (4, 3)]:
                        #     for iii in tboard:
                        #         print(iii)
                        #     print('#####################', time + 1)
                    # 바이러스 또는 벽이면 무시
        if empty == tempty:     # 빈 공간에 모두 바이러스를 퍼뜨렸다면
            # print(maxtime, where)
            if minV > maxtime:
                # print(where)
                minV = maxtime
    elif left < want:
        return
    else:
        where[want - 1] = virus_place[left - 1]
        f(left - 1, want - 1, where)
        f(left - 1, want, where)


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
f(virus, M, [0]*M)
if minV == 10000:
    print(-1)
else:
    print(minV)
