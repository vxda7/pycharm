def check(i, j):  # 근처 지뢰 갯수 찾기
    global board
    global N
    dc = [0, 1, 0, -1, 1, 1, -1, -1]
    dr = [1, 0, -1, 0, 1, -1, 1, -1]
    cnt = 0
    for k in range(8):
        nc = i + dc[k]
        nr = j + dr[k]
        if 0 <= nc < N and 0 <= nr < N:
            if board[nc][nr] == '*':
                cnt += 1
    return cnt


def change(i, j):
    global board
    global N
    dc = [0, 1, 0, -1, 1, 1, -1, -1]
    dr = [1, 0, -1, 0, 1, -1, 1, -1]
    stack = [[i, j]]
    board[i][j] = 0  # 누른 곳 바꾸기
    while stack != []:
        # print(stack)
        col, row = stack.pop()
        for k in range(8):
            nc = col + dc[k]
            nr = row + dr[k]
            if 0 <= nc < N and 0 <= nr < N:
                one = check(nc, nr)
                if one == 0 and board[nc][nr] == '.':
                    board[nc][nr] = 0
                    stack.append([nc, nr])
                else:
                    board[nc][nr] = one


def click(N):
    global board
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == '.' and check(i, j) == 0:
                change(i, j)
                cnt += 1
    return cnt


t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    board = [list(input()) for i in range(N)]
    # print(board)
    cnt = click(N)
    # print(board)
    # print(cnt)

    for i in range(N):
        for j in range(N):
            if board[i][j] == '.':
                cnt += 1

    print("#{} {}".format(tc, cnt))
