def find(i, N, left, right, col, l, r, c, board):
    global cnt
    if i == N:  # 모든 줄에 퀸을 놓은 경우
        cnt += 1
    else:
        for j in range(N):
            # 다른 줄에 j번 열에 퀸이 없어야 하고
            # 왼쪽 대각선과 오른쪽 대각선에 퀸이 없어야 한다.
            # if check(i, j, N):
            if i + j not in left and i - j + N not in right and j not in col:
                board[i][j] = 1
                left[l] = i + j
                right[r] = i - j + N
                col[c] = j
                l += 1
                r += 1
                c += 1
                find(i + 1, N, left, right, col, l, r, c, board)
                board[i][j] = 0
                l -= 1
                r -= 1
                c -= 1
                left[l] = -1
                right[r] = -1
                col[c] = -1



t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    cnt = 0
    board = [[0] * N for i in range(N)]
    left, right, col = [-1] * (N * N), [-1] * (N * N), [-1] * (N * N)
    l, r, c = 0, 0, 0
    find(0, N, left, right, col, l, r, c, board)
    print("#{} {}".format(tc, cnt))

# def check(col, row, N):
#     global board
#     for i in range(N):
#         if 0 <= col - i < N:
#             if board[i][row] == 1:
#                 return False
#             if 0 <= row + i < N:
#                 if board[col - i][row + i] == 1:
#                     return False
#             if 0 <= row - i < N:
#                 if board[col - i][row - i] == 1:
#                     return False
#     return True
