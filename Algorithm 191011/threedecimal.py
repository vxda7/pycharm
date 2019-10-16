def decimal(N):
    delist = [False]*2 + [True]*(N-1)
    m = int(N ** 0.5)
    for i in range(2, m+1):
        if delist[i]:
            for j in range(i+i, N+1, i):
                delist[j] = False
    return delist


T = int(input())
delist = decimal(999)
for tc in range(1, T + 1):
    N = int(input())
    cnt = 0
    for i in range(2, N//3+1):
        if delist[i]:
            for j in range(i, (N-i)//2+1):
                if delist[j]:
                    for k in range(j, N-i-j+1):
                        if delist[k]:
                            if N == i+j+k:
                                cnt += 1
                        # print(i,j,k)
    print("#{} {}".format(tc, cnt))
