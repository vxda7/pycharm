def make(num, volume, value, t):
    global N, K, things, maxV
    if maxV < value and volume <= K:
        maxV = value
    if num == N or value + t <= maxV:
        return
    else:
        make(num + 1, volume + things[num][0], value + things[num][1], t - things[num][1])
        make(num + 1, volume, value, t - things[num][1])


t = int(input())
for tc in range(1, t + 1):
    N, K = map(int, input().split())
    things = [list(map(int, input().split())) for i in range(N)]
    maxV = 0
    t = 0
    for i in range(N):
        t += things[i][1]
    make(0, 0, 0, t)  # 갯수 부피 가치 남은물건들의가치
    print("#{} {}".format(tc, maxV))
