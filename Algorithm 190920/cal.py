def find(N, M, t):
    global minV
    if N == M:
        if t < minV:
            minV = t
    elif t >= minV:
        return
    if 0 < N <= 1000000:
        find(N + 1, M, t + 1)
        find(N - 1, M, t + 1)
        find(N * 2, M, t + 1)
        find(N - 10, M, t + 1)


t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split())
    minV = 1000000000000000
    find(N, M, 0)
    print("#{} {}".format(tc, minV))