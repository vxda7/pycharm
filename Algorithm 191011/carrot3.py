T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    carrots = [list(map(int, input().split())) for i in range(N)]
    minV = 100000000

    for i in range(N-1):
        for j in range(M-1):
            farmer1, farmer2, farmer3 = 0, 0, 0
            for k in range(0, i+1):
                for l in range(0, j+1):
                    farmer1 += carrots[k][l]

            for k in range(0, i+1):
                for l in range(j+1, M):
                    farmer2 += carrots[k][l]

            for k in range(i+1, N):
                farmer3 += sum(carrots[k])

            res = max(abs(farmer1 - farmer2), abs(farmer2 - farmer3), abs(farmer3 - farmer1))
            if minV > res:
                minV = res

    print("#{} {}".format(tc, minV))


