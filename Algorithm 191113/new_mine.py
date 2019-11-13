t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    board = [list(input()) for i in range(N)]

    # 정보가공
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]
    mines = [board[i][:] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == '.':
                cnt = 0
                for direct in direction:
                    col, row = i + direct[0], j + direct[1]
                    if 0 <= col < N and 0 <= row < N:
                        if board[col][row] == "*":
                            cnt += 1
                mines[i][j] = cnt

    # 지뢰가 없는 공간 다 누르기

    click = 0
    for i in range(N):
        for j in range(N):
            if mines[i][j] == 0 and board[i][j] == '.':
                click += 1
                board[i][j] = 0
                stack = [(i, j)]
                while stack != []:
                    col, row = stack.pop()
                    for direct in direction:
                        nc, nr = col + direct[0], row + direct[1]
                        if 0 <= nc < N and 0 <= nr < N:
                            if mines[col][row] == 0 and board[nc][nr] == '.':    # 0일 때
                                stack.append((nc, nr))  # 추가
                                board[nc][nr] = mines[nc][nr]


    for i in range(N):
        for j in range(N):
            if board[i][j] == '.':
                click += 1

    print("#{} {}".format(tc, click))


