import time
import sys

sys.stdin = open("input (10).txt", "r")
start = time.time()


def perm(start, num, cnt):
    global maxV, wow, wownum
    if start == cnt:
        answer = int(''.join(num))
        if maxV < answer:
            maxV = answer
    else:
        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                num[i], num[j] = num[j], num[i]
                if num == wow:
                    wownum = start + 1
                perm(start + 1, num, cnt)
                num[i], num[j] = num[j], num[i]


t = int(input())
for tc in range(1, t + 1):
    num, cnt = input().split()
    num = list(num)
    cnt = int(cnt)
    N = [i for i in range(len(num))]
    maxV = 0
    wow = list(reversed(sorted(num)))

    first = True
    did = False
    wownum = 10000000000
    if cnt < 5:
        perm(0, num, cnt)
    else:
        perm(0, num, len(num) - 1)
        if (cnt - wownum) % 2 == 1:
            maxV = wow
            maxV[-1], maxV[-2] = maxV[-2], maxV[-1]
            maxV = ''.join(maxV)
    print("#{} {}".format(tc, maxV))
    # print(time.time() - start)
