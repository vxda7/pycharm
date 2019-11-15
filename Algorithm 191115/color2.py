t = int(input())
for tc in range(1, t+1):
    # N: 노드의 갯수, E: 간선의 갯수, M: 색상 수
    N, E, M = map(int, input().split())
    board = [[[]] + [0]*N for i in range(N + 1)]

    for i in range(E):
        a, b = map(int, input().split())
        board[a][b] = 1
        board[b][a] = 1

    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            color = 1
            while board[0][i] == 0:
                if color not in board[i][0]:
                    board[0][i] = color
                    for k in range(1, N + 1):
                        if not i and color not in board[k][0]:
                            board[k][0].append(color)
                color += 1

    print(board)