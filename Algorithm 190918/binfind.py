def find(x, l, r):
    global A, cnt, lok, rok
    m = (l + r) // 2
    # print(A[m], x, l, r, m)
    if A[m] == x:
        # print("yeab")
        return 1
    elif m == l:
        if lok and rok:
            return 1
        else:
            return 0
    elif x > A[m]:
        lok = True
        return find(x, m + 1, r)
    elif x < A[m]:
        rok = True
        return find(x, l, m)


t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cnt = 0
    for i in range(M):
        l, r, lok, rok = 0, len(A) - 1, False, False
        cnt += find(B[i], l, r)
    print("#{} {}".format(tc, cnt))
