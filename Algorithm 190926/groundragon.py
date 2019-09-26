import sys, time
sys.stdin = open('groundragon.txt', 'r')
start = time.time()
def find(now, N):
    global minV
    if now == N:
        x = 0
        y = 0
        for i in range(N//2):
            x += where[i * 2][0] - where[i * 2 + 1][0]
            y += where[i * 2][1] - where[i * 2 +1][1]
        res = x**2 + y**2
        if minV > res:
            minV = res
    else:
        for i in range(now, N):
            where[now], where[i] = where[i], where[now]
            find(now+1, N)
            where[now], where[i] = where[i], where[now]


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    where = [list(map(int, input().split())) for i in range(N)]
    minV = 1000000000000
    find(0, N)
    print(minV)
    print(time.time() - start)
