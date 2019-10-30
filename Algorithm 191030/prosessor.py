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


# 가능성 정보 만드는 함수
def findpossible(n):
    global possible, infos
    for i in range(n):
        possible.append(isit(infos[i], n))


temp = []
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


def find(direction, tempboard, n, idx):
    global infos
    # 1 : 아래, 2 : 오른쪽, 3 : 위, 4 : 왼쪽
    di = [0, (1, 0), (0, 1), (-1, 0), (0, -1)]
    col = infos[idx][0]  # 위치
    row = infos[idx][1]
    line = 0
    for i in range(n):
        nc = col + di[direction][0] * i
        nr = row + di[direction][1] * i
        if 0 <= nc < n or 0 <= nr < n:
            tempboard[nc][nr] = 2
        else:
            break
    return i


def best(chosen, n):
    global minV, board
    tempboard = [[]*n for i in range(n)]

    for i in range(n):
        for j in range(n):
            tempboard[i][j] = board[i][j]
    lines = 0
    for i in range(n):
        if chosen[i] != 0:
            lines += find(chosen[i], tempboard, n, i)




t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    board = [list(map(int, input().split())) for i in range(N)]
    infos = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                infos.append((i, j))
    # 1 : 아래, 2 : 오른쪽, 3 : 위, 4 : 왼쪽
    possible = []
    findpossible(N)
    for i in range(N):
        possible[i].append(0)
    print(possible)
    # 0 : 선택안함
    chosen = []
    choose(0, N)
    print(chosen)

    minV = 100000000
    best(chosen, N)
    print("#{} {}".format(tc, minV))