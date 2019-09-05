def change(get):
    if get == 1:
        return 2
    elif get == 2:
        return 1
    elif get == 3:
        return 4
    elif get == 4:
        return 3
    print("change Error")


t = int(input())
for tc in range(1, t + 1):
    N, M, K = map(int, input().split())
    space = [[0] * N for i in range(N)]
    for i in range(K):
        col, row, nums, direct = map(int, input().split())
        space[col][row] = [nums, direct]
    # 0을 제외한 이동방향 상하좌우
    dc = [0, -1, 1, 0, 0]
    dr = [0, 0, 0, -1, 1]
    while M != 0:
        for i in range(N):
            for j in range(N):
                if space[i][j] != 0:
                    direction = space[i][j][1]
                    ni = i+dc[direction]
                    nj = j+dr[direction]
                    if space[ni][nj] != 0:


                    if i == N or i == 0 or j == N or j == 0:
                        space[i][j][0] //= 2
                        original = space[i][j][1]
                        space[i][j][1] = change(original)

        M -= 1
