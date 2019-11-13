def find(board, N):
    click = 0
    di = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]

    # 숫자 모두 확인하기 0 인 공간 다 누르기
    for i in range(N):
        for j in range(N):
            # 값이 0이면서 .이 찍힌 보드 부터 다 누르기
            if board[i][j] == '.':
                stack = [(i, j)]
                while stack != []:
                    co, ro = stack.pop(0)
                    if board[co][ro] == '.':
                        # co, ro의 지뢰갯수
                        cnt = 0
                        for d in di:
                            nc, nr = co + d[0], ro + d[1]
                            if 0 <= nc < N and 0 <= nr < N:
                                if board[co][ro] == '*':
                                    cnt += 1
                        # 지뢰가 없는 칸이라면
                        if cnt == 0:
                            if i == co and j == ro:
                                click += 1
                                board[co][ro] = 0
                            for d in di:
                                ncc, nrr = co + d[0], ro + d[1]
                                if 0 <= ncc < N and 0 <= nrr < N:
                                    if board[ncc][nrr] == '.':
                                        stack.append((ncc, nrr))
                        else:   # 지뢰가 근처에 있다면
                            board[nc][nr] = cnt

    for i in range(N):
        for j in range(N):
            if board[i][j] == '.':
                click += 1
    return click


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    board = [list(input()) for i in range(N)]
    res = find(board, N)
    print("#{} {}".format(tc, res))