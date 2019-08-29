t = int(input())
for tc in range(1, t+1):
    N, K = map(int, input().split())
    V = []
    C = []
    for i in range(N):
        v, c = map(int, input().split())
        V.append(v)
        C.append(c)
    all = []
    for i in range(1 << N):
        temp = []
        over = 0
        value = 0
        for j in range(N):
            if i & (1 << j):
                temp.append([V[j], C[j]])
                over += V[j]
                value += C[j]
        if over <= K:   # 넣을 조합 값이 가방 부피보다 적으면
            all.append(value)    # 가치 합을 넣는다.
    print("#{} {}".format(tc, max(all)))