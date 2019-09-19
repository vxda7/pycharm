def find(now):
    global minV, stations, N
    for i in range(now):
        if now - i <= stations[i]:
            minV += 1
            find(i)
            break


t = int(input())
for tc in range(1, t+1):
    stations = list(map(int, input().split()))
    N = stations[0]
    stations = stations[1:]
    minV = 0
    find(N-1)
    print("#{} {}".format(tc, minV-1))