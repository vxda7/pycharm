<<<<<<< HEAD
import sys

# sys.stdin = open('sample_input.txt', 'r')


def remain(temp, w, h):
    hap = 0
    for i in range(h):
        for j in range(w):
            if temp[i][j]:
                hap += 1
    return hap


def destroy(order, n, w, h):
    global board
    temp = [0] * h
    for i in range(h):
        temp[i] = board[i][:]

    di = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for one in order:
        idx = h - 1
        while temp[idx][one] != 0 or idx != 0:
            idx -= 1

        stack = [(idx, one)]
        while stack != []:
            col, row = stack.pop()
            for i in di:
                for j in range(1, temp[col][row]):
                    nc = col + i[0] * j
                    nr = row + i[1] * j
                    if 0 <= nc < n and 0 <= nr < n:
                        temp[nc][nr] = 0
                        stack.append((nc, nr))
    return remain(temp, w, h)


def perp(start, end):
    if start == end:
        choose.append(line[:])
    else:
        for i in range(start, N):
            line[start], line[i] = line[i], line[start]
            perp(start + 1, end)
            line[start], line[i] = line[i], line[start]
=======
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

>>>>>>> dfc355c39ca8ec99513a1d691387b22b12e5d77c


t = int(input())
for tc in range(1, t + 1):
    N, W, H = map(int, input().split())
    line = list(range(H))
    choose = []
<<<<<<< HEAD
    perp(0, N)
    minV = 0
    board = [list(map(int, input().split())) for i in range(H)]
    print(choose)
    for one in choose:
        res = destroy(one, N, W, H)
        if res < minV:
            minV = res

    print("#{} {}".format(tc, minV))
=======
    perp(0, N, W)
    board = [list(map(int, input().split())) for i in range(H)]
    for one in choose:
        destroy(one, W, H)
>>>>>>> dfc355c39ca8ec99513a1d691387b22b12e5d77c
