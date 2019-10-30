def destroy(chosen, w, h):
    temp = [[0] * w for i in range(h)]
    for i in range(h):
        for j in range(w):
            temp[i][j] = board[i][j]

    di = [(0, 1), (1, 0), (0, -1)]
    for one in chosen:
        idx = 0  # 벽돌의 제일 위
        while temp[idx][one] == 0:
            idx += 1
            if idx == h:
                idx = h - 1
                break
        stack = [(idx, one)]
        while stack != []:
            col, row = stack.pop(0)
            xs = temp[col][row]
            temp[col][row] = 0
            if xs > 1:
                for d in di:
                    for x in range(1, xs):
                        nc = col + d[0] * x
                        nr = row + d[1] * x
                        if 0 <= nc < h - 1 and 0 <= nr < w - 1:
                            stack.append((nc, nr))
    #     print(temp)
    print(chosen)
    print(temp)

    # 내려주기
    # 갯수세서 return



partial = []
def perp(start, end, w):
    global partial
    if start == end:
        choose.append(partial[:])
        return
    for i in range(w):
        partial.append(i)
        perp(start + 1, end, w)
        partial.pop()


t = int(input())
for tc in range(1, t + 1):
    N, W, H = map(int, input().split())
    line = list(range(H))
    choose = []
    perp(0, N, W)
    board = [list(map(int, input().split())) for i in range(H)]
    for one in choose:
        destroy(one, W, H)
