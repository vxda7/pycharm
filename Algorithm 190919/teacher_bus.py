def f(n, k, e, c):
    global minV, stations
    if n == k:
        if c < minV:
            minV = c
        return
    elif e < 0:
        return
    else:
        f(n + 1, k, stations[n] - 1, c + 1)  # 교체
        f(n + 1, k, e - 1, c)  # 통과


t = int(input())
for tc in range(1, t + 1):
    stations = list(map(int, input().split()))
    N = stations[0]
    stations = stations[1:]
    minV = N-1
    f(0, N-1, stations[0], 0)
    print("#{} {}".format(tc, minV))
