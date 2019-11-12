import copy
# 1번계단일지 2번계단일지 조합
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
    upstairs = [list(map(int, input().split())) for i in range(N)]
    # 입력받음

    # 정보가공
    stairs = []
    infos = []
    for i in range(N):
        for j in range(N):
            if upstairs[i][j] == 1:
                infos.append((i, j))
            elif upstairs[i][j] > 1:
                stairs.append((i, j, upstairs[i][j]))

    # 추가가공
    diffs1 = []
    diffs2 = []
    for i in range(len(infos)):
        colstairs1 = abs(infos[i][0] - stairs[0][0])
        rowstairs1 = abs(infos[i][1] - stairs[0][1])
        colstairs2 = abs(infos[i][0] - stairs[1][0])
        rowstairs2 = abs(infos[i][1] - stairs[1][1])
        diffs1.append(colstairs1 + rowstairs1)
        diffs2.append(colstairs2 + rowstairs2)
    diffs1.sort()
    diffs2.sort()

    # possible 1로 갈지 2로 갈지
    timetable = [[0]*50 for i in range(len(diffs1))]
    added = 0
    for possible in possibles[len(diffs1)]:     # 모든 가능성 보기
        timetable1 = copy.deepcopy(timetable)
        timetable2 = copy.deepcopy(timetable)
        minV = 10000
        for didx in range(len(diffs1)):     # 가까운 순서대로 고르기
            maxV = 0
            if possible[didx] == 0:     # 1번계단
                for k in range(3):  # 3칸
                    start = diffs1[didx] + 1   # 이동거리 + 대기시간
                    cnt = len(diffs1) + 1 - list(map(list, zip(*timetable1)))[start].count(0)
                    # 대기시간 + 1칸
                    while cnt >= 4:     # 4이상의 값이면 우측으로
                        start += 1      # 한칸 옮기기
                        added += 1
                        cnt = len(diffs1) + 1 - list(map(list, zip(*timetable1)))[start].count(0)
                        # 세로에 0값이 아닌 수의 갯수 세기 + 1
                    timetable1[didx][start + k] = cnt   # 그 갯수 값 넣어주기
                    if start + k > maxV:
                        maxV = start + k
            elif possible[didx] == 1:      # 2번계단
                for k in range(3):
                    start = diffs2[didx] + 1
                    cnt = len(diffs2) + 1 - list(map(list, zip(*timetable2)))[start].count(0)
                    while cnt >= 4:
                        start += 1
                        added += 1
                        cnt = len(diffs2) + 1 - list(map(list, zip(*timetable2)))[start].count(0)
                    timetable2[didx][start + k] = cnt
                    if start + k > maxV:
                        maxV = start + k
        if minV > maxV:
            minV = maxV
        # if minV == 10:
        #     print(timetable1)
        #     print(timetable2)
    print("#{} {}".format(tc, minV - 1))