t = int(input())
for testcase in range(1, t+1):
    n, m = map(int, input().split())

    board = [[0]*n for i in range(n)]
    center = n//2-1
    board[center][center] = 2
    board[center + 1][center] = 1
    board[center][center + 1] = 1
    board[center + 1][center + 1] = 2

    # print(board)
    for cmd in range(m):
        row, col, color = map(int, input().split())
        board[col-1][row-1] = color
        other = 1
        if color == 1:
            other = 2
        dr = [1, 0, -1, 0, 1, 1, -1, -1]
        dc = [0, 1, 0, -1, 1, -1, 1, -1]

        for i in range(8):
            nr = row - 1  # 인덱스 맞춤
            nc = col - 1  # 인덱스 맞춤
            nr += dr[i]
            nc += dc[i]
            stack = []
            while 0 <= nr < n and 0 <= nc < n and board[nc][nr] != 0 and board[nc][nr] != color:
                stack.append([nr, nc])
                nr += dr[i]
                nc += dc[i]
            # print(stack,end=" ")
            if 0 <= nr < n and 0 <= nc < n:
                if board[nc][nr] == color:
                    while stack != []:
                        tr, tc = stack.pop()
                        board[tc][tr] = color
        # print(board)

    cntblack = 0
    cntwhite = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cntblack += 1
            elif board[i][j] == 2:
                cntwhite += 1

    print("#{} {} {}".format(testcase, cntblack, cntwhite))




