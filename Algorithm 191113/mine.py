def find(board, N):
    click = 0
    di = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]
    for i in range(N):
        for j in range(N):
            stack = [(i,j)]
            while stack != []:
                co, ro = stack.pop()
                if board[co][ro] == '.':
                    cnt = 0
                    for d in di:
                        col = co + d[0]
                        row = ro + d[1]
                        if 0 <= col < N and 0 <= row < N:
                            if board[col][row] == '*':
                                cnt += 1
                    if cnt == 0:
                        if board[co][ro] == '.':
                            board[co][ro] = 0
                            if i == co and j ==ro:
                                click += 1
                                print(board)

                    for d in di:
                        col = co + d[0]
                        row = ro + d[1]
                        if 0 <= col < N and 0 <= row < N:
                            if board[col][row] == '.' and board[co][ro] == 0:
                                stack.append((col, row))
                            elif board[col][row] == '.':

    return click


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    board = [list(input()) for i in range(N)]
    res = find(board, N)
    print("#{} {}".format(tc, res))