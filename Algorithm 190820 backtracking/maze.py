def find(sRow, sCol):
    dRow = [0, 1, 0, -1]
    dCol = [1, 0, -1, 0]
    s = []
    s.append([sRow, sCol])  # 입구로 이동
    maze[sRow][sCol] = 1    # 방문 표시
    while(len(s) != 0):
        n = s.pop()         # 이동할 칸 좌표를 꺼내고
        for i in range(4):  # 주변 좌표를 계산
            nRow = n[0] + dRow[i]
            nCol = n[1] + dCol[i]
            if 0 <= nRow < N and 0 <= nCol < N:  # 미로 내부인지확인
                if maze[nRow][nCol] == 3:       # 목적지인 경우 1 반환
                    return 1
                elif maze[nRow][nCol] == 0:     # 갈 수 있는 곳 저장
                    s.append([nRow, nCol])
                    maze[n[0]][n[1]] = 1
    return 0    # 출구에 도달하지 못하고 모든 칸 방문

# test_case = int(input())
# for case in range(test_case):
#     N = int(input())
#     maze =[]
#     startx, starty, endx, endy =0
#     for i in range(N):
#         get = list(input())
#         maze.append(get)
#         if '2' in get:
#             starty = i
#             startx = get.index('2')
#         elif '3' in get:
#             starty = i
#             startx = get.index('3')
#
#     dir = 1
#     for j in range(N**2):
#         if maze[starty][startx+1] == '0':


def f(i, j):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    global maze
    global N
    # if maze[i][j] == '1':
    #     return 0
    if maze[i][j] == '3':
        return 1
    else:
        maze[i][j] = '1'    # 방문 표시, 벽으로 바꿈
        # 이동할 좌표 생성
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni >= 0 and ni<N and nj>=0 and nj<N:
                if maze[ni][nj] != '1':   # 벽이 아니면 방문
                    if f(ni, nj) == 1:  # 진행방향에서 목적지를 찾은 경우
                        return 1
        return 0    # 현재위치에서 갈 수 있는 방향에서 목적지를 찾지 못함, 이전의 다른방향 탐색

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    startI = 0
    srattJ = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == "2":
                startI = i
                startJ = j
                break
        else:
            continue
        break

    print("#{} {}".format(tc, f(startI, startJ)))