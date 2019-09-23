# def find(s, A, D):
#     global N, E
#     U = {s}
#     V = set(range(N + 1))
#     for v in range(N + 1):
#         D[v] = A[s][v]
#     while U != V:
#         minV = 100000000000000
#         for i in V - U:
#             if D[i] < minV:
#                 minV = D[i]
#                 w = i
#         # w = D.index(min([D[i] for i in V - U]))
#         U.add(w)
#         for v in range(N + 1):
#             if 0 < A[w][v] < 10001:
#                 D[v] = min(D[v], D[w] + A[w][v])



t = int(input())
for tc in range(1, t + 1):
    N, E = map(int, input().split())
    sew = [list(map(int, input().split())) for i in range(E)]
    near = [[10001] * (N + 1) for i in range(N + 1)]
    for i in sew:
        near[i[0]][i[1]] = i[2]
    for i in range(N + 1):
        near[i][i] = 0
    D = near[0]
    U = {0}
    V = set(range(N + 1))
    while U != V:
        minV = 100000000000000
        for i in V - U:
            if D[i] < minV:
                minV = D[i]
                w = i
        U.add(w)
        for v in range(N + 1):
            if 0 < near[w][v] < 10001:
                D[v] = min(D[v], D[w] + near[w][v])
    print("#{} {}".format(tc, D[-1]))
