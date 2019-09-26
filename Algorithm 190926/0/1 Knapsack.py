import time
start = time.time()

def find(N, K):
    maxV = 0
    for i in range(1 << N):
        value = 0
        space = 0
        for j in range(N):
            if i & (1 << j):
                value += values[j][1]
                space += values[j][0]
        if space <= K:
            if maxV < value:
                maxV = value
    return maxV


t = int(input())
for tc in range(1, t + 1):
    N, K = map(int, input().split())
    values = [list(map(int, input().split())) for i in range(N)]
    print("#{} {}".format(tc, find(N, K)))

print(time.time() - start)