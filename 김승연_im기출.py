def turnon(cnt, n):
    global gets
    global test
    cnt += 1
    for i in range(cnt, n+1, cnt):
        i -= 1
        if test[i] == 0:
            test[i] = 1
        else:
            test[i] = 0


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    gets = list(map(int, input().split()))
    test = [0]*n
    cnt = 0
    res = 0
    # print(gets)
    while test != gets:
        # print(test)
        if gets[cnt] != test[cnt]:
            turnon(cnt, n)
            res += 1
        cnt += 1

        if cnt >= n:
            cnt -= n

    print("#{} {}".format(tc, res))