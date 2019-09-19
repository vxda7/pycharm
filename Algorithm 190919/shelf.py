def find(n, N, B, tall):
    global minV, talls
    if n == N:
        if minV > tall and B <= tall:
            minV = tall
    elif tall > minV:
        return
    else:
        find(n + 1, N, B, tall + talls[n])
        find(n + 1, N, B, tall)


t = int(input())
for tc in range(1, t+1):
    N, B = map(int, input().split())
    talls = list(map(int, input().split()))
    minV = sum(talls)
    find(0, N, B, 0)
    # print(minV)
    print("#{} {}".format(tc, minV - B))