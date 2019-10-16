def howmany(w, h):  # 전체에 부서지지 않은 부분 세주는 함수
    global minV
    cnt = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] != 0:
                cnt += 1
    if minV > cnt:
        minV = cnt
    return cnt

def calmdown(w, h): # 부수고 나서 전부 밑으로 내려줌
    global board
    empty = [[0]*w for i in range(h)]
    for i in range(w):
        idx = h-1
        for j in range(h-1, -1, -1):
            if board[j][i] != 0:
                empty[idx][i] = board[j][i]
                idx -= 1
    board = empty

def find(w, h, x): # 원하는 위치를 주면 다 부숴주는 함수
    where = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    col = h - 1
    while board[col][x] != 0:
        col -= 1
        if col == -1:
            break
    
    queue = [(col, x)]  # 첫 위치는 지정
    while queue != []:
        one = queue.pop(0)
        if col != -1:   # 처음에 바닥에 닿지 않았다면
            for boom in range(board[one[0]][one[1]] - 1):
                for direction in where:
                    cd = col + direction[0]
                    rd = x + direction[1]
                    if 0 <= cd < h and 0 <= rd < w:
                        board[cd][rd] = 0
                        queue.append((cd, rd))
    calmdown(w, h)
    return howmany(w, h)


def choice(w, start, end, empty):
    global choose
    if start == end:
        choose.append(empty)
    else:
        for i in range(w):
            empty.append(i)
            choice(w, start+1, end, empty)
            empty.pop()



t = int(input())
for tc in range(1, t + 1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(H)]
    choose = []
    empty = []
    choice(W, 0, N, empty)
    print(choose)
    print("#{} {}".format(tc, minV))
