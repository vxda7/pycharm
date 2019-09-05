# import sys
# sys.stdin = open("sample_input (7).txt", "r")

t = int(input())
for tc in range(1, t + 1):
    N, M, K = map(int, input().split())
    info = []
    for i in range(K):
        col, row, nums, direct = map(int, input().split())
        info.append([col, row, nums, direct])
    # 0을 제외한 이동방향 상하좌우
    dc = [0, -1, 1, 0, 0]
    dr = [0, 0, 0, -1, 1]
    happend = False  # 겹치는 경우가 발생할경우
    while M != 0:   # 시간이 다 될 때 까지
        print(info)
        for i in range(K):     # 방향으로 이동
            info[i][0] += dc[info[i][3]]
            info[i][1] += dr[info[i][3]]
        print(info)
        i = 0      # 지우는 것을 대비한 i 현재 값
        temp = []
        for k in range(K):  #
            col = info[i][0]
            row = info[i][1]

            tidx = 0
            for o in range(K):
                if col == info[tidx][0] and row == info[tidx][1]:
                    happend = True
                    temp.append(info[tidx])
                    del info[tidx]
                    K -= 1
                    i -= 1
                    tidx -= 1
                tidx += 1

            temp.append(info[i])
            if happend:
                happend = False
                temp.sort(key=lambda x: x[2])
                for find in range(len(temp) - 1):
                    temp[-1][2] += temp[find][2]
                del info[i]
                K -= 1
                i -= 1
                info.append(temp[-1])

            elif col == N or col == 0 or row == N or row == 0:
                if info[i][2] == 1:  # 벽에 닿아 모두 죽으면
                    del info[i]
                    K -= 1
                    i -= 1
                else:
                    info[i][2] //= 2
            i += 1
        print(info)
        M -= 1
    hap = 0
    for i in range(K):
        hap += info[i][2]

    print("#{} {}".format(tc, hap))
