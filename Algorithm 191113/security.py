t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())    # 마을크기, 집이 지불가능한 비용
    homes = [list(map(int, input().split())) for i in range(N)]
    maxV = 0
    a = 0
    for K in range(1, N + 1):
        operate_cost = K * K + (K-1) * (K-1)
        # if K % 2 == 1 and K != 1:
        #     a += 1
        for i in range(N):
            for j in range(N):
                num_house = 0
                start, end = j, j
                for col in range(i - (K - 1), i + (K - 1)):
                    if 0 <= col < N:
                        for row in range(start, end + 1):
                            if 0 <= row < N:
                                if homes[col][row] > 0:
                                    num_house += homes[col][row]
                    if col < i:
                        start -= 1
                        end += 1
                    else:
                        start += 1
                        end -= 1
                cost = num_house * M - operate_cost
                # print(cost)
                if K == 4:
                    print(i, j, cost, num_house)
                if cost >= 0:
                    if num_house > maxV:
                        print(i,j, K)
                        maxV = num_house


    print("#{} {}".format(tc, maxV))