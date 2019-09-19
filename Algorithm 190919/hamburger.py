def make(N, L):
    global foods
    maxV = 0
    for i in range(1 << N):
        temp = []
        for j in range(N):
            if i & (1 << j):
                temp.append(j)
        calory = 0
        score = 0
        for k in range(N):
            if k in temp:
                calory += foods[k][1]
                score += foods[k][0]
        if calory <= L and maxV < score:
            maxV = score
    return maxV


t = int(input())
for tc in range(1, t + 1):
    N, L = map(int, input().split())
    foods = [list(map(int, input().split())) for i in range(N)]
    res = make(N, L)
    print("#{} {}".format(tc, res))