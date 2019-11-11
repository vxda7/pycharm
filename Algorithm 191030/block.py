import sys, time
sys.stdin = open("sample_input (1).txt", "r")
start = time.time()

def destroy(chosen, w, h):
    global maxV
    temp = [[0] * w for i in range(h)]
    for i in range(h):
        for j in range(w):
            temp[i][j] = board[i][j]

    di = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for one in chosen:
        idx = 0  # 벽돌의 제일 위
        while temp[idx][one] == 0:
            idx += 1
            if idx == h:
                idx = h - 1
                break
        stack = [(idx, one)] + ([(-1, -1)] * 180)
        # while stack != []:
        #     col, row = stack.pop(0)
        #     xs = temp[col][row]
        #     temp[col][row] = 0
        #     if xs > 1:
        #         for d in di:
        #             for x in range(1, xs):
        #                 nc = col + d[0] * x
        #                 nr = row + d[1] * x
        #                 if 0 <= nc < h and 0 <= nr < w:
        #                     if temp[nc][nr] != 0:
        #                         stack.append((nc, nr))
        #                     elif temp[nc][nr] == 1:
        #                         temp[nc][nr] = 1
        ####################
        startidx = 0
        endidx = 1
        while startidx != endidx:
            col, row = stack[startidx]
            startidx += 1
            endidx += 1
            xs = temp[col][row]
            temp[col][row] = 0
            if xs > 1:
                for d in di:
                    for x in range(1, xs):
                        nc = col + d[0] * x
                        nr = row + d[1] * x
                        if 0 <= nc < h and 0 <= nr < w:
                            if temp[nc][nr] != 0:
                                stack[endidx] = (nc, nr)
                                endidx += 1
                            elif temp[nc][nr] == 1:
                                temp[nc][nr] = 1


        ####################

        # hap = 0
        # for z in range(h):
        #     hap += sum(temp[z])
        # if hap == 0:
        #     return 0

        # 내려주기
        temp = list(zip(*temp))
        change = []
        for tem in temp:
            word = ''.join(list(map(str,tem))).replace('0', '')
            word_len = len(word)
            word = '0' * (h - word_len) + word
            change.append(list(map(int, word)))
        temp = list(map(list, zip(*change)))
        if chosen == [2, 2, 6]:
            print(temp)


    cnt = 0
    # print(temp, h, w)
    for i in range(h):
        for j in range(w):
            if temp[i][j]:
                cnt += 1
    return cnt

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
    # cnt = 0
    # for i in range(H):
    #     for j in range(W):
    #        if board[i][j]:
    #            cnt += 1
    minV = 10000000000
    # print(choose)
    for one in choose:
        answer = destroy(one, W, H)
        if minV > answer:
            minV = answer
    print("#{} {}".format(tc, minV))

print(time.time() - start)