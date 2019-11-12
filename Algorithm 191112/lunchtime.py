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

def find(poss, people, N):
    print(poss)
    tempmans = mans[:]
    tempinfos = infos[:]
    time = 0
    waiting1 = [0] * 3
    waiting2 = [0] * 3
    w1idx = 0
    w2idx = 0
    check = 0
    while check != people or sum(waiting1) or sum(waiting2):
        time += 1
        for pi in range(people):
            if tempinfos[pi][2]:    # 아직 못내려갔다면
                if poss[pi] == 1:   # 1번 계단을 쓴다면
                    if tempinfos[pi][0] > 0:    # 계단에 가까이 가기
                        tempinfos[pi][0] -= 1
                    if tempinfos[pi][0] == 0:
                        # 계단에 사람이 더 들어갈 수 있다면 추가
                        if w1idx < 3:   # 아직 계단에 공간이 있다면
                            waiting1[w1idx] = stairs[0][2]
                            tempinfos[pi][0] = -1
                            check += 1
                            w1idx += 1
                else:       # 2번 계단을 쓴다면
                    if tempinfos[pi][1] > 0:
                        tempinfos[pi][1] -= 1
                    if tempinfos[pi][1] == 0:
                        if w2idx < 3:
                            waiting2[w2idx] = stairs[1][2]
                            tempinfos[pi][1] = -1
                            check += 1
                            w2idx += 1
        for i in range(3):
            if waiting1[i] > 0:
                waiting1[i] -= 1
                if waiting1[i] == 0:
                    w1idx -= 1
            if waiting2[i] > 0:
                waiting2[i] -= 1
                if waiting2[i] == 0:
                    w2idx -= 1
        if time == 100:
            break
        print(time, waiting1, waiting2, check, w1idx, w2idx, tempinfos)
    return time


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
        infos.append([
            abs(stairs[0][0] - j[0]) + abs(stairs[0][1] - j[1]),
            abs(stairs[1][0] - j[0]) + abs(stairs[1][1] - j[1]),
            True
        ])
    print(infos)
    minV = 1000000
    for possible in possibles[len(mans)]:
        if possible:
            now = find(possible, len(mans), N)
            if now < minV:
                minV = now
    print("#{} {}".format(tc, minV))