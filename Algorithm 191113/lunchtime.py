t = int(input())
for tc in range(1, t+1):
    N = int(input())
    up = [list(map(int, input().split())) for i in range(N)]
    stairs = []
    mans = []

    for i in range(N):
        for j in range(N):
            if up[i][j] > 1:
                stairs.append((i, j, up[i][j]))
            elif up[i][j] == 1:
                mans.append((i, j))

    people = len(mans)
    infos_one = []
    infos_two = []
    for i in range(people):
        infos_one.append(abs(mans[i][0] - stairs[0][0]) + abs(mans[i][1] - stairs[0][1]))
        infos_two.append(abs(mans[i][0] - stairs[1][0]) + abs(mans[i][1] - stairs[1][1]))

    possible = []
    for i in range(1 << people):
        temp = []
        for j in range(people):
            if i & (1 << j):
                temp.append(0)
            else:
                temp.append(1)
        possible.append(temp[:])

    minV = 1000000000
    for poss in possible:
        under = 0
        time = 0
        info1 = infos_one[:]
        info2 = infos_two[:]
        wait_one = []
        wait_two = []
        # print('######', poss)
        while under != people and time != 50:
            time += 1
            # print(info1, info2)
            if wait_two or wait_one:
                deadlist1 = []
                deadlist2 = []
                for i in range(3):
                    if i < len(wait_one):
                        if wait_one[i] > 0:
                            wait_one[i] -= 1
                        if wait_one[i] == 0:
                            deadlist1.append(i)
                            under += 1
                    if i < len(wait_two):
                        if wait_two[i] > 0:
                            wait_two[i] -= 1
                        if wait_two[i] == 0:
                            deadlist2.append(i)
                            under += 1
                for i in deadlist1:
                    wait_one.remove(0)
                for i in deadlist2:
                    wait_two.remove(0)

            for i in range(people):
                if poss[i] == 0:  # 1번계단을 쓰면
                    if info1[i] != -1:
                        info1[i] -= 1
                        if info1[i] == -1:
                            wait_one.append(stairs[0][2])   # 대기시간
                else:
                    if info2[i] != -1:
                        info2[i] -= 1
                        if info2[i] == -1:
                            wait_two.append(stairs[1][2])
            # print(time, under, wait_one, wait_two)
        if minV > time:
            minV = time

    print("#{} {}".format(tc, minV))
