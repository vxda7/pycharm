import sys
sys.stdin = open("sample_input (7).txt", "r")

def change(get):
    if get == 1:
        return 2
    elif get == 2:
        return 1
    elif get == 3:
        return 4
    elif get == 4:
        return 3


t = int(input())
for tc in range(1, t + 1):
    N, M, K = map(int, input().split())
    info = [list(map(int, input().split())) for i in range(K)]
    # 0을 제외한 이동방향 상하좌우
    dc = [0, -1, 1, 0, 0]
    dr = [0, 0, 0, -1, 1]

    locations = {}

    while M != 0:
        for infoidx in range(len(info)):  # 한칸 씩 이동시키기
            direction = info[infoidx][3]
            info[infoidx][0] += dc[direction]
            info[infoidx][1] += dr[direction]
        # 서로 겹치는 지와 테두리에 닿았는지 확인

        checkidx = 0
        for do in range(len(info)):
            crosson = False
            col = info[checkidx][0]
            row = info[checkidx][1]
            deadlist = []
            if col == 0 or col == N-1 or row == 0 or row == N-1:  # 주변에 닿았다면
                if info[checkidx][2] == 1:  # 미생물 수 가 1이라면 삭제목록에 추가
                    deadlist.append(info[checkidx][:])
                else:  # 아니라면
                    info[checkidx][2] //= 2  # 2로 나눈 몫 주기
                    info[checkidx][3] = change(info[checkidx][3])  # 방향 주기
            else:
                cross = [info[checkidx][:]]  # 겹치는 정보 넣을 곳
                # 겹치는 항목이 있는지 확인
                for otheridx in range(checkidx + 1, len(info)):
                    if col == info[otheridx][0] and row == info[otheridx][1]:  # 같은 위치라면
                        cross.append(info[otheridx][:])
                        crosson = True

                if crosson:
                    # 겹치는 것들을 미생물 크기 순으로 정렬
                    cross.sort(key=lambda x: x[2])
                    # 겹치는 항목들을 가장 뒤에 값에 더해주고 모두 삭제목록에 추가
                    deadlist.append(cross[-1][:])
                    for crossidx in range(len(cross) - 1):
                        cross[-1][2] += cross[crossidx][2]
                        deadlist.append(cross[crossidx][:])
                    # 겹치는 것중 미생물이 많은 녀석을 넣어주기
                    info.append(cross[-1][:])

            # 지울 것이 있다면 지우기
            if deadlist:
                for dead in deadlist:
                    info.remove(dead)
                checkidx -= 1
            if checkidx == len(info)-1:  # 마지막 지점이면 종료
                break
            checkidx += 1
        M -= 1
    micros = 0
    for micro in info:
        micros += micro[2]

    print("#{} {}".format(tc, micros))
