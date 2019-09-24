def find(N, start):
    D = near[start]
    U = {start}
    V = {i for i in range(1, N + 1)}
    while U != V:
        minV = 1000000000
        for k in V - U:
            if D[k] < minV:
                minV = D[k]
                minidx = k
        U.add(minidx)
        for i in range(1, N + 1):
            if 0 < near[minidx][i] < 1000000:
                D[i] = min(D[i], D[minidx] + near[minidx][i])
    return D


def comback(N, start):
    D = []
    for i in range(N + 1):
        D.append(near[i][start])
    U = {start}
    V = {i for i in range(1, N + 1)}
    while U != V:
        minV = 1000000
        for k in V - U:
            if D[k] < minV:
                minV = D[k]
                minidx = k
        U.add(minidx)
        for i in range(1, N + 1):
            if 0 < near[i][minidx] < 1000000:
                D[i] = min(D[i], D[minidx] + near[i][minidx])
    return D


t = int(input())
for tc in range(1, t + 1):
    N, M, X = map(int, input().split())
    near = [[1000000] * (N + 1) for i in range(N + 1)]
    for i in range(M):
        x, y, c = map(int, input().split())
        near[x][y] = c
    for i in range(N + 1):
        near[i][i] = 0
    # 입력받고 근사행렬 완성
    D = find(N, X)
    A = comback(N, X)
    answer = [0] * (N + 1)
    for i in range(1, N + 1):
        answer[i] = D[i] + A[i]
    print("#{} {}".format(tc, max(answer[1:])))
