import sys
import time
start = time.time()
sys.stdin = open("input (1).txt", "r")

t = int(input())
for tc in range(1, t + 1):
    N, B = map(int, input().split())
    talls = list(map(int, input().split()))


    possible = set()
    for i in range(1 << N):
        this = 0
        for j in range(N):
            if i & (1 << j):
                this += talls[j]
        possible.add(this)

    res = 0
    possible = list(possible)
    possible.sort()
    # print(B, possible)
    minV = 100000000000000000000
    for i in possible:
        if i==B:
            this = 0
            break
        elif B < i:
            this = i-B
            break
            # if this < minV:
            #     minV = this
    res = this
    print("#{} {}".format(tc, res))

print(time.time() - start)