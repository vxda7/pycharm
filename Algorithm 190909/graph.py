def find(n):
    global connect
    a = connect[n]
    cnt = 0
    for i in range(len(a)):
        if n < a[i]:
            b = connect[a[i]]
            for j in range(len(b)):
                if a[i] < b[j]:
                    c = connect[b[j]]
                    if n in c:
                        # print("-----------")
                        # print(n, a)
                        # print(a[i], b)
                        # print(b[j], c)
                        cnt += 1
    return cnt


t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split())
    connect = {i: [] for i in range(1, N + 1)}
    for i in range(M):
        x, y = map(int, input().split())
        connect[x].append(y)
        connect[y].append(x)

    triangle = 0
    for i in range(1, N + 1):
        triangle += find(i)
    print("#{} {}".format(tc, triangle))
