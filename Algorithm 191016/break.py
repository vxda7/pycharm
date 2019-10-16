def howmany(w, h):
    cnt = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] != 0:
                cnt += 1
    return cnt

def calmdown(w, h):
    global board
    empty = [[0]*w for i in range(h)]
    for i in range(w):
        idx = h-1
        for j in range(h-1, -1, -1):
            if board[j][i] != 0:
                empty[idx][i] = board[j][i]
                idx -= 1
    board = empty

def find(n, w, h, x, left):
    where = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    col = h - 1
    while board[col][x] != 0:
        col -= 1
        if col == -1:
            break
    queue = [(col, x)]
    while queue != []:
        one = queue.pop(0)
        if col != -1:
            for boom in range(board[col][x]):
                for dir in where:
                    cd = col + dir[0]
                    rd = x + dir[1]
                    if 0 <= cd < h and 0 <= rd < w:
                        board[cd][rd] = 0

    calmdown(w, h)
    return howmany(w, h)


t = int(input())
for tc in range(1, t + 1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(H)]
    all = howmany(W, H)

    print("#{} {}".format(tc, maxV))
