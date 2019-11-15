# dictionary를 활용한 줄기세포 문제 풀기
t = int(input())
for tc in range(1, t + 1):
    # N 줄마다 M개의 그리드 상태 정보, K 는 배양시간
    N, M, K = map(int, input().split())
    greeds = [list(map(int, input().split())) for i in range(N)]

    infos = {}
    for i in range(N):
        for j in range(M):
            if greeds[i][j] > 0:
                # 상태 0 비활성 1 활성 2 사망 처리 필요
                infos[(i, j)] = [greeds[i][j], greeds[i][j], 0]  # 원래 세포가치, 활성시간, 현재상태
    direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    time = 0
    while time != K:
        # print(infos, time)
        time += 1
        addlist = {}
        for key, value in infos.items():
            if value[2] == 0:  # 비활성이라면
                if value[1] - 1 == 0:
                    infos[key][2] = 1  # 활성화!  살아있는 시간 만들어주기
                    infos[key][1] = infos[key][0]   # 활성화하면서 생존시간 초기화
                else:
                    infos[key][1] -= 1  # 시간 줄이기
            elif value[2] == 1:  # 활성중이면
                infos[key][1] -= 1  # 시간 줄이기
                if value[1] == 0:  # 사망처리
                    infos[key][2] = 2
                if infos[key][1] + 1 == infos[key][0]:  # 바로 이전에 활성이었다면 늘려주기
                    # 확장
                    col, row = key
                    for direct in direction:
                        nc = col + direct[0]
                        nr = row + direct[1]
                        if (nc, nr) not in infos:  # infos에 사용되지 않은 값일 때
                            if (nc, nr) in addlist:  # 이미 값이 들어있다면 추가하려는 항목에 들어있다면
                                # 들어있는게 방금 추가한 값이라면, 비활성상태의 시간이 안지난 세포
                                if addlist[(nc, nr)][2] == 0 and addlist[(nc, nr)][1] == addlist[(nc, nr)][0]:
                                    # 넣으려는 생명력이 더 크다면
                                    if addlist[(nc, nr)][0] < value[0]:
                                        addlist[(nc, nr)] = [value[0], value[0], 0]  # 새로추가
                                    # 작다면 무시
                            else:  # 없다면
                                addlist[(nc, nr)] = [value[0], value[0], 0]  # 비활성화 상태로 추가

        # addlist 처리
        for key, value in addlist.items():
            infos[key] = value
    cnt = 0
    for key, value in infos.items():
        if value[2] == 0 or value[2] == 1:  # 마지막에 사망했다면
            cnt += 1
    print("#{} {}".format(tc, cnt))
