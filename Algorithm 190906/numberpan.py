def find(i, j, n, s):
    global collection
    global board
    dc = [0, 1, 0, -1]
    dr = [1, 0, -1, 0]
    if n == 7:
        collection.add(s)
    else:
        for k in range(4):
            nc = i + dc[k]
            nr = j + dr[k]
            if 0 <= nc < 4 and 0 <= nr < 4:
                find(nc, nr, n + 1, s + str(board[nc][nr]))


t = int(input())
for tc in range(1, t + 1):
    N = 4
    board = [list(map(int, input().split())) for i in range(N)]
    collection = set()
    for i in range(N):
        for j in range(N):
            find(i, j, 0, '')

    print("#{} {}".format(tc, len(collection)))