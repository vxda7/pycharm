t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())    # 마을크기, 집이 지불가능한 비용
    homes = [list(map(int, input().split())) for i in range(N)]
    maxV = 0
    a = 0
    for K in range(1, N + 2):
        operate_cost = K * K + (K-1) * (K-1)
        if K % 2 == 1 and K != 1:
            a += 1
        for i in range(N-a):
            for j in range(N-a):
                num_house = 0

                for b in range(N):
                    for d in range(N):
                        if abs(i-b) + abs(j-d) <= K - 1:
                            if homes[b][d] == 1:
                                num_house += 1
                cost = num_house * M - operate_cost

                if cost >= 0:
                    if num_house > maxV:
                        maxV = num_house

    print("#{} {}".format(tc, maxV))