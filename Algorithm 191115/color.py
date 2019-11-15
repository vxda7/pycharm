
t = int(input())
for tc in range(1, t+1):
    # N: 노드의 갯수, E: 간선의 갯수, M: 색상 수
    N, E, M = map(int, input().split())
    nlist = [0] * (N + 1)
    board = [[[]] + [0]*N for i in range(N + 1)]
    # color = set(range(1, M + 1))

    for i in range(E):
        a, b = map(int, input().split())
        board[a][b] = 1
        board[b][a] = 1
        yeab, yeah = True, True
        color = 1
        # a색 정하기
        while yeab and yeah:
            if color[0][a] == 0:
                if color not in board[a][0] and color != board[0][b]:
                    board[0][a] = color
                    board[b][0].append(color)
                    yeab = False
            else:
                if color[0][a] not in board[b][0]:
                    board[b][0].append(color[0][a])
                    yeab = False
            if color[0][b] == 0:
                if color not in board[b][0] and color != board[0][a]:
                    board[0][b] = color
                    board[a][0].append(color)
                    yeah = False
            color += 1
        # while yeab and yeah:
        #     if color not in board[a][0] and color not in board[b][0]:
        #         board[a][0].append(color)
        #         board[b][0].append(color)
        #         yeab = False
        #     if color not in board[a][0] and color not in board[b][0]:
        #         board[b][0].append(color)
        #         board[a][0].append(color)
        #         yeah = False
        #     color += 1
    print(board)
    ok = 1
    for one in board[0][1:]:
        if one > M:
            ok = 0
    print("#{} {}".format(tc, ok))
