import time, sys
from memory_profiler import profile
start = time.time()
sys.stdin = open('sample_input.txt', 'r')


def isit(one, n):
    global board
    if one[0] == 0 or one[0] == n - 1 or one[1] == 0 or one[1] == n - 1:
        return []  # 이미 연결되어있음
    di = [0, (1, 0), (0, 1), (-1, 0), (0, -1)]
    where = []
    # 1 : 아래, 2 : 오른쪽, 3 : 위, 4 : 왼쪽
    for direction in range(1, 5):
        for i in range(1, n):
            one_col = one[0] + di[direction][0] * i
            one_row = one[1] + di[direction][1] * i
            if one_col < 0 or one_col > n - 1 or one_row < 0 or one_row > n - 1:
                where.append(direction)
                break
            if board[one_col][one_row] == 1:
                break
    return where[:]

temp = []
@profile
def choose(start, end):
    global chosen, possible
    if start == end:
        chosen.append(temp[:])
        return
    else:
        for c in possible[start]:
            temp.append(c)
            choose(start + 1, end)
            temp.pop()


# def find(direction, tempboard, n, idx):
#     global infos, di
#     # 1 : 아래, 2 : 오른쪽, 3 : 위, 4 : 왼쪽
#     col = infos[idx][0]  # 위치
#     row = infos[idx][1]
#     line = 0
#     for i in range(1, n):
#         nc = col + di[direction][0] * i
#         nr = row + di[direction][1] * i
#         if 0 <= nc < n and 0 <= nr < n:
#             if tempboard[nc][nr] == 2:
#                 return 0, 0
#             tempboard[nc][nr] = 2
#         else:
#             break
#     return i - 1, 1


# def best(chosen, n):
#     global board
#     lines = 0
#     connected = 0
#     maxV = 0
#     minV = 100000000
#     tempboard = [[0] * n for i in range(n)]
#
#     # 1 : 아래, 2 : 오른쪽, 3 : 위, 4 : 왼쪽
#     for chosed in chosen:
#         for i in range(n):
#             for j in range(n):
#                 tempboard[i][j] = board[i][j]
#
#         for i in range(n):
#             if chosed[i] != 0:
#                 res = find(chosed[i], tempboard, n, i)
#                 lines += res[0]
#                 connected += res[1]
#         if maxV <= connected:
#             maxV = connected
#             if minV > lines:
#                 minV = lines
#         lines = 0
#         connected = 0
#     return minV


t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    board = [list(map(int, input().split())) for i in range(N)]
    di = [0, (1, 0), (0, 1), (-1, 0), (0, -1)]
    infos = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                infos.append((i, j))
    # 1 : 아래, 2 : 오른쪽, 3 : 위, 4 : 왼쪽
    possible = []
    for i in range(N):
        ######################################
        if infos[i][0] == 0 or infos[i][0] == N- 1 or infos[i][1] == 0 or infos[i][1] == N - 1:
            where = [] #return []  # 이미 연결되어있음
        else:
            di = [0, (1, 0), (0, 1), (-1, 0), (0, -1)]
            where = []
            # 1 : 아래, 2 : 오른쪽, 3 : 위, 4 : 왼쪽
            for direction in range(1, 5):
                for i in range(1, N):
                    one_col = infos[i][0] + di[direction][0] * i
                    one_row = infos[i][1] + di[direction][1] * i
                    if one_col < 0 or one_col > N - 1 or one_row < 0 or one_row > N - 1:
                        where.append(direction)
                        break
                    if board[one_col][one_row] == 1:
                        break
        #####################################
        #possible.append(isit(infos[i], N))
        possible.append(where[:])
        where = []
    for i in range(N):
        possible[i].append(0)
    # 0 : 선택안함
    chosen = []
    choose(0, N)
    # print(chosen)
    # minV = best(chosen, N)


    #########################
    lines = 0
    connected = 0
    maxV = 0
    minV = 100000000
    tempboard = [[0] * N for i in range(N)]

    # 1 : 아래, 2 : 오른쪽, 3 : 위, 4 : 왼쪽
    for chosed in chosen:
        for i in range(N):
            for j in range(N):
                tempboard[i][j] = board[i][j]

        for i in range(N):
            if chosed[i] != 0:
                # res = find(chosed[i], tempboard, N, i)
                aha = True
                #########################################
                col = infos[i][0]  # 위치
                row = infos[i][1]
                line = 0
                for k in range(1, N):
                    nc = col + di[chosed[i]][0] * k
                    nr = row + di[chosed[i]][1] * k
                    if 0 <= nc < N and 0 <= nr < N:
                        if tempboard[nc][nr] == 2:
                            res = (0, 0)
                            aha = False
                            break
                        tempboard[nc][nr] = 2
                    else:
                        break
                if aha:
                    res = (k - 1, 1)
                ##########################################
                lines += res[0]
                connected += res[1]
        if maxV <= connected:
            maxV = connected
            if minV > lines:
                minV = lines
        lines = 0
        connected = 0
    ##########################
    print("#{} {}".format(tc, minV))


print(time.time() - start)