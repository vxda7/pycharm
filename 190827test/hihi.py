# 0211907

t = int(input())
for tc in range(1, t+1):
    n, m, k = map(int, input().split())      # 세로n 가로m 칠횟수k
    space = [[0] * m for i in range(n)]  # 색칠할 공간
    for i in range(k):  # k 번 칠!
        y1, x1, y2, x2, black = map(int, input().split())
        clear = True
        for j in range(y1,y2+1):
            for i in range(x1,x2+1):
                if space[j][i] > black:
                    clear = False

        if clear == True:   # 명도가 더 진한 색이 칠할 공간에 없으면
            for j in range(y1, y2 + 1):
                for i in range(x1, x2 + 1):
                    space[j][i] = black

    # print(space)
    cntcolor = {key:0 for key in range(11)}

    for j in range(n):
        for i in range(m):
            cntcolor[space[j][i]] += 1
    # print(cntcolor)
    print("#{} {}".format(tc, max(cntcolor.values())))



