def change(color):
    if color == 1:
        return 2
    else:
        return 1


def rock(row, col, color, N):
    global space
    other = change(color)
    space[col][row] = color

    di = [0, 1, 0, -1, 1, -1, 1, -1]
    dj = [1, 0, -1, 0, 1, -1, -1, 1]
    for i in range(8):
        ni = col + di[i]
        nj = row + dj[i]
        stack = []
        if 0 <= ni < N and 0 <= nj < N:
            if space[ni][nj] == other:
                while 0 <= ni < N and 0 <= nj < N and space[ni][nj] != 0 and space[ni][nj] != color:
                    stack.append([ni, nj])
                    ni += di[i]
                    nj += dj[i]
                if 0 <= ni < N and 0 <= nj < N:  # 같은색이 끝에 있다면
                    if space[ni][nj] == color:
                        while stack != []:
                            ni, nj = stack.pop()
                            space[ni][nj] = color


t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split())
    space = [[0] * N for i in range(N)]
    space[N // 2 - 1][N // 2 - 1: N // 2 + 1] = [2, 1]
    space[N // 2][N // 2 - 1: N // 2 + 1] = [1, 2]

    for m in range(M):
        row, col, color = map(int, input().split())
        rock(row - 1, col - 1, color, N)
        # print(space)

    black = 0
    white = 0
    for i in range(N):
        for j in range(N):
            if space[i][j] == 1:
                black += 1
            elif space[i][j] == 2:
                white += 1

    print("#{} {} {}".format(tc, black, white))
