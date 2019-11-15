def find(chosen, direct, left, right):     # 선택된 시계, 방향, 주변에 영향 주는지
    if chosen == 0:
        if infos[chosen][2] != infos[chosen + 1][-2] and right:
            find(chosen + 1, direct * -1, False, True)
        if direct == 1:
            infos[chosen].insert(0, infos[chosen].pop())    # 시계방향 돌리기
        else:
            infos[chosen].append(infos[chosen].pop(0))  # 반시계 돌리기
    elif chosen == 1:
        if infos[chosen][2] != infos[chosen + 1][-2] and right:
            find(chosen + 1, direct * -1, False, True)
        if infos[chosen][-2] != infos[chosen - 1][2] and left:
            find(chosen - 1, direct * -1, True, False)
        if direct == 1:
            infos[chosen].insert(0, infos[chosen].pop())    # 시계방향 돌리기
        else:
            infos[chosen].append(infos[chosen].pop(0))  # 반시계 돌리기
    elif chosen == 2:
        if infos[chosen][2] != infos[chosen + 1][-2] and right:
            find(chosen + 1, direct * -1, False, True)
        if infos[chosen][-2] != infos[chosen - 1][2] and left:
            find(chosen - 1, direct * -1, True, False)
        if direct == 1:
            infos[chosen].insert(0, infos[chosen].pop())    # 시계방향 돌리기
        else:
            infos[chosen].append(infos[chosen].pop(0))  # 반시계 돌리기
    elif chosen == 3:
        if infos[chosen][-2] != infos[chosen - 1][2] and left:
            find(chosen - 1, direct * -1, True, False)
        if direct == 1:
            infos[chosen].insert(0, infos[chosen].pop())    # 시계방향 돌리기
        else:
            infos[chosen].append(infos[chosen].pop(0))  # 반시계 돌리기


t = int(input())
for tc in range(1, t+1):
    K = int(input())
    # 시계 방향으로 N극: 0  S극: 1
    infos = [list(map(int, input().split())) for i in range(4)]
    # 시계방향 1, 반시계 -1
    commands = [list(map(int, input().split())) for i in range(K)]
    # 명령실행!
    for cmd in commands:
        chosen = cmd[0] - 1 # 자석의 번호를 자석의 인덱스로
        direct = cmd[1]
        find(chosen, direct, True, True)

    score = 0
    for i in range(4):
        if infos[i][0] == 1:
            score += 2 ** i
    print("#{} {}".format(tc, score))


