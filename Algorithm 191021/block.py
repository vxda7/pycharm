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


t = int(input())
for tc in range(1, t + 1):
    N, W, H = map(int, input().split())
    line = list(range(N))
    choose = []
    perp(0, N)
    minV = 0
    board = [list(map(int, input().split())) for i in range(H)]
    print(choose)
    for one in choose:
        res = destroy(one, N, W, H)
        if res < minV:
            minV = res

    print("#{} {}".format(tc, minV))
