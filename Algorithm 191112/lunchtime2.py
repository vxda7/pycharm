# 1번계단일지 2번계단일지
possibles = []
for k in range(11):
    eachpossible = []
    for i in range(1 << k):
        temp = []
        for j in range(k):
            if i & (1 << j):
                temp.append(1)
            else:
                temp.append(0)
        eachpossible.append(temp)
    possibles.append(eachpossible)


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    board = [list(map(int, input().split())) for i in range(N)]
    stairs = []
    mans = []
    for i in range(N):
        for j in range(N):
            if board[i][j] > 1:
                stairs.append((i, j, board[i][j]))
            elif board[i][j] == 1:
                mans.append([i, j])
    infos = []
    for j in mans:
        infos.append(
            [
                abs(stairs[0][0] - j[0]) + abs(stairs[0][1] - j[1]),    # 1번계단과의 거리
                abs(stairs[1][0] - j[0]) + abs(stairs[1][1] - j[1])     # 2번계단과의 거리
            ]
        )
    print(infos)
    for possibles in possibles[len(mans)]:
        timeboard1 = [[0] * 30 for i in range(len(mans))]
        timeboard2 = [[0] * 30 for i in range(len(mans))]
        for i in range(len(mans)):
            if possibles[i] == 0:    # 1번계단
                for j in range(infos[i][0] + 1, infos[i][0] + 4):
                    cnt = len(mans) - list(map(list, zip(*timeboard1)))[j].count(0) + 1
                    timeboard1[i][j] = cnt
            else:   # 2번계단
                for j in range(infos[i][1] + 1, infos[i][1] + 4):
                    cnt = len(mans) - list(map(list, zip(*timeboard2)))[j].count(0) + 1
                    timeboard2[i][j] = cnt
    print(possibles)
    print(timeboard1)
    print(timeboard2)
    # print("#{} {}".format(tc, max(infos)))
