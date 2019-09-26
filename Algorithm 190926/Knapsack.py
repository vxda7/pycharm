import time

start = time.time()


def make(num, volume, value, t):
    global N, K, volumelist, valuelist, maxV, cnt
    cnt += 1
    if maxV < value and volume <= K:
        maxV = value
    if num == N or value + t <= maxV or volume >= K:
        return
    else:
        make(num + 1, volume + volumelist[num], value + valuelist[num], t - valuelist[num])
        make(num + 1, volume, value, t - valuelist[num])


t = int(input())
for tc in range(1, t + 1):
    N, K = map(int, input().split())
    volumelist = [0] * N
    valuelist = [0] * N
    for i in range(N):
        volumelist[i], valuelist[i] = map(int, input().split())
    maxV = 0
    t = sum(valuelist)
    cnt = 0
    make(0, 0, 0, t)  # 갯수 부피 가치 남은물건들의가치
    print("#{} {}".format(tc, maxV))
print(cnt)
print(time.time() - start)
