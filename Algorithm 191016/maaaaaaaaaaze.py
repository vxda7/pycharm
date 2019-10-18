from copy import deepcopy
# import time
# start = time.time()

def perm(n, k):
    if n == k:
        possible.append(deepcopy(order))
    else:
        for i in range(n, k):
            order[n], order[i] = order[i], order[n]
            perm(n + 1, k)
            order[n], order[i] = order[i], order[n]


def rot(what, ks):
    temp = [[0] * 5 for _ in range(5)]
    for k in range(ks + 1):
        for i in range(5):
            for j in range(5):
                temp[j][4 - i] = what[i][j]
    return temp


def maze(puzzle):  # 3차원 미로 최단 탈출 bfs
    global minV
    if puzzle[0][0][0] == 0 or puzzle[4][4][4] == 0:
        return 10000  # 시작점과 끝점을 못 들어간다면 최대값 반환
    di = [(0, 0, 1), (0, 1, 0), (1, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
    queue = [(0, 0, 0)]
    puzzle[0][0][0] == 2  # 도중에 1이 나오면 안되므로 시작점 2
    while queue != []:
        x, y, z = queue.pop(0)
        for d in di:
            dx = x + d[0]
            dy = y + d[1]
            dz = z + d[2]
            if 0 <= dx < 5 and 0 <= dy < 5 and 0 <= dz < 5:
                if puzzle[dx][dy][dz] == 1:
                    puzzle[dx][dy][dz] = puzzle[x][y][z] + 1
                    queue.append((dx, dy, dz))
                    if puzzle[dx][dy][dz] - 1 >= minV:
                        return 10000
                    if dx == 4 and dy == 4 and dz == 4:
                        return puzzle[4][4][4] - 1  # 시작점이 2이므로 빼주기
    return 10000  # 출발 도착은 갈 수 있지만 도착할 수 없으면 최대값 반환


def choose(one, get):
    empty = [0, 0, 0, 0, 0]
    idx = 0
    for i in one:
        empty[i] = get[idx]
        idx += 1
    return empty


def answer(get):
    global minV

    for i in range(4):  # 각 판의 회전 경우
        get[0] = deepcopy(rot(get[0], i))
        for j in range(4):
            get[1] = deepcopy(rot(get[1], j))
            for k in range(4):
                get[2] = deepcopy(rot(get[2], k))
                for l in range(4):
                    get[3] = deepcopy(rot(get[3], l))
                    for m in range(4):
                        get[4] = deepcopy(rot(get[4], m))
                        for n in possible:
                            temp = deepcopy(choose(n, get))
                            # print(temp)
                            res = maze(temp)
                            if res < minV:
                                minV = res
                                if minV == 12:
                                    return minV
    return minV


N = 5
board = [[list(map(int, input().split())) for i in range(N)] for j in range(N)]
order = [0, 1, 2, 3, 4]
possible = []  # 5개를 선택하는 120가지 경우의 수
perm(0, 5)
minV = 10000
# 결과값
res = answer(board)
if res == 10000:
    print(-1)
else:
    print(res)

# 보드 회전 테스트
# print(board[0])
# for i in range(4):
#     board[0] = deepcopy(rot(board[0], i))
#     print(board[0])

# 보드 선택 테스트
# for i in possible:
#     print(choose(i, board))

# 탈출 테스트
# print(maze(board))
# print(time.time()- start)